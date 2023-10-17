from django.shortcuts import render
from portfolio.models import ProjectPortfolio


# Create your views here.
def index(request):
    projects = ProjectPortfolio.objects.all()
    context = {"projects": projects}
    return render(request, "portfolio/index.html", context=context)
