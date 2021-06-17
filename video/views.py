from django.shortcuts import render
from .models import Video
from go_fluent_app.models import Category
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.
def video(request , title):
    cat=Category.objects.get(title=title)
    video=Video.objects.filter(category=cat)
    return render(request,'index.html',{'video':video})


def index(request):
    if request.method ==  'POST':
        message =request.POST['message']

        send_mail('Contact Form',
        message,
        settings.EMAIL_HOST_USER,
        'psiteamsei15@gmail.com',
        fail_silently=False)
    return render(request,'index.html')