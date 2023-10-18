from blog.models import Category, Page, Post, Tag
from django.contrib import admin
from django.utils.safestring import mark_safe
from django_summernote.admin import SummernoteModelAdmin


# Register your models here.
@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "slug")
    list_display_links = ("name",)
    search_fields = ("id", "name", "slug")
    list_per_page = 10
    ordering = ("-id",)
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "slug")
    list_display_links = ("name",)
    search_fields = ("id", "name", "slug")
    list_per_page = 10
    ordering = ("-id",)
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Page)
class PageAdmin(SummernoteModelAdmin):
    summernote_fields = ("content",)
    list_display = ("id", "title", "slug")
    list_display_links = ("title",)
    search_fields = ("id", "title", "slug")
    list_per_page = 10
    ordering = ("-id",)
    prepopulated_fields = {"slug": ("title",)}


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    summernote_fields = ("content",)
    list_display = ("id", "title", "is_published", "created_by")
    list_display_links = ("title",)
    search_fields = ("id", "title", "slug", "excerpt", "content")
    list_per_page = 50
    ordering = ("-id",)
    list_filter = ("category", "is_published")
    list_editable = ("is_published",)
    readonly_fields = (
        "created_at",
        "updated_at",
        "created_by",
        "updated_by",
        "post_link",
    )
    prepopulated_fields = {"slug": ("title",)}
    autocomplete_fields = ("tags", "category")

    def post_link(self, obj):
        if not obj.pk:
            return "-"

        url_post = obj.get_absolute_url()
        safe_url = mark_safe(
            f'<a target="_blank" href="{url_post}">Ver post: {obj.title}</a>'
        )  # noqa 501
        return safe_url

    def save_model(self, request, obj, form, change):
        if change:
            obj.updated_by = request.user
        else:
            obj.created_by = request.user
        obj.save()
        return super().save_model(request, obj, form, change)
