from django.db import models
from utils.random_slug import slugify_new
from utils.resize_image import resize_image


class ProjectPortfolio(models.Model):
    class Meta:
        verbose_name = "ProjectPortfolio"
        verbose_name_plural = "ProjectsPortfolio"

    name = models.CharField(max_length=255)
    slug = models.SlugField(
        unique=True,
        default=None,
        null=True,
        blank=True,
        max_length=255,
    )
    description = models.TextField()
    cover = models.ImageField(
        upload_to="projects/%Y/%m",
        blank=True,
        default="",
    )
    repository_link = models.CharField(max_length=2048)
    deploy_link = models.CharField(max_length=2048)
    is_published = models.BooleanField(default=False)

    def save(self, *args, **kwargs) -> None:
        if not self.slug:
            self.slug = slugify_new(self.name)

        cover_name_before_save = str(self.cover.name)
        super_save = super().save(*args, **kwargs)
        cover_changed = False
        if self.cover:
            if cover_name_before_save != self.cover.name:
                cover_changed = True

        if cover_changed:
            resize_image(
                image=self.cover,
                new_width=900,
                optimize=True,
                quality=70,
            )

        return super_save

    def __str__(self) -> str:
        return self.name
