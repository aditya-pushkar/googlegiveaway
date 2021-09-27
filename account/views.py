from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.sites.shortcuts import get_current_site
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode

# internal import 
from .forms import RegistrationForm
from feed.forms import UplodeImageForm
from .token import account_activation_token
from .models import UserBase
from refferal.models import Refferal
from feed.models import UplodedPic



# Create your views here.
@login_required
def dashboard(request):
    user = request.user 
    refferal_profile = Refferal.objects.get(user=user)
    my_pic = UplodedPic.objects.filter(user=user)
    
    error = False
    for i in my_pic:
        if i != None:
            error = True
        
    
    # user earning
    refferals_earnings = refferal_profile.get_refferal_earnings()
    # people who joinded from user  link
    refferal_profile_detail  = refferal_profile.get_refferal_profiles()
    # total number of user joined by user refferal code 
    refferal_count = len(refferal_profile_detail)
    # users refferal/invite code 
    current_site = get_current_site(request)
    refferal_code = f"{current_site.domain}/{refferal_profile.code}"

    
    formUplode = UplodeImageForm()
    if request.method == "POST":
        formUplode = UplodeImageForm(request.POST, request.FILES)
        if formUplode.is_valid():

            form = formUplode.save(commit=False)
            form.user = user
            form.img = formUplode.cleaned_data['img']
            form.save()

            return redirect('account:success')
        else:
            pass
    
    context = {
        'form': formUplode,
        'refferal_count': refferal_count,
        'refferals_earnings': refferals_earnings,
        'refferal_profile_detail':refferal_profile_detail,
        'refferal_code': refferal_code,
        'error': error
     
    }  
    # print('error', error)
    return render(request, 'account/dashboard.html', context)


def success(request):
    return HttpResponse('your pic is uploded successfuly')

def test(request):
    return render(request, "account/test.html")

def account_register(request):
    if request.user.is_authenticated:
        return redirect('account:dashboard')
    # get refferal code  
    refferal_id = request.session.get('ref_profile')
    print('profile_id', refferal_id)
    if request.method == 'POST':
        registerForm = RegistrationForm(request.POST)

        if registerForm.is_valid():
            
            if refferal_id is not None:
                recommended_by_profile = Refferal.objects.get(id=refferal_id)
                print("recommended_by_profile", recommended_by_profile)
                instance = registerForm.save()
                registered_user  = UserBase.objects.get(id=instance.id)
                registered_profile = Refferal.objects.get(user=registered_user)
                registered_profile.recommended_by = recommended_by_profile.user
                registered_profile.save()


                user = registerForm.save(commit=False)
                user.email = registerForm.cleaned_data['email']
                user.set_password(registerForm.cleaned_data['password'])
                user.is_active = False
                user.save()

                current_site = get_current_site(request)
                subject = 'Activate your Account'
                message = render_to_string('account/account_activation_email.html', {
                    'user': user,
                    'domain': current_site.domain,
                    'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                    'token': account_activation_token.make_token(user),
                })
                user.email_user(subject=subject, message=message)
                return HttpResponse('registered succesfully and activation sent')
            else:
                user = registerForm.save(commit=False)
                user.email = registerForm.cleaned_data['email']
                user.set_password(registerForm.cleaned_data['password'])
                user.is_active = False
                user.save()
                current_site = get_current_site(request)
                subject = 'Activate your Account'
                message = render_to_string('account/account_activation_email.html', {
                    'user': user,
                    'domain': current_site.domain,
                    'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                    'token': account_activation_token.make_token(user),
                })
                user.email_user(subject=subject, message=message)
                return HttpResponse('registered succesfully and activation sent')

    else:
        registerForm = RegistrationForm()
    return render(request, 'account/register.html', {'form': registerForm})


def account_activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = UserBase.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, user.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        return redirect('account:dashboard')
    else:
        return render(request, 'account/activation_invalid.html')
