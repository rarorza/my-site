from django.utils import translation
from site_setup.models import SiteSetup


def site_setup(request):
    """
    Global context to access site_setup model in all pages
    """
    html_language = translation.get_language()
    setup = SiteSetup.objects.order_by("-id").first()

    if setup:
        about_me = setup.about_me.split("*")
        about_me_pt = setup.about_me_pt.split("*")
    else:
        setup = list
        about_me = list
        about_me_pt = list

    setup_context = {
        "site_setup": setup,
        "html_language": html_language,
        "about_me": about_me,
        "about_me_pt": about_me_pt,
    }
    return setup_context
