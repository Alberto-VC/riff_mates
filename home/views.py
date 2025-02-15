from django.http import HttpResponse, JsonResponse


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
