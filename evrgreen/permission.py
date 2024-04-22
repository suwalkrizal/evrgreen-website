from rest_framework import permissions
class isCustomerProfileorReadOnly(permissions.BasePermission):
    def has_permission(self,request,view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user.is_authenticated and request.user.role=="customerprofile"

class isMerchantProfileReadOnly(permissions.BasePermission):
    def has_permission(self,request,view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user.is_authenticated and request.user.role=="merchantprofile"    



 
        