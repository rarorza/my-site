from django.contrib import messages
from django.shortcuts import redirect, render
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

    if request.method == "POST":
        form = ContactForm(data=request.POST)
        if form.is_valid():
            name = str(form.cleaned_data["name"]).strip()
            email = str(form.cleaned_data["email"]).strip()
            content = str(form.cleaned_data["content"]).strip()
            was_sent = send_email(name, email, content)

            if was_sent:
                messages.success(request, "Email successfully sent!")
                return redirect("portfolio:index-portfolio")
            else:
                messages.error(
                    request,
                    "Unable to send, please contact me via email:\
                    rarorza@proton.me",
                )
    else:
        form = ContactForm()

    context = {"projects": projects, "experiences": experiences, "form": form}
    return render(request, "portfolio/index.html", context=context)
