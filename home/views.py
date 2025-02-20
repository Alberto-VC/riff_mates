from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from future.backports.datetime import datetime


# Create your views here.


def credits(request):
    content = "Nicky\nAlberto"

    return HttpResponse(content, content_type="text/plain")


def about(request):
    content = [
        "<!doctype html>",
        '<html lang="en">',
        "<head>",
        "  <title>RiffMates About</title>",
        "</head>",
        "<body>",
        "  <h1>RiffMates About</h1>",
        "  <p>",
        "    RiffMates is a for musicians seeking musicians. Find your next ",
        "    band or band-mate. Find your next gig.",
        "  </p>",
        "</body>",
        "</html>",
    ]

    content = "\n".join(content)
    return HttpResponse(content, content_type="text/html")


def version(request):
    data = {
        "version": "0.0.1",
    }

    return JsonResponse(data)


def news(request):
    data = {
        "news": [
            "RiffMates now has a news page!",
            "RiffMates has its first web page!",
        ]
    }

    return render(request, "news2.html", data)

def news_advanced(request):
    news_items = [
        (datetime(2020, 1, 1), "RiffMates now has a news page!"),
        (datetime(2020, 1, 2), "RiffMates has its first web page!"),
        (datetime(2020, 1, 3), "RiffMates has a new logo!"),
    ]

    return render(request, "news_advanced.html", {"news_items": news_items})