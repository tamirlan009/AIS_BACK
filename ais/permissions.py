from rest_framework.permissions import BasePermission


class UserHasAccess(BasePermission):
    """
    Проверка пользователья на доступ к данным
    """

    def has_object_permission(self, request, view, obj):
        return bool(
            obj.creator == request.user or
            obj.executor == request.user or
            request.user.is_superuser
        )


class UserCanCreate(BasePermission):
    """
    Проверка пользователья на доступ к данным
    """

    def has_permission(self, request, view):

        return bool(
            request.user.is_company_employee
        )


class UserCanAnswer(BasePermission):
    """
    Проверка пользователья на доступ к данным
    """

    def has_permission(self, request, view):

        return bool(
            request.user.is_superuser or
            request.user.is_contractor
        )


class UserCanView(BasePermission):
    """
    Проверка пользователья на доступ к данным
    """

    def has_permission(self, request, view):

        return bool(
            request.user.is_superuser or
            request.user.is_company_employee
        )

