from django.contrib import messages
from django.db.models import F
from django.shortcuts import redirect, render
from django.utils import translation
from django.utils.translation import gettext_lazy as _
from portfolio.forms import ContactForm
from portfolio.models import Experience, ProjectPortfolio
from utils.email_sender import send_email


# Create your views here.
def index(request):
    projects = (
        ProjectPortfolio.objects.filter(
            is_published=True,
        )
        .all()
        .order_by("-pk")
    )
    experiences = (
        Experience.objects.filter(
            is_published=True,
        )
        .all()
        .order_by("-pk")
    )
    html_language = translation.get_language()

    if html_language == "pt-br":
        experiences_translate = experiences.values(
            "id",
            t_title=F("title_pt"),
            t_description=F("description_pt"),
        )
        projects_translate = projects.values(
            "id",
            t_name=F("name_pt"),
            t_description=F("description_pt"),
        )
    else:
        experiences_translate = experiences.values(
            "id",
            t_title=F("title"),
            t_description=F("description"),
        )
        projects_translate = projects.values(
            "id",
            t_name=F("name"),
            t_description=F("description"),
        )

    if request.method == "POST":
        form = ContactForm(data=request.POST)
        if form.is_valid():
            name = str(form.cleaned_data["name"]).strip()
            email = str(form.cleaned_data["email"]).strip()
            content = str(form.cleaned_data["content"]).strip()
            was_sent = send_email(name, email, content)

            if was_sent:
                messages.success(request, _("Email successfully sent!"))
                return redirect("portfolio:index-portfolio")
            else:
                messages.error(
                    request,
                    _("Unable to send, please contact me via email: rarorza@proton.me"),
                )
    else:
        form = ContactForm()

    context = {
        "projects_translate": projects_translate,
        "projects": projects,
        "experiences_translate": experiences_translate,
        "experiences": experiences,
        "form": form,
    }
    return render(request, "portfolio/index.html", context=context)
