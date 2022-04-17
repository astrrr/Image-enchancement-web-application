from django.db import models
from .utils import get_filtered_image

from PIL import Image
import numpy as np
from io import BytesIO
from django.core.files.base import ContentFile

# Create your models here.

ACTION_CHOICES =(
    ('NO_FILTER', 'no filter'),
    ('COLORIZED', 'colorized'),
    ('GRAYSCALE', 'grayscale'),
    ('BLURRED', 'blurred'),
    ('BINARY', 'binary'),
    ('INVERT', 'invert')
)

# GAMMA_CHOICES =(
#     (0.1, '0.1'),
#     (0.2, '0.2'),
#     (0.3, '0.3'),
#     (0.4, '0.4'),
#     (0.5, '0.5'),
#     (0.6, '0.6')
# )

class Upload(models.Model):
    image = models.ImageField(upload_to='images')
    action = models.CharField(max_length=50, choices=ACTION_CHOICES)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    # gamma_val = models.FloatField(choices=GAMMA_CHOICES)


    def __str__(self):
        return str(self.id)

    def save(self, *args, **kwargs):
        
        # open img
        pil_img = Image.open(self.image)

        # convert img to array and do some process
        cv_img = np.array(pil_img)
        img = get_filtered_image(cv_img, self.action)

        # gamma
        # img = gamma(cv_image, self.gamma_val)

        # convert back to pil img
        im_pil = Image.fromarray(img)

        # save
        buffer = BytesIO()
        im_pil.save(buffer, format='png') # can add more format later
        image_png = buffer.getvalue()

        self.image.save(str(self.image), ContentFile(image_png), save=False)

        super().save(*args, **kwargs)
