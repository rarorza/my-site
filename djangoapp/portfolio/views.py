from django.shortcuts import render
from portfolio.models import Category, ProjectPortfolio


# Create your views here.
def index(request):
    projects = ProjectPortfolio.objects.all()
    categories = Category.objects.all()
    context = {"projects": projects, "categories": categories}
    return render(request, "portfolio/index.html", context=context)


def category(request, slug):
    categories = ProjectPortfolio.objects.filter(category__name=slug)
    context = {"categories": categories}
    return render(request, "portfolio/index.html", context=context)
