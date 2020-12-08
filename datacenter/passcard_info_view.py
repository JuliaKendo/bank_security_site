from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from django.utils.timezone import localtime


DURATION_OF_LONG_VISIT = 60
YESNO = {True: 'Да', None: 'Нет'}


def get_duration(visit):
    leaved_at = visit.leaved_at if visit.leaved_at else localtime()
    time_stay_in_vault = leaved_at - localtime(visit.entered_at)
    return time_stay_in_vault.total_seconds()


def format_duration(visit_duration_seconds):
    hours = int(visit_duration_seconds // 3600)
    minutes = int((visit_duration_seconds % 3600) // 60)
    seconds = int(visit_duration_seconds - ((hours * 3600) + (minutes * 60)))
    return f'{hours}:{minutes}:{seconds}'


def is_visit_long(visit, duration_of_long_visit):
    visit_duration_seconds = get_duration(visit)
    if int(visit_duration_seconds // 60) >= duration_of_long_visit:
        return True


def passcard_info_view(request, passcode):
    passcard = Passcard.objects.get(passcode=passcode)
    visits_in_bank_vault = Visit.objects.filter(passcard=passcard)

    this_passcard_visits = [
        {
            "entered_at": localtime(visit.entered_at),
            "duration": format_duration(get_duration(visit)),
            "is_strange": YESNO[is_visit_long(visit, DURATION_OF_LONG_VISIT)],
        } for visit in visits_in_bank_vault
    ]
    context = {
        "passcard": passcard,
        "this_passcard_visits": this_passcard_visits
    }
    return render(request, 'passcard_info.html', context)
