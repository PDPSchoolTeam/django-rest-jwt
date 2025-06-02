from django.urls import path
from api.views import Home

urlpatterns = [
    path("", Home.as_view())
]
