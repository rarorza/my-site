from django.contrib import admin
from django.http.request import HttpRequest
from site_setup.models import MenuLink, SiteSetup


class MenuLinkInLine(admin.TabularInline):
    model = MenuLink
    extra = 1


@admin.register(SiteSetup)
class SiteSetupAdmin(admin.ModelAdmin):
    list_display = "title", "description"
    inlines = (MenuLinkInLine,)

    def has_add_permission(self, request: HttpRequest) -> bool:
        return not SiteSetup.objects.exists()
