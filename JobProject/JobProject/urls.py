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
    path('viewjob/<str:jobid>',viewjob,name='viewjob'),
    
    path('applicantPage/<str:jobid>',applicantPage,name='applicantPage'),


    #Recriter
    path('addjobPage/',addjobPage,name='addjobPage'),
    path('rejectcandidate/<str:jobid>',rejectcandidate,name='rejectcandidate'),
    path('callinterview/<str:jobid>',callinterview,name='callinterview'),


    #Profile
    path('profilebase/',profilebase,name='profilebase'),
    path('basicinfoPage/',basicinfoPage,name='basicinfoPage'),
    path('contactinfoPage/',contactinfoPage,name='contactinfoPage'),
    path('educationinfoPage/',educationinfoPage,name='educationinfoPage'),
    path('workexperiencePage/',workexperiencePage,name='workexperiencePage'),
    path('editprofilePage/',editprofilePage,name='editprofilePage'),
    path('changepassword/',changepassword,name='changepassword'),

    #Applied Job (Seeker)

    path('appliedjob/',appliedjob,name='appliedjob'),
    path('postedjob/',postedjob,name='postedjob'),



] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
