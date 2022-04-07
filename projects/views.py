from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from projects.models import Project, Contributor, Issue, Comment
from projects.serializers import (
    ProjectSerializer,
    ContributorsSerializer,
    IssueSerializer,
    CommentSerializer)


class ProjectViewSet(ModelViewSet):

    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Project.objects.all()


class ContributorsViewset(ModelViewSet):

    serializer_class = ContributorsSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Contributor.objects.all()


class IssueViewSet(ModelViewSet):

    serializer_class = IssueSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Issue.objects.all()


class CommentViewSet(ModelViewSet):

    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Comment.objects.all()
