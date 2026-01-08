from django.shortcuts import render
from .models import Content


def show(request):
    elements = Content.objects.all().order_by("-created_at")
    context = {
        "elements": elements,
    }
    return render(request, "core/index.html", context)

def sorted_up(request):
    elements = Content.objects.all().order_by("rating")
    context = {
        "elements": elements,
    }
    return render(request, "core/index.html", context)

def sorted_down(request):
    elements = Content.objects.all().order_by("-rating")
    context = {
        "elements": elements,
    }
    return render(request, "core/index.html", context)

