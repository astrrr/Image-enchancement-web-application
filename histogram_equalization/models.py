from django.db import models
from .utils_hist_eq import get_historgram_equal

from PIL import Image
import numpy as np
from io import BytesIO
from django.core.files.base import ContentFile
# Create your models here.

class HistogramEqualization(models.Model):
    image = models.ImageField(upload_to='images')
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)

    def save(self, *args, **kwargs):
        
        # open img
        pil_img = Image.open(self.image)

        # convert img to array and do some process
        cv_img = np.array(pil_img)
        
        img = get_historgram_equal(cv_img)
        

        # convert back to pil img
        im_pil = Image.fromarray(img)

        # save
        buffer = BytesIO()
        im_pil.save(buffer, format='png') # can add more format later
        image_png = buffer.getvalue()

        self.image.save(str(self.image), ContentFile(image_png), save=False)

        super().save(*args, **kwargs)
