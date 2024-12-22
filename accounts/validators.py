from django.core.exceptions import ValidationError
import os

def allow_only_images_validator(value):
    ext = os.path.splitext(value.name)[1] #cover-images.jpg
    print(ext)
    valid_extenstions=['.jpg','.png','.jpeg']
    if not ext.lower() in valid_extenstions:
        raise ValidationError('unsupported file extenstions. Allowed extenstions:' +str(valid_extenstions))