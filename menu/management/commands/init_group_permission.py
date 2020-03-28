"""
    file: menu/.../commands/init_group_permission.py
    purpose: Define the command to init group and permission for the authorization of Menu app
"""

from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import Group, Permission

from menu.constants import GROUP_PERMISSION_MAPPING
from menu.utils import add_perrmission_to_group


class Command(BaseCommand):
    """ Init groupd and permission command """

    def handle(self, *args, **options):
        for group in GROUP_PERMISSION_MAPPING:
            # Add this group into db
            group_obj, created = Group.objects.get_or_create(name=group)
            if not created:
                self.stdout.write(self.style.SUCCESS('Group "%s" is created' % group))

            # File the permissions that be not added
            not_added_permissions = [
                x for x in GROUP_PERMISSION_MAPPING[group]
                if x not in group_obj.permissions.values_list('codename', flat=True)
            ]

            # Add those permission into group
            for permission_code_name in not_added_permissions:
                add_perrmission_to_group(permission_code_name, group_obj)

        self.stdout.write(self.style.SUCCESS('Completed'))
