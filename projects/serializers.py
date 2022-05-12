from rest_framework.serializers import ModelSerializer
from rest_framework.serializers import SerializerMethodField
from projects.models import Project, Contributor, Issue, Comment


def get_project_serializer(user):
    class ProjectSerializer(ModelSerializer):
        """Conversion des données du modèle Project au format JSON."""
        user_role = SerializerMethodField('get_user_role')

        class Meta:
            model = Project
            exclude = ('author_user', )

        def get_user_role(self, project):
            user_role = Contributor.objects.get(project=project, user=user)
            return user_role.role
    return ProjectSerializer


class ContributorSerializer(ModelSerializer):
    """Conversion des données du modèle Contributor au format JSON."""

    class Meta:
        model = Contributor
        fields = ('id', 'user', 'project', 'role')


class IssueSerializer(ModelSerializer):
    """Conversion des données du modèle Issue au format JSON."""
    issue_author = SerializerMethodField('get_author_user')

    class Meta:
        model = Issue
        exclude = ('author_user', 'project')

    def get_author_user(self, issue):
        return issue.author_user.username


class CommentSerializer(ModelSerializer):
    """Conversion des données du modèle Comment au format JSON."""
    comment_author = SerializerMethodField('get_author_user')
    issue_title = SerializerMethodField('get_issue')

    class Meta:
        model = Comment
        exclude = ('author_user', 'issue')

    def get_author_user(self, comment):
        return comment.author_user.username

    def get_issue(self, comment):
        return comment.issue.title
