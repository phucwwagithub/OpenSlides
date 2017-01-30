# Generated by Django 1.10.5 on 2017-01-11 21:45
from __future__ import unicode_literals

import django.db.models.deletion
from django.db import migrations, models

import openslides.users.models
import openslides.utils.models


def create_openslides_groups(apps, schema_editor):
    """
    Creates the users.models.Group objects for each existing
    django.contrib.auth.models.Group object.
    """
    # We get the model from the versioned app registry;
    # if we directly import it, it will be the wrong version.
    DjangoGroup = apps.get_model('auth', 'Group')
    Group = apps.get_model('users', 'Group')
    for group in DjangoGroup.objects.all():
        Group.objects.create(group_ptr_id=group.pk, name=group.name)


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0008_alter_user_username_max_length'),
        ('users', '0002_user_misc_default_groups'),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[(
                'group_ptr',
                models.OneToOneField(
                    auto_created=True,
                    on_delete=django.db.models.deletion.CASCADE,
                    parent_link=True,
                    primary_key=True,
                    serialize=False,
                    to='auth.Group'))],
            options={
                'default_permissions': (),
            },
            bases=(openslides.utils.models.RESTModelMixin, 'auth.group'),
            managers=[
                ('objects', openslides.users.models.GroupManager()),
            ],
        ),
        migrations.RunPython(
            create_openslides_groups,
        ),
    ]
