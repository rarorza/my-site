from django.db import models
from utils.random_slug import slugify_new
from utils.resize_image import resize_image


class Category(models.Model):
    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    name = models.CharField(max_length=255)
    name_pt = models.CharField(max_length=255)
    slug = models.SlugField(
        unique=True, default=None, null=True, blank=True, max_length=255
    )

    def save(self, *args, **kwargs) -> None:
        if not self.slug:
            self.slug = slugify_new(self.name)
        return super().save(*args, **kwargs)

    def __str__(self) -> str:
        return self.name


class ProjectPortfolio(models.Model):
    class Meta:
        verbose_name = "ProjectPortfolio"
        verbose_name_plural = "ProjectsPortfolio"

    name = models.CharField(max_length=255)
    name_pt = models.CharField(max_length=255)
    slug = models.SlugField(
        unique=True,
        default=None,
        null=True,
        blank=True,
        max_length=255,
    )
    description = models.TextField()
    description_pt = models.TextField()
    cover = models.ImageField(
        upload_to="projects/%Y/%m",
        blank=True,
        default="",
    )
    repository_link = models.CharField(max_length=2048, null=True, blank=True)
    deploy_link = models.CharField(max_length=2048, null=True, blank=True)
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True, blank=True, default=None
    )
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


class Experience(models.Model):
    class Meta:
        verbose_name = "Experience"
        verbose_name_plural = "Experiences"

    start_time = models.DateField(null=True, blank=True)
    end_time = models.DateField(null=True, blank=True)
    title = models.CharField(max_length=255)
    title_pt = models.CharField(max_length=255)
    description = models.TextField()
    description_pt = models.TextField()
    is_published = models.BooleanField(default=False)
    is_education = models.BooleanField(default=False)
    is_current_experience = models.BooleanField(
        default=False,
        null=True,
        blank=True,
    )

    def __str__(self) -> str:
        return self.title


class Contact(models.Model):
    class Meta:
        verbose_name = "Contact"
        verbose_name_plural = "Contacts"

    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    content = models.TextField()
