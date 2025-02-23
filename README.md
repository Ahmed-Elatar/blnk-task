# blnk-task

This project is a Django-based web application that facilitates loan and fund management between providers, customers, and banks. It includes user authentication, loan requests, fund requests, and status tracking for transactions. The system is secured with permission groups and integrates with Celery and Redis for background processing. The application is containerized using Docker for easy deployment.

## Table of Contents
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Functions and Classes](#functions-and-classes)
- [URLs Map](#urls-map)
- [Installation Notes](#installation-notes)

## Features
- User authentication system with roles: Provider, Customer, and Banker.
- Loan request and approval workflow.
- Fund request and approval system.
- Tracking of loan repayments and bank total funds.
- Role-based access control for secure operations.
- Uses PostgreSQL as the database.
- Dockerized for simplified deployment.
- REST API built using Django Rest Framework.

---

## Prerequisites
Ensure you have the following installed:
- [Python 3.8+](https://www.python.org/downloads)
- [Docker](https://www.docker.com/get-started/)
- [Docker Compose](https://docs.docker.com/compose/install/)

---

## Installation
1. Clone the repository:
    ```bash
    git clone https://github.com/Ahmed-Elatar/e-finance.git
    cd e-finance
    ```

2. Build Docker containers:
    ```bash
    sudo docker-compose build
    ```

3. Create a Django superuser:
    ```bash
    sudo docker-compose run web python manage.py createsuperuser
    ```

4. Start the Docker containers:
    ```bash
    sudo docker-compose up
    ```

---

## Usage
Once running, access the application at `http://0.0.0.0:8000/`.

### Admin Panel
Go to `http://0.0.0.0:8000/admin` to access the Django admin panel using the superuser credentials created during setup.

---

## Functions and Classes

### **Authentication Views**
1. **`user_signup(request)`**  
   Handles user registration and assigns the correct role.
   
2. **`user_login(request)`**  
   Authenticates users and redirects them to the main page.
   
3. **`user_logout(request)`**  
   Logs out the user and redirects to the login page.

### **Provider Views**
4. **`ProviderAccountDetails(APIView)`**  
   - `GET`: Returns the provider's account details and redirects if pending or rejected.

5. **`ProviderFundRequest(APIView)`**  
   - `GET`: Returns a form for requesting funds.
   - `POST`: Submits a fund request, marking it as pending.

### **Banker Views**
6. **`ChangeLoanDetails(APIView)`**  
   - `GET`: Retrieves the current minimum and maximum loan limits.
   - `PUT`: Updates loan limits.

7. **`FundRequests(APIView)`**  
   - `GET`: Retrieves all fund requests.
   - `PUT`: Approves or rejects a fund request and updates the bank's total money.

8. **`LoanRequests(APIView)`**  
   - `GET`: Retrieves all loan requests.
   - `PUT`: Approves or rejects a loan request and updates the bank's total money.

### **Customer Views**
9. **`CustomerLoanRequests(APIView)`**  
   - `GET`: Displays the loan request form.
   - `POST`: Submits a new loan request.

10. **`CustomerLoanDetails(APIView)`**  
   - `GET`: Returns the customer's loan details and repayment status.
   - `POST`: Processes a loan repayment and updates remaining balance.

---

## URLs Map

### Authentication Endpoints:
- `/login/` - User login page
- `/signup/` - User signup page
- `/logout/` - Logs out the user

### Provider Endpoints:
- `/pending/` - Pending page for providers
- `/provider-fund-request/` - Fund request form
- `/provider-account-details/` - Provider account details

### Banker Endpoints:
- `/bank-change-min-max/` - Modify loan min/max limits
- `/bank-fund-requests/` - List of fund requests
- `/bank-fund-request/<int:fund_id>/` - Specific fund request details
- `/bank-loan-request/<int:loan_id>/` - Specific loan request details
- `/bank-loan-requests/` - List of loan requests

### Customer Endpoints:
- `/customer-loan-request/` - Loan request form
- `/customer-loan-status/` - Loan status page

---

## Installation Notes
1. Edit `.env` file to configure PostgreSQL database credentials.
2. Update `docker-compose.yml` with matching database credentials.

This README provides an overview of the project, its installation, usage, and function descriptions for maintaining and expanding the system.

