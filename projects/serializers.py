from rest_framework.serializers import ModelSerializer
from rest_framework.serializers import SerializerMethodField
from projects.models import Project, Contributor, Issue, Comment


def get_project_serializer(user):
    class ProjectSerializer(ModelSerializer):
        """Conversion des données du modèle Project au format JSON."""
        user_role = SerializerMethodField('get_user_role')
        endpoint = SerializerMethodField('get_endpoint')

        class Meta:
            model = Project
            exclude = ('author_user', )

        def get_user_role(self, project):
            user_role = Contributor.objects.get(project=project, user=user)
            return user_role.role

        def get_endpoint(self, project):
            return f"/api/projects/{project.id}"
    return ProjectSerializer


class ContributorSerializer(ModelSerializer):
    """Conversion des données du modèle Contributor au format JSON."""
    project_title = SerializerMethodField("get_project")
    username = SerializerMethodField("get_username")
    user_role = SerializerMethodField("get_user_role")

    class Meta:
        model = Contributor
        fields = ('id', 'user', 'user_role', 'project_title', 'username')

    def get_project(self, contributor):
        return contributor.project.title

    def get_username(self, contributor):
        return contributor.user.username

    def get_user_role(self, contributor):
        return contributor.role


class IssueSerializer(ModelSerializer):
    """Conversion des données du modèle Issue au format JSON."""
    issue_author = SerializerMethodField('get_author_user')
    assignee_user_name = SerializerMethodField('get_assignee_user_name')

    class Meta:
        model = Issue
        exclude = ('author_user', 'project')

    def get_author_user(self, issue):
        return issue.author_user.username

    def get_assignee_user_name(self, issue):
        return issue.assignee_user.username


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
