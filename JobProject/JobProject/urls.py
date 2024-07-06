from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from JobProject.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',siginPage,name='siginPage'),
    path('signupPage/',signupPage,name='signupPage'),
    path('dashboard/',dashboard,name='dashboard'),
    path('logoutPage/',logoutPage,name='logoutPage'),
    path('alljobPage/',alljobPage,name='alljobPage'),


    path('editjob/<str:jobid>',editjob,name='editjob'),
    path('deletePage/<str:jobid>',deletePage,name='deletePage'),
    path('applyjob/<str:jobid>',applyjob,name='applyjob'),

    #Recriter
    path('addjobPage/',addjobPage,name='addjobPage'),

    #Profile
    path('profilebase/',profilebase,name='profilebase'),



] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
