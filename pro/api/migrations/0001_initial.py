# Generated by Django 5.0.8 on 2025-02-22 15:39

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_budget', models.FloatField(default=0.0)),
                ('account_profit', models.FloatField()),
                ('account_user', models.ForeignKey(limit_choices_to=models.Q(('groups__name', 'Loan_Provider'), ('groups__name', 'Loan_Customer'), _connector='OR'), on_delete=django.db.models.deletion.CASCADE, related_name='Account', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Fund',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_budget', models.FloatField()),
                ('status', models.CharField(choices=[('PENDING', 'Pending'), ('APPROVED', 'Approved'), ('REJECTED', 'Rejected')], default='PENDING', max_length=20)),
                ('provider', models.ForeignKey(limit_choices_to={'groups__name': 'Loan_Provider'}, on_delete=django.db.models.deletion.CASCADE, related_name='Fund', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
