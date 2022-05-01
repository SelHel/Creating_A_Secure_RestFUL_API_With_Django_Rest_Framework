from rest_framework.serializers import ModelSerializer
from projects.models import Project, Contributor, Issue, Comment


class ProjectSerializer(ModelSerializer):

    class Meta:
        model = Project
        exclude = ('author_user', )


class ContributorSerializer(ModelSerializer):

    class Meta:
        model = Contributor
        fields = ('id', 'role', 'user')


class IssueSerializer(ModelSerializer):

    class Meta:
        model = Issue
        fields = "__all__"


class CommentSerializer(ModelSerializer):

    class Meta:
        model = Comment
        fields = "__all__"
