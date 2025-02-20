from django.urls import path

from bands import views

urlpatterns = [
    path(
        "musician/<int:musician_id>/", views.musician_detail(), name="musician_detail"
    ),
    path("musicians/", views.musicians, name="musicians"),
]
