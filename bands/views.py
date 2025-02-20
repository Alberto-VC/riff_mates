from django.shortcuts import render, get_object_or_404

from bands.models import Musician

# Create your views here.


def musician_detail(request, musician_id):
    musician = get_object_or_404(Musician, id=musician_id)
    data = {
        "musician": musician,
    }
    return render(request, "musician.html", data)


def musicians(request, musician_id):
    data = {
        "musicians": Musician.objects.all().order_by("last_name"),
    }
    return render(request, "musician.html", data)
