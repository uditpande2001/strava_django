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


def get_activities_by_date(request):
    try:
        activities_by_date = Activities.objects.filter(date_time__date="2024-01-16")

        logger.info("Retrieved all activities successfully")
        return JsonResponse({'date': list(activities_by_date.values())}, safe=False, json_dumps_params={'indent': 2})

    except Exception as e:

        logger.error(f'Error retrieving all activities: {e}')

        return JsonResponse({'error': 'An error occurred while retrieving activities.'}, status=500)


def get_activities_by_activity_name(request):
    try:
        activities_by_date = Activities.objects.filter(activity_name__exact="Kartik ji home to my home")

        logger.info("Retrieved all activities successfully")
        return JsonResponse({'date': list(activities_by_date.values())}, safe=False, json_dumps_params={'indent': 2})

    except Exception as e:

        logger.error(f'Error retrieving all activities: {e}')

        return JsonResponse({'error': 'An error occurred while retrieving activities.'}, status=500)
