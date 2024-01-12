from django.urls import path
from learner import views

urlpatterns=[
    path('',views.index,name='index'),
    path('about',views.about,name='about'),
    path('login' , views.user_login , name="login"),
    path('courses',views.courses,name='courses'),
]