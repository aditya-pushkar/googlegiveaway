# Generated by Django 3.2.7 on 2021-09-19 23:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0003_payment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='status',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='payment',
            name='user_product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='order.order'),
        ),
    ]