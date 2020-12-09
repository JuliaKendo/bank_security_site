from datacenter.models import Visit
from django.shortcuts import render
from django.utils.timezone import localtime


def get_duration(visit):
    leaved_at = visit.leaved_at if visit.leaved_at else localtime()
    time_stay_in_vault = leaved_at - localtime(visit.entered_at)
    return time_stay_in_vault.total_seconds()


def format_duration(visit_duration_seconds):
    hours = int(visit_duration_seconds // 3600)
    minutes = int((visit_duration_seconds % 3600) // 60)
    seconds = int(visit_duration_seconds - ((hours * 3600) + (minutes * 60)))
    return f'{hours}:{minutes}:{seconds}'


def storage_information_view(request):

    visits_in_bank_vault = Visit.objects.filter(leaved_at__isnull=True)
    non_closed_visits = [
        {
            "who_entered": visit.passcard.owner_name,
            "entered_at": localtime(visit.entered_at),
            "duration": format_duration(get_duration(visit)),
        } for visit in visits_in_bank_vault
    ]

    context = {
        "non_closed_visits": non_closed_visits,
    }
    return render(request, 'storage_information.html', context)
