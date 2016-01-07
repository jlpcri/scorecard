from itertools import groupby

from models import InnovationStats
from scorecard.apps.datas.utils import get_week_ending_date


def get_distinct_dates():
    result = []
    qis = InnovationStats.objects.order_by('created')
    for created_date, group in groupby(qis, key=extract_date):
        result.append(created_date)

    return result


def extract_date(qi):
    return get_week_ending_date(qi.created)
