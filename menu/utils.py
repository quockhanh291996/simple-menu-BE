"""
    file: menu/utils.py
    purpose: Contains utilization function use for menu app
"""

import logging

from django.contrib.auth.models import Permission
from django.core.exceptions import ObjectDoesNotExist

logger = logging.getLogger(__name__)

def add_perrmission_to_group(permission_code_name, group):
    """ Function to add a permission into group """

    try:
        #Filter if permission is added
        permiss_obj = Permission.objects.get(codename=permission_code_name)
        group.permissions.add(permiss_obj)
        group.save()
        logger.info('Added permission %s into group %s', permission_code_name, group.name)
    except ObjectDoesNotExist:
        logger.error('Missing permission %s', permission_code_name)
