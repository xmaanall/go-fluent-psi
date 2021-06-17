from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save


# Create your models here.

class Profile(models.Model):
    # image = models.ImageField(upload_to ="img/" , null=True)
    goal =models.TextField(max_length=140, null = True)
    native = models.CharField(max_length=50, null = True)
    user = models.OneToOneField(User , related_name="profile" , on_delete=models.CASCADE)
    
    def __str__(self):
        return self.user.username

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance , id =instance.id )

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()