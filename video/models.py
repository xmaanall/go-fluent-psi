from django.db import models
from embed_video.fields import EmbedVideoField
from go_fluent_app.models import Category

# Create your models here.
class Video(models.Model):
    caption=models.CharField(max_length=100)
    video=EmbedVideoField(null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE,null=True)
    def __str__(self):
        return self.caption


