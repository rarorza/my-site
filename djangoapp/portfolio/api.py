from django.http import JsonResponse
from rest_framework.decorators import (
    api_view,
    authentication_classes,
    permission_classes,
)

from portfolio.models import Experience, ProjectPortfolio, Section
from portfolio.serializers import ProjectPortfolioSerializer, ExperienceSerializer, SectionSerializer

@api_view(["GET"])
@authentication_classes([])
@permission_classes([])
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
    sections = Section.objects.all().order_by("-pk")

    experiences_serializer = ExperienceSerializer(experiences, many=True)
    projects_serializer = ProjectPortfolioSerializer(projects, many=True)
    sections_serializer = SectionSerializer(sections, many=True)
    

    context = {"projects": projects_serializer.data, "experiences": experiences_serializer.data, "sections": sections_serializer.data}
    return JsonResponse(context)