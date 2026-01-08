from django.urls  import path
from .views import show, sorted_up, sorted_down

urlpatterns = [
    path("", show, name="home"),
    path("sorted_up/", sorted_up),
    path("sorted_down/", sorted_down)
]

