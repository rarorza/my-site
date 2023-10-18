from django.contrib import admin
from portfolio.models import Category, ProjectPortfolio


# Register your models here.
@admin.register(ProjectPortfolio)
class ProjectPortfolioAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "is_published")
    list_display_links = ("name",)
    list_editable = ("is_published",)
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    list_display_links = ("name",)
    prepopulated_fields = {"slug": ("name",)}
