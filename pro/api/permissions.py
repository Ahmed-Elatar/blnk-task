from rest_framework import permissions

class ProviderGroupPermission(permissions.BasePermission):
    """
    Custom permission to allow access only to users in a specific group.
    """

    def has_permission(self, request, view):
        # Check if user is authenticated
        
        if not request.user or not request.user.is_authenticated:
            return False  
        

        # Retrieve allowed group name from the view
        if request.user.groups.filter(name='Loan_Provider').exists() :
            return True
        else:
            return False
        

class BankGroupPermission(permissions.BasePermission):
    """
    Custom permission to allow access only to users in a specific group.
    """

    def has_permission(self, request, view):
        # Check if user is authenticated
        
        if not request.user or not request.user.is_authenticated:
            return False  
        

        # Retrieve allowed group name from the view
        if request.user.groups.filter(name='Bank_personal').exists() :
            return True
        else:
            return False
        

class CustomerGroupPermission(permissions.BasePermission):
    """
    Custom permission to allow access only to users in a specific group.
    """

    def has_permission(self, request, view):
        # Check if user is authenticated
        
        if not request.user or not request.user.is_authenticated:
            return False  
        

        # Retrieve allowed group name from the view
        if request.user.groups.filter(name='Loan_Customer').exists() :
            return True
        else:
            return False