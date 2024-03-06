from rest_framework import serializers

from portfolio.models import Experience, ProjectPortfolio, Section, SectionContent

class ProjectPortfolioSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectPortfolio
        fields = (
            "id", "name", "description", "repository_link", "deploy_link", "category", "is_published",
        )

class ExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Experience
        fields = (
            "id", "start_time", "end_time", "title", "description", "is_published", "is_education", "is_current_experience",
        )

class SectionContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = SectionContent
        fields = ("content",)

class SectionSerializer(serializers.ModelSerializer):
    contents = SectionContentSerializer(read_only=True, many=True)
    class Meta:
        model = Section
        fields = (
            "id", "title", "description", "contents"
        )