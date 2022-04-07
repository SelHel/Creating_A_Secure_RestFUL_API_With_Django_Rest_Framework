from django.contrib import admin
from projects.models import Comment, Contributor, Issue, Project


admin.site.register(Comment)
admin.site.register(Contributor)
admin.site.register(Issue)
admin.site.register(Project)
