from django.shortcuts import render

from django.http import JsonResponse
from .models import Activities, HrStreamData

# externally imported modules
# decorators for annotations ->
from rest_framework.decorators import api_view
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

import logging

logger = logging.getLogger(__name__)


@swagger_auto_schema(method='get', operation_summary='get all activities',
                     responses={
                         200: openapi.Response(
                             'Successful response',
                             openapi.Schema(
                                 type=openapi.TYPE_OBJECT,
                                 properties={
                                     'date': openapi.Schema(type=openapi.TYPE_ARRAY,
                                                            items=openapi.Schema(type=openapi.TYPE_STRING))},
                             )
                         ),
                         404: openapi.Response('No activities found .'),
                         500: openapi.Response('Internal server error.'),
                     }
                     )
@api_view(['GET'])
def get_all_activities(request):
    try:
        all_activities = Activities.objects.all()

        logger.info('Retrieved all activities successfully.')

        return JsonResponse({'data': list(all_activities.values())}, safe=False, json_dumps_params={'indent': 2})

    except Exception as e:

        logger.error(f'Error retrieving all activities: {e}')

        return JsonResponse({'error': 'An error occurred while retrieving activities.'}, status=500)


@swagger_auto_schema(
    method='get',
    operation_summary='Get all activities by activity name',
    manual_parameters=[
        openapi.Parameter(
            'activity_name', in_=openapi.IN_QUERY, type=openapi.TYPE_STRING,
            description='Name of the activity for filtering.'
        ),
    ],
    responses={
        200: openapi.Response(
            'Successful response',
            openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties={
                    'date': openapi.Schema(type=openapi.TYPE_ARRAY, items=openapi.Schema(type=openapi.TYPE_STRING))},
            )
        ),
        404: openapi.Response('No activities found with the specified name.'),
        500: openapi.Response('Internal server error.'),
    }
)
@api_view(['GET'])
def get_activities_by_activity_name(request):
    try:
        activity_name = request.GET.get('activity_name', '')

        if activity_name:
            activities_by_name = Activities.objects.filter(activity_name__icontains=activity_name)

            if not activities_by_name.exists():
                return JsonResponse({'message': f'No activities found with name "{activity_name}".'}, status=404)

            logger.info("Retrieved activities successfully")
            return JsonResponse({'data': list(activities_by_name.values())}, safe=False,
                                json_dumps_params={'indent': 2})

    except Exception as e:
        logger.error(f'Error retrieving activities: {e}')
        return JsonResponse({'error': 'An error occurred while retrieving activities.'}, status=500)


@swagger_auto_schema(
    method='get',
    operation_summary='Get all activities by activity date',
    manual_parameters=[
        openapi.Parameter(
            'activity_date', in_=openapi.IN_QUERY, type=openapi.TYPE_STRING,
            description='Date of the activity for filtering (YYYY-MM-DD).'
        ),
    ],
    responses={
        200: openapi.Response(
            'Successful response',
            openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties={
                    'date': openapi.Schema(type=openapi.TYPE_ARRAY, items=openapi.Schema(type=openapi.TYPE_STRING)),
                },
            )
        ),
        404: openapi.Response("No activities found for the given date."),
        500: openapi.Response("Internal server error."),
    }
)
@api_view(['GET'])
def get_activities_by_date(request):
    try:
        activity_date = request.GET.get('activity_date', '')

        if activity_date:
            activities_by_date = Activities.objects.filter(date_time__date=activity_date)

            if not activities_by_date.exists():
                return JsonResponse({'error': 'No activities found for the given date.'}, status=404)

            logger.info(f"Retrieved activities for date: {activity_date}")
            return JsonResponse({'data': list(activities_by_date.values())}, safe=False,
                                json_dumps_params={'indent': 2})

    except Exception as e:
        logger.error(f'Error retrieving activities: {e}')
        return JsonResponse({'error': 'An error occurred while retrieving activities.'}, status=500)


@swagger_auto_schema(
    method='get',
    operation_summary='Get activity hr data by activity id',
    manual_parameters=[
        openapi.Parameter(
            'activity_id', in_=openapi.IN_QUERY, type=openapi.TYPE_NUMBER,
            description='activity id for filtering.'
        ),
    ],
    responses={
        200: openapi.Response(
            'Successful response',
            openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties={
                    'date': openapi.Schema(type=openapi.TYPE_ARRAY, items=openapi.Schema(type=openapi.TYPE_STRING))},
            )
        ),
        404: openapi.Response('No heartrate data found with the specified activity id.'),
        500: openapi.Response('Internal server error.'),
    }
)
@api_view(['GET'])
def get_hr_data(request):
    try:
        activity_id = request.GET.get('activity_id', '')

        if activity_id:
            activity_by_id = HrStreamData.objects.filter(activity_id=activity_id)

            if not activity_by_id.exists():
                return JsonResponse({'message': f'No heartrate data found for activity with id "{activity_id}".'},
                                    status=404)

            logger.info("Retrieved activity heart rate data successfully")
            return JsonResponse({'data': list(activity_by_id.values())}, safe=False,
                                json_dumps_params={'indent': 2})

    except Exception as e:
        logger.error(f'Error retrieving activities: {e}')
        return JsonResponse({'error': 'An error occurred while retrieving activity heartrate data.'}, status=500)
