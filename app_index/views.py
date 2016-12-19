from django.shortcuts import render
from .models import *

# Create your views here.

def index(request):

    spendigns = EverydaySpendingING.objects.all()

    context = {
        "spendings": spendigns,
    }

    return render(request, "index.html", context)
