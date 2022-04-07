from rest_framework.permissions import BasePermission


class IsProjectAuthor(BasePermission):
    pass


class IsProjectContributor(BasePermission):
    pass
