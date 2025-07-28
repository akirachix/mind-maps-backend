from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsFarmer(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and getattr(request.user, 'user_type', None) == 'Farmer'

class IsExtentionWorker(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and getattr(request.user, 'user_type', None) == 'Extentionworker'

class IsAdminOrSelf(BasePermission):
    def has_permission(self, request, view):
        if getattr(view, "action", None) == "list":
            return request.user.is_authenticated and request.user.is_staff
        return request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        return request.user.is_staff or obj == request.user
    
class TrainingsPermission(BasePermission):
    def has_permission(self, request, view):
        user = request.user
        if not user.is_authenticated:
            return False
        if user.is_staff:
            return True
        if getattr(user, 'user_type', None) in ['Extentionworker', 'Farmer']:
            return request.method in SAFE_METHODS
        return False

    def has_object_permission(self, request, view, obj):
        user = request.user
        if user.is_staff:
            return True
        if getattr(user, 'user_type', None) in ['Extentionworker', 'Farmer']:
            return request.method in SAFE_METHODS
        return    
    
class RewardsPermission(BasePermission):
    def has_permission(self, request, view):
        user = request.user
        if not user.is_authenticated:
            return False
        if user.is_staff:
            return True
        if getattr(user, 'user_type', None) == 'Extentionworker':
            return True
        if getattr(user, 'user_type', None) == 'Farmer':
            return request.method in SAFE_METHODS
        return False

    def has_object_permission(self, request, view, obj):
        user = request.user
        if user.is_staff:
            return True
        if getattr(user, 'user_type', None) == 'Extentionworker':
            return True
        if getattr(user, 'user_type', None) == 'Farmer':
            return request.method in SAFE_METHODS and getattr(obj, 'farmer_id', None) == user.id
        return  

class PaymentPermission(BasePermission):
    def has_permission(self, request, view):
        user = request.user
        if not user.is_authenticated:
            return False
        if user.is_staff:
            return True
        if getattr(user, 'user_type', None) == 'Farmer':
            return request.method in SAFE_METHODS + ('POST',)
        return False

    def has_object_permission(self, request, view, obj):
        user = request.user
        if user.is_staff:
            return True
        if getattr(user, 'user_type', None) == 'Farmer':
            return getattr(obj, 'farmer_id', None) == user.id and request.method in SAFE_METHODS
        return False

class RefundPermission(BasePermission):
    def has_permission(self, request, view):
        user = request.user
        if not user.is_authenticated:
            return False
        if user.is_staff:
            return True  
        if getattr(user, 'user_type', None) == 'Farmer':
            return request.method in SAFE_METHODS + ('POST', 'DELETE')
        return False

    def has_object_permission(self, request, view, obj):
        user = request.user
        if user.is_staff:
            return True 
        if getattr(user, 'user_type', None) == 'Farmer':
            return getattr(obj, 'farmer_id', None) == user.id and request.method in SAFE_METHODS + ('DELETE',)
        return False

class AttendancePermission(BasePermission):
    def has_permission(self, request, view):
        user = request.user
        if not user.is_authenticated:
            return False
        if user.is_staff:
            return True
        if getattr(user, 'user_type', None) == 'Extentionworker':
            return True
        if getattr(user, 'user_type', None) == 'Farmer':
            return request.method in SAFE_METHODS
        return False

    def has_object_permission(self, request, view, obj):
        user = request.user
        if user.is_staff:
            return True
        if getattr(user, 'user_type', None) == 'Extentionworker':
            return True
        if getattr(user, 'user_type', None) == 'Farmer':
            return request.method in SAFE_METHODS and getattr(obj, 'farmer_id', None) == user.id
        return


class SchedulePermission(BasePermission):
    def has_permission(self, request, view):
        user = request.user
        if not user.is_authenticated:
            return False
       
        if user.is_staff:
            return True
       
        if getattr(user, 'user_type', None) in ['Extentionworker', 'Farmer']:
            return request.method in SAFE_METHODS
        return False

    def has_object_permission(self, request, view, obj):
        user = request.user
        if user.is_staff:
            return True
        if getattr(user, 'user_type', None) in ['Extentionworker', 'Farmer']:
            return request.method in SAFE_METHODS
        return False
    
class VillagePermission(BasePermission):
    def has_permission(self, request, view):
        user = request.user
        if not user.is_authenticated:
            return False
        if user.is_staff:
            return True
        if getattr(user, 'user_type', None) == 'Extentionworker':
            return request.method in SAFE_METHODS
        if getattr(user, 'user_type', None) == 'Farmer':
            return request.method in SAFE_METHODS + ('PUT', 'PATCH')
        return False

    def has_object_permission(self, request, view, obj):
        user = request.user
        if user.is_staff:
            return True
        if getattr(user, 'user_type', None) == 'Extentionworker':
            return request.method in SAFE_METHODS
        if getattr(user, 'user_type', None) == 'Farmer':
            return request.method in SAFE_METHODS + ('PUT', 'PATCH')    