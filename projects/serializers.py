from rest_framework.serializers import ModelSerializer
from projects.models import Project, Contributor, Issue, Comment


class ProjectSerializer(ModelSerializer):

    class Meta:
        model = Project
        fields = ['id', 'title', 'description', 'type', 'author_user']


class ContributorsSerializer(ModelSerializer):

    class Meta:
        model = Contributor
        fields = ['id', 'user', 'project', 'role']


class IssueSerializer(ModelSerializer):

    class Meta:
        model = Issue
        fields = ['id', 'title', 'description', 'tag', 'priority', 'project',
                  'status', 'author_user', 'assignee_user', 'created_time']


class CommentSerializer(ModelSerializer):

    class Meta:
        model = Comment
        fields = ['id', 'description', 'author_user', 'issue',
                  'created_time']
