from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse


class Products(models.Model):
    product_photo = models.ImageField(upload_to='images/', blank=False)
    product_name = models.CharField(max_length=100)
    product_summary = models.CharField(max_length=512)
    product_about = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.product_summary

    def get_absolute_url(self):
        return reverse('product_detail', args=[str(self.pk)])
