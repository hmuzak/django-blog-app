from django.db import models
# Create your models here.
from taggit.managers import TaggableManager
from django_ckeditor_5.fields import CKEditor5Field

class Post(models.Model):
    title       = models.CharField(max_length=240)
    description = CKEditor5Field('Text', config_name='extends')
    published   = models.DateField(auto_now_add=True)
    slug        = models.SlugField(unique=True, max_length=150)
    tags        = TaggableManager()
    post_img    = models.ImageField()
    def __str__(self):
        return self.title

