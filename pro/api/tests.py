from django.test import TestCase

# Create your tests here.
from django.contrib.auth.models import User, Group
from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models.provider import Fund, Account
from .models.customer import Loan, LoanStatus
from .models.banker import Total_money, LoanDetails


class AuthenticationTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='testpass')

    def test_user_signup(self):
        response = self.client.post('/signup/', {'username': 'newuser', 'password': 'newpass', 'role': 'Provider'})
        self.assertEqual(response.status_code, 200)

    def test_user_login(self):
        response = self.client.post('/login/', {'username': 'testuser', 'password': 'testpass'})
        self.assertEqual(response.status_code, 200)

    def test_user_logout(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.get('/logout/')
        self.assertEqual(response.status_code, 302)


class FundRequestTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.provider = User.objects.create_user(username='provider', password='testpass')
        self.provider_group = Group.objects.create(name='Loan_Provider')
        self.provider.groups.add(self.provider_group)

    def test_fund_request_creation(self):
        self.client.login(username='provider', password='testpass')
        response = self.client.post('/provider-fund-request/', {'total_budget': 5000})
        self.assertEqual(response.status_code, 302)  # Redirects after successful request
        self.assertEqual(Fund.objects.count(), 1)


class PermissionsTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.customer = User.objects.create_user(username='customer', password='testpass')
        self.provider = User.objects.create_user(username='provider', password='testpass')
        self.bank = User.objects.create_superuser(username='bank', password='testpass')
        self.client.login(username='customer', password='testpass')

    def test_provider_access_denied(self):
        response = self.client.get('/provider-account-details/')
        self.assertEqual(response.status_code, 403)  # Forbidden access

    def test_bank_access_loan_requests(self):
        self.client.login(username='bank', password='testpass')
        response = self.client.get('/bank-loan-requests/')
        self.assertEqual(response.status_code, 200)
