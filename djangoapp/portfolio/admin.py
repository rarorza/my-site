from django.contrib import admin
from portfolio.models import ProjectPortfolio


# Register your models here.
@admin.register(ProjectPortfolio)
class ProjectPortfolioAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "slug")
