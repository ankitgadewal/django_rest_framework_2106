from rest_framework import permissions

class IsTeacher(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user and request.user.groups.filter(name='Teachers'):
            return True
        return False

class IsStudent(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user and request.user.groups.filter(name='Students'):
            return True
        return False

class IsLibrarian(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user and request.user.groups.filter(name='Librarian'):
            return True
        return False

class ReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return False