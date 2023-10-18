from site_setup.models import SiteSetup


def site_setup(request):
    """
    Global context to access site_setup model in all pages
    """
    setup = SiteSetup.objects.order_by("-id").first()
    setup_context = {"site_setup": setup}
    return setup_context
