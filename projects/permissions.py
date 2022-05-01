from rest_framework.permissions import BasePermission, SAFE_METHODS
from projects.models import Project


class IsAuthorOrReadOnly(BasePermission):
    """Autorise uniquement les auteurs d'un objet à le modifier."""

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return obj.author_user == request.user


class IsProjectAuthor(BasePermission):
    """Autorisation personnalisée pour l'auteur d'un projet."""

    message = "Accès refusé : Vous n'êtes pas l'auteur du projet."

    def has_permission(self, request, view):
        pass


class IsProjectContributor(BasePermission):
    """Autorisation personnalisée pour le contributeur d'un projet."""

    message = "Accès refusé : Vous n'êtes pas contributeur du projet."

    def has_permission(self, request, view):
        pass
