from django.shortcuts import render

import logging
from django.http import JsonResponse
from .models import Activities

logger = logging.getLogger(__name__)


def get_all_activities(request):
    try:
        all_activities = Activities.objects.all()

        logger.info('Retrieved all activities successfully.')

        return JsonResponse({'data': list(all_activities.values())}, safe=False, json_dumps_params={'indent': 2})

    except Exception as e:

        logger.error(f'Error retrieving all activities: {e}')

        return JsonResponse({'error': 'An error occurred while retrieving activities.'}, status=500)
