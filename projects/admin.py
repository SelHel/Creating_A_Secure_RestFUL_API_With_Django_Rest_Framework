from django.contrib import admin
from .models import Comment, Contributor, Issue, Project


admin.site.register(Comment)
admin.site.register(Contributor)
admin.site.register(Issue)
admin.site.register(Project)
