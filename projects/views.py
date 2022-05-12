from rest_framework.viewsets import ModelViewSet
from rest_framework import status
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticated

from projects.models import (Project,
                             Contributor,
                             Issue,
                             Comment)

from projects.serializers import (ContributorSerializer,
                                  IssueSerializer,
                                  CommentSerializer, get_project_serializer)

from projects.permissions import (IsProjectAuthor,
                                  IsContributorsAdmin,
                                  IsProjectContributor)


class ProjectViewSet(ModelViewSet):

    permission_classes = [IsAuthenticated, IsProjectAuthor]

    def get_serializer_class(self):
        return get_project_serializer(self.request.user)

    def get_queryset(self):
        """Retourne la liste de tous les projets liés à l'utilisateur connecté."""
        return Project.objects.filter(contributors__user_id=self.request.user)

    def perform_create(self, serializer):
        """Permet d'ajouter l'auteur du projet a la liste des contributeurs."""
        serializer.save(author_user=self.request.user)


class ContributorViewset(ModelViewSet):

    serializer_class = ContributorSerializer
    permission_classes = [IsAuthenticated, IsContributorsAdmin]

    def get_queryset(self):
        """Retourne tous les contributeurs du projet."""
        return Contributor.objects.filter(project=self.kwargs['project_pk'])

    def create(self, request, project_pk=None):
        """Permet d'ajouter un utilisateur à la liste des contributeurs d'un projet."""
        data = request.data.copy()
        contributors_list = []

        for object in Contributor.objects.filter(project_id=project_pk):
            contributors_list.append(object.user_id)

        # Vérifie si l'utilisateur connecté n'est pas déjà dans la liste des contributeurs.
        if int(data['user']) in contributors_list:
            return Response(
                {"L'utilisateur est déjà dans la liste des contributeurs du projet."},
                status=status.HTTP_400_BAD_REQUEST
            )
        else:
            # Ajout de l'utilisateur en tant que contributeur du projet.
            data['project'] = project_pk
            data['role'] = 'CONTRIBUTOR'
            serializer = ContributorSerializer(data=data)
            serializer.is_valid(raise_exception=True)
            serializer.save()

            return Response(
                {"L'utilisateur a bien été ajouté à la liste des contributeurs du projet."},
                status=status.HTTP_201_CREATED
            )


class IssueViewSet(ModelViewSet):

    serializer_class = IssueSerializer
    permission_classes = [IsAuthenticated, IsProjectContributor]

    def get_queryset(self):
        """Retourne tous les problèmes du projet."""
        return Issue.objects.filter(project=self.kwargs['project_pk'])

    def perform_create(self, serializer):
        """Permet de créer un problème dans un projet."""
        serializer.save(author_user=self.request.user, project=Project.objects.get(id=self.kwargs['project_pk']))


class CommentViewSet(ModelViewSet):

    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated, IsProjectContributor]

    def get_queryset(self):
        """Retourne tous les commentaires liés à un problème."""
        return Comment.objects.filter(issue=self.kwargs['issue_pk'])

    def perform_create(self, serializer):
        """Permet de créer un commentaire sur un problème."""
        serializer.save(author_user=self.request.user, issue=Issue.objects.get(id=self.kwargs['issue_pk']))
