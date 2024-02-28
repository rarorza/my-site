from django.db import models
from utils.models_validators import validate_pdf, validate_png
from utils.resize_image import resize_image


class MenuLink(models.Model):
    class Meta:
        verbose_name = "Menu Link"
        verbose_name_plural = "Menu Links"

    title = models.CharField(max_length=50)
    url_or_path = models.CharField(max_length=2048)
    new_tab = models.BooleanField(default=False)
    site_setup = models.ForeignKey(
        "SiteSetup",
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        default=None,
    )

    def __str__(self):
        return self.title


class SiteSetup(models.Model):
    class Meta:
        verbose_name = "Setup"
        verbose_name_plural = "Setup"

    title = models.CharField(max_length=65)
    description = models.CharField(max_length=255)
    show_header = models.BooleanField(default=True)
    show_search = models.BooleanField(default=True)
    show_menu = models.BooleanField(default=True)
    show_description = models.BooleanField(default=True)
    show_pagination = models.BooleanField(default=True)
    show_footer = models.BooleanField(default=True)

    favicon = models.ImageField(
        upload_to="assets/favicon/%Y/%m/",
        blank=True,
        default="",
        validators=[validate_png],
    )
    profile_pic = models.ImageField(
        upload_to="assets/profile_pic/%Y/%m/",
        blank=True,
        default="",
        validators=[validate_png],
    )
    cv = models.FileField(
        upload_to="assets/cv/%Y/%m/",
        blank=True,
        default="",
        validators=[validate_pdf],
    )

    def save(self, *args, **kwargs):
        current_favicon_name = str(self.favicon.name)
        current_profile_pic = str(self.profile_pic.name)
        super().save(*args, **kwargs)

        favicon_changed = False
        profile_pic_changed = False

        if self.favicon:
            if current_favicon_name != self.favicon.name:
                favicon_changed = True

        if self.profile_pic:
            if current_profile_pic != self.profile_pic.name:
                profile_pic_changed = True

        if favicon_changed:
            resize_image(image=self.favicon, new_width=32)

        if profile_pic_changed:
            resize_image(image=self.profile_pic, new_width=524)

    def __str__(self):
        return self.title
