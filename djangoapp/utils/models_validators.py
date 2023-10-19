from django.core.exceptions import ValidationError


def validate_png(image):
    """
    Checks if the attached image is a PNG
    """
    is_pgn = image.name.lower().endswith("png")
    if not is_pgn:
        raise ValidationError("Image needs to be PNG")


def validate_pdf(pdf):
    """
    Checks if the attached file is a pdf
    """
    is_pdf = pdf.name.lower().endswith("pdf")
    if not is_pdf:
        raise ValidationError("FIle needs to be PDF")
