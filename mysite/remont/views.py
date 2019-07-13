from django.shortcuts import render
from .forms import VisitorsForm

def index(request):
    form = VisitorsForm(request.POST or None)

    return render(request, 'remont/homePage.html', {'form': form})