from django.db import models
from .utils_gamma import get_gamma_image

from PIL import Image
import numpy as np
from io import BytesIO
from django.core.files.base import ContentFile
import cv2
# Create your models here.

ACTION_CHOICES =(
    ('0.1', '0.1'),
    ('0.2', '0.2'),
    ('0.3', '0.3'),
    ('0.4', '0.4'),
    ('0.5', '0.5'),
    ('0.6', '0.6'),
    ('0.7', '0.7'),
    ('0.8', '0.8'),
    ('0.9', '0.9'),
    ('1.0', '1.0'),
)

# GAMMA_CHOICES =(
#     (0.1, '0.1'),
#     (0.2, '0.2'),
#     (0.3, '0.3'),
#     (0.4, '0.4'),
#     (0.5, '0.5'),
#     (0.6, '0.6')
# )

class Gamma(models.Model):
    image = models.ImageField(upload_to='images')
    gamma = models.CharField(max_length=10)
    a = models.CharField(max_length=10, default='1')
    b = models.CharField(max_length=10, default='0')
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    # gamma_val = models.FloatField(choices=GAMMA_CHOICES)


    def __str__(self):
        return str(self.id)

    def save(self, *args, **kwargs):
        
        # open img
        pil_img = Image.open(self.image)

        
        # convert img to array and do some process
        
        #img = get_filtered_image(cv_img, self.action)

        # gamma
        img = get_gamma_image(np.array(pil_img), self.gamma, self.a, self.b)

        # convert back to pil img
        im_pil = Image.fromarray(img)

        # save
        buffer = BytesIO()
        im_pil.save(buffer, format='png') # can add more format later
        image_png = buffer.getvalue()

        self.image.save(str(self.image), ContentFile(image_png), save=False)

        super().save(*args, **kwargs)
