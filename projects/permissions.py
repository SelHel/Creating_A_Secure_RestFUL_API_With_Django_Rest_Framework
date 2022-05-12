from rest_framework.permissions import BasePermission, SAFE_METHODS

from projects.models import Project


class IsProjectAuthor(BasePermission):
    """Autorise uniquement les auteurs d'un projet à le modifier."""

    def has_permission(self, request, view):
        return True

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return obj.author_user == request.user


class IsContributorsAdmin(BasePermission):
    """
    Autorise uniquement l'auteur d'un projet à y ajouter ou
    supprimer des contributeurs.
    """

    def has_permission(self, request, view):
        project = Project.objects.get(id=view.kwargs['project_pk'])
        ctr_projects = Project.objects.filter(contributors__user=request.user)
        if project in ctr_projects:
            project = Project.objects.get(id=view.kwargs['project_pk'])
            if request.method in SAFE_METHODS:
                return True
            return project.author_user == request.user
        return False

    def has_object_permission(self, request, view, obj):
        project = Project.objects.get(id=view.kwargs['project_pk'])
        if request.method in SAFE_METHODS:
            return True
        return project.author_user == request.user


class IsProjectContributor(BasePermission):
    """
    Autorise uniquement les contributeurs d'un projet a accéder à ses problèmes et ses commentaires.
    """

    def has_permission(self, request, view):
        project = Project.objects.get(id=view.kwargs['project_pk'])
        ctr_projects = Project.objects.filter(contributors__user=request.user)
        if project in ctr_projects:
            return True
        return False

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return obj.author_user == request.user
