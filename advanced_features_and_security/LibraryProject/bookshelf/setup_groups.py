from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from .models import Book

class Command(BaseCommand):
    help = 'Setup default groups and permissions'

    def handle(self, *args, **kwargs):
        content_type = ContentType.objects.get_for_model(Book)

        perms = {
            'Editors': ['can_edit', 'can_create'],
            'Viewers': ['can_view'],
            'Admins': ['can_view', 'can_create', 'can_edit', 'can_delete'],
        }

        for group_name, perm_codes in perms.items():
            group, created = Group.objects.get_or_create(name=group_name)
            for code in perm_codes:
                permission = Permission.objects.get(codename=code, content_type=content_type)
                group.permissions.add(permission)

        self.stdout.write(self.style.SUCCESS('Groups and permissions created.'))
