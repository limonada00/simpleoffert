from .models import SimpleOfert
from django.contrib.auth.models import User


def create_offert(*, title, content, price, image_field, author, category):
    errors = []

    if not title.strip():
        errors.append('Title is required.')

    if not content.strip():
        errors.append('Content is required.')

    if errors:
        return None, errors

    ofertichki = SimpleOfert.objects.create(title=title, content=content, price=price, image_field=image_field,
                                            author=author, category=category)

    return ofertichki, None