from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from django.utils.timezone import localtime


DURATION_OF_LONG_VISIT = 60
YESNO = {True: 'Да', None: 'Нет'}


def passcard_info_view(request, passcode):
    passcard = Passcard.objects.get(passcode=passcode)
    visits_in_bank_vault = Visit.objects.filter(passcard=passcard)

    this_passcard_visits = [
        {
            "entered_at": localtime(visit.entered_at),
            "duration": visit.format_duration(visit.get_duration(visit)),
            "is_strange": YESNO[visit.is_visit_long(visit, DURATION_OF_LONG_VISIT)],
        } for visit in visits_in_bank_vault
    ]
    context = {
        "passcard": passcard,
        "this_passcard_visits": this_passcard_visits
    }
    return render(request, 'passcard_info.html', context)
