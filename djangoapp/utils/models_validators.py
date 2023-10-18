from django.core.exceptions import ValidationError


def validate_png(image):
    """
    Checks if the attached image is a PNG
    """
    is_pgn = image.name.lower().endswith("png")
    if not is_pgn:
        raise ValidationError("Image needs to be PNG")
