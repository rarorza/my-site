from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django_summernote.models import AbstractAttachment
from utils.random_slug import slugify_new
from utils.resize_image import resize_image


class Tag(models.Model):
    class Meta:
        verbose_name = "Tag"
        verbose_name_plural = "Tags"

    name = models.CharField(max_length=255)
    slug = models.SlugField(
        unique=True,
        default=None,
        null=True,
        blank=True,
        max_length=255,
    )

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify_new(self.name)
        return super().save(*args, **kwargs)

    def __str__(self) -> str:
        return self.name


class Category(models.Model):
    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    name = models.CharField(max_length=255)
    slug = models.SlugField(
        unique=True, default=None, null=True, blank=True, max_length=255
    )

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify_new(self.name)
        return super().save(*args, **kwargs)

    def __str__(self) -> str:
        return self.name


class Page(models.Model):
    class Meta:
        verbose_name = "Page"
        verbose_name_plural = "Pages"

    title = models.CharField(max_length=65)
    slug = models.SlugField(
        unique=True, default=None, null=True, blank=True, max_length=255
    )
    is_published = models.BooleanField(
        default=False,
        help_text="Este campo precisará estar marcado para a página ser exibida",  # noqa 501
    )
    content = models.TextField()

    def get_absolute_url(self):
        if not self.is_published:
            return reverse("blog:index")
        return reverse("blog:page", args=(self.slug,))

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify_new(self.title)
        return super().save(*args, **kwargs)

    def __str__(self) -> str:
        return self.title


class PostManager(models.Manager):
    def get_published(self):
        return self.filter(is_published=True).order_by("-pk")


class Post(models.Model):
    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"

    objects = PostManager()

    title = models.CharField(max_length=65)
    slug = models.SlugField(
        unique=True, default=None, null=True, blank=True, max_length=255
    )
    is_published = models.BooleanField(
        default=False,
        help_text="Este campo precisará estar marcado para o post ser exibido",
    )
    excerpt = models.CharField(max_length=150)
    content = models.TextField()
    cover = models.ImageField(upload_to="posts/%Y/%m", blank=True, default="")
    cover_in_post_content = models.BooleanField(
        default=True,
        help_text="Se marcado, exibirá a capa dentro do conteúdo do post",
    )

    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name="post_created_by",
    )
    updated_at = models.DateTimeField(auto_now=True)
    updated_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name="post_updated_by",
    )

    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True, blank=True, default=None
    )
    tags = models.ManyToManyField(Tag, blank=True, default="")

    def get_absolute_url(self):
        if not self.is_published:
            return reverse("blog:index")
        return reverse("blog:post", args=(self.slug,))

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify_new(self.title)

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
        return self.title


class PostAttachment(AbstractAttachment):
    def save(self, *args, **kwargs):
        if not self.name:
            self.name = self.file.name
        file_name_before_save = str(self.file.name)

        super_save = super().save(*args, **kwargs)

        file_changed = False

        if self.file:
            if file_name_before_save != self.file.name:
                file_changed = True

        if file_changed:
            resize_image(
                image=self.file,
                new_width=900,
                optimize=True,
                quality=70,
            )

        return super_save
