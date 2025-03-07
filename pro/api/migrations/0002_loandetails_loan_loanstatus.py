# Generated by Django 5.0.8 on 2025-02-22 21:10

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='LoanDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('min_loan', models.FloatField()),
                ('max_loan', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Loan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('loan_amount', models.FloatField()),
                ('Installments', models.IntegerField(default=1)),
                ('status', models.CharField(choices=[('PENDING', 'Pending'), ('APPROVED', 'Approved'), ('REJECTED', 'Rejected'), ('FINISHED', 'Finished')], default='PENDING', max_length=20)),
                ('interst_rate', models.FloatField(default=0.1)),
                ('customer', models.ForeignKey(limit_choices_to={'groups__name': 'Loan_Customer'}, on_delete=django.db.models.deletion.CASCADE, related_name='Loan', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='LoanStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('single_Installments', models.FloatField()),
                ('Installments_paid', models.IntegerField(default=0)),
                ('duration_left', models.IntegerField(default=0)),
                ('customer', models.ForeignKey(limit_choices_to={'groups__name': 'Loan_Customer'}, on_delete=django.db.models.deletion.CASCADE, related_name='LoanStatus', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
