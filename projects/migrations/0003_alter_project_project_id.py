# Generated by Django 4.0.3 on 2022-04-10 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_project_project_id_alter_contributor_project_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='project_id',
            field=models.CharField(max_length=10, unique=True),
        ),
    ]
