from django.urls import path 
from go_fluent_app import views
from django.conf.urls.static import static
from django.conf import settings
from video.views import video
from .views import (
    # QuizListView,
    quiz_view,
    quiz_data_view,
    # quiz,
    quizes,
    save_quiz_view
)

urlpatterns = [
     path('' , views.home , name= "home" ),
     path('start/' , views.choose , name= "choose"),
     path('quiz/' , quizes , name= "quizes"),
     path('quiz/<pk>/', quiz_view, name='quiz-view'),
     path('quiz/<pk>/save/', save_quiz_view, name='save-view'),
     path('quiz/<pk>/data/', quiz_data_view, name='quiz-data-view'),
     path('language/<title>/' , views.language , name='language'),
     path('language/<title>/lesson/', video ,name='video'), 
    #  path('language/<title>/quiz/', quiz ,name='quiz'),
    #  path('quiz/', QuizListView.as_view(), name='main-view'),
    #  path('language/<title>/quiz/<pk>/', quiz_view, name='quiz-view'),
    #  path('language/<title>/quiz/<pk>/save/', save_quiz_view, name='save-view'),
    #  path('language/<title>/quiz/<pk>/data/', quiz_data_view, name='quiz-data-view'),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

