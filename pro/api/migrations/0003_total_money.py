# Generated by Django 5.0.8 on 2025-02-22 22:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_loandetails_loan_loanstatus'),
    ]

    operations = [
        migrations.CreateModel(
            name='Total_money',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_money', models.FloatField(default=0)),
            ],
        ),
    ]
