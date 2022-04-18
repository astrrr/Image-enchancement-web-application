from django.db import models
from .utils_hist_match import get_historgram_matching
import cv2
from PIL import Image
import numpy as np
from io import BytesIO
from django.core.files.base import ContentFile
# Create your models here.

class HistogramMatching(models.Model):
    main_image = models.ImageField(upload_to='main image')
    sub_image = models.ImageField(upload_to='sub image')
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)

    def save(self, *args, **kwargs):
        
        # open img
        pil_main_img = Image.open(self.main_image)
        pil_sub_img = Image.open(self.sub_image)

        # convert img to array and do some process
        # cv_main_img = np.array(pil_main_img)
        # cv_sub_img = np.array(pil_sub_img)

        img = get_historgram_matching(np.array(pil_main_img), np.array(pil_sub_img))
        

        # convert back to pil img
        im_pil = Image.fromarray(img)

        # save
        buffer = BytesIO()
        im_pil.save(buffer, format='png') # can add more format later
        image_png = buffer.getvalue()

        self.main_image.save(str(self.main_image), ContentFile(image_png), save=False)

        super().save(*args, **kwargs)
