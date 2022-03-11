from datetime import datetime
from dateutil.relativedelta import relativedelta

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from tasks.models import Task


class CountTaskReport(APIView):
    """
    Формируем статистики по месяцам
    """

    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):

        start = request.query_params['start'].rsplit('-', 1)[0]
        end = request.query_params['end'].rsplit('-', 1)[0]

        start_date = datetime.strptime(start, "%Y-%m")
        end_date = datetime.strptime(end, "%Y-%m")

        labels = []

        count_all_tasks = []
        count_executed_tasks = []
        count_expired_tasks = []

        while start_date <= end_date:

            date_str = start_date.strftime("%Y-%m")
            labels.append(date_str)

            count_all_tasks.append(Task.objects.filter(createDate__gte=start_date).filter(
                createDate__lte=start_date + relativedelta(months=1)).count())

            count_executed_tasks.append(Task.objects.filter(createDate__gte=start_date).
                                        filter(createDate__lte=start_date+relativedelta(months=1)).
                                        filter(is_done=True).count())

            count_expired_tasks.append(Task.objects.filter(createDate__gte=start_date).
                                       filter(createDate__lte=start_date + relativedelta(months=1)).
                                       filter(expired=True).filter(is_done=False).count())

            start_date += relativedelta(months=1)

        date_list = {
            'labels': labels,
            'datasets': {
                'count_all_tasks': count_all_tasks,
                'count_executed_tasks': count_executed_tasks,
                'count_expired_tasks': count_expired_tasks,
            }
        }

        return Response(date_list)
