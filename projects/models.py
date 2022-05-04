from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

TYPE_CHOICES = [
    ('BACK_END', 'Back-end'),
    ('FRONT_END', 'Front-end'),
    ('IOS', 'iOS'),
    ('ANDROID', 'Android')
]

ROLE_CHOICES = [
    ('AUTHOR', 'Auteur'),
    ('CONTRIBUTOR', 'Contributeur'),
]

TAG_CHOICES = [
    ('BUG', 'Bug'),
    ('UPGRADE', 'Amélioration'),
    ('TASK', 'Tâche'),
]

PRIORITY_CHOICES = [
    ('LOW', 'Faible'),
    ('MEDIUM', 'Moyenne'),
    ('HIGH', 'Élevée'),
]

STATUS_CHOICES = [
    ('TO_DO', 'À faire'),
    ('IN_PROGRESS', 'En cours'),
    ('DONE', 'Terminé'),
]


class Project(models.Model):
    project_id = models.CharField(max_length=10, unique=True)
    title = models.CharField(max_length=120)
    description = models.TextField(null=True, blank=True)
    type = models.CharField(max_length=15, choices=TYPE_CHOICES)
    author_user = models.ForeignKey(to=User, on_delete=models.CASCADE)

    def __str__(self):
        return f"Project_id : {self.id} - {self.title} - Author : {self.author_user}"


@receiver(post_save, sender=Project)
def add_contributor(sender, instance, created, **kwargs):
    """Permet d'ajouter l'auteur du projet a la liste des contributeurs."""
    # Vérifie si l'utilisateur n'est pas déjà auteur du projet.
    if created:
        Contributor.objects.create(
            user=instance.author_user,
            project=instance,
            role='AUTHOR'
        )


class Contributor(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='contributor')
    project = models.ForeignKey(to=Project, on_delete=models.CASCADE, related_name='contributors')
    role = models.CharField(max_length=11, choices=ROLE_CHOICES, default='CONTRIBUTOR')

    class Meta:
        unique_together = ('user', 'project')
        constraints = [
            models.UniqueConstraint(
                fields=['project'], condition=models.Q(role='AUTHOR'), name='unique_author_per_project')
        ]

    def __str__(self):
        return f"Project id : {self.project.id} / Contributor : {self.id} - {self.role} - {self.user.username}"


class Issue(models.Model):
    title = models.CharField(max_length=128)
    description = models.TextField(null=True, blank=True)
    tag = models.CharField(max_length=15, choices=TAG_CHOICES)
    priority = models.CharField(max_length=15, choices=PRIORITY_CHOICES, default='LOW')
    project = models.ForeignKey(to=Project, on_delete=models.CASCADE)
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default='TO_DO')
    author_user = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='created_issues')
    assignee_user = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='assigned_issues')
    created_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Issue id : {self.id} / Issue Author : {self.author_user} / Project id : {self.project.id}"


class Comment(models.Model):
    description = models.TextField(null=True, blank=True)
    author_user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    issue = models.ForeignKey(to=Issue, on_delete=models.CASCADE)
    created_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment id : {self.id} / Comment Author : {self.author_user} / Issue id : {self.issue.id}"
