from datacenter.models import Visit
from django.shortcuts import render
from django.utils.timezone import localtime


def storage_information_view(request):

    visits_in_bank_vault = Visit.objects.filter(leaved_at__isnull=True)
    non_closed_visits = [
        {
            "who_entered": visit.passcard.owner_name,
            "entered_at": localtime(visit.entered_at),
            "duration": visit.format_duration(visit.get_duration(visit)),
        } for visit in visits_in_bank_vault
    ]

    context = {
        "non_closed_visits": non_closed_visits,
    }
    return render(request, 'storage_information.html', context)
