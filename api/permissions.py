from rest_framework import permissions

class IsAdminOnly(permissions.BasePermission):
    """
    Faqat admin foydalanuvchilarga API'ga kirishga ruxsat berish
    """
    def has_permission(self, request, view):
        return request.user and request.user.is_staff
