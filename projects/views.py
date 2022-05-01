from django.db import IntegrityError
from rest_framework.exceptions import NotAcceptable
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from projects.models import Project, Contributor, Issue, Comment
from projects.permissions import (IsAuthorOrReadOnly,
                                  IsProjectAuthor,
                                  IsProjectContributor)
from projects.serializers import (ProjectSerializer,
                                  ContributorSerializer,
                                  IssueSerializer,
                                  CommentSerializer)


class ProjectViewSet(ModelViewSet):

    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        contributor = Contributor.objects.filter(user=self.request.user)
        projects_user = [c.project.id for c in contributor]
        return Project.objects.filter(id__in=projects_user)

    def perform_create(self, serializer):
        if self.request.user.is_authenticated:
            instance = serializer.save(author_user=self.request.user)
            Contributor.objects.create(user=self.request.user, project=instance, role='AUTHOR')


class ContributorViewset(ModelViewSet):

    serializer_class = ContributorSerializer
    permission_classes = [IsAuthenticated, IsProjectAuthor]

    def get_queryset(self):
        return Contributor.objects.filter(project=self.kwargs['project_pk'])

    def perform_create(self, serializer):
        try:
            if self.request.user.is_authenticated:
                project = Project.objects.get(id=self.kwargs["project_pk"])
                return serializer.save(project=project)
        except IntegrityError:
            raise NotAcceptable("Un seul auteur possible par projet.")


class IssueViewSet(ModelViewSet):

    serializer_class = IssueSerializer
    permission_classes = [IsAuthenticated, IsProjectContributor]

    def get_queryset(self):
        return Issue.objects.all()


class CommentViewSet(ModelViewSet):

    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated, IsProjectContributor]

    def get_queryset(self):
        return Comment.objects.all()
