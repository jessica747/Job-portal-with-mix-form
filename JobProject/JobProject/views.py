from django.shortcuts import render,redirect
from JobApp.models import *
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from JobProject.forms import *


message_box={
    'signup_success':'Signup is successfully done',
    'password_warning':'password do not match',
    'signin_success' : 'signin successfully done ',
    'signin_warning' :'credential does not match '
}

def signupPage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        confirm_password=request.POST.get('confirm_password')
        email=request.POST.get('email')
        User_Type=request.POST.get('user_type')
        City=request.POST.get('city')
        Gender=request.POST.get('gender')
        Profile_Picture=request.FILES.get('profile_picture')
        if password==confirm_password:
            user=CustomeUser_model.objects.create_user(
                username=username,
                password=confirm_password,
                User_Type=User_Type,
                City=City,
                email=email,
                Gender=Gender,
                Profile_Picture=Profile_Picture,
                )
            user.save()
            basicuser=BasicInformation_model.objects.create(portaluser=user)
            basicuser.save()
            if User_Type == 'recruiter':
                contactuser=ContactInformation_model.objects.create(portaluser=user)
                contactuser.save()

            return redirect ('siginPage')
    return render(request,'common/signupPage.html')


def siginPage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user = authenticate(username=username,password=password) 
        if user:
            login(request,user)
            return redirect ('dashboard')
    return render(request,'common/signinPage.html')


def dashboard(request):
    return render(request,'common/dashboard.html')

login_required
def logoutPage(request):
    logout(request)
    return redirect('logoutPage')


def addjobPage(request):
    if request.method == 'POST':
        addjobdata=addjob_form(request.POST,request.FILES)
        if addjobdata.is_valid():
            jobform=addjobdata.save(commit=False)
            jobform.recruiteruser=request.user
            jobform.save()
            return redirect('alljobPage')
    else:
        addjobdata=addjob_form()
    context={
        'addjobdata':addjobdata

    }
    return render(request,'recruiter/addjobPage.html',context)
@login_required
def alljobPage(request):
    alljobdata=AddJob_Model.objects.all()
    context={
        'alljobdata':alljobdata
    }
    return render(request,'common/alljobPage.html',context)

@login_required
def editjob(request,jobid):
    job=AddJob_Model.objects.get(id=jobid)
    if request.method == 'POST':
        editjobdata=addjob_form(request.POST,request.FILES,instance=job)
        if editjobdata.is_valid():
            jobform=editjobdata.save(commit=False)
            jobform.recruiteruser=request.user
            jobform.save()
            return redirect('alljobPage')
    else:
        editjobdata=addjob_form(instance=job)
    context={
        'editjobdata':editjobdata

    }
    return render(request,'recruiter/editjob.html',context)

@login_required
def deletePage(request,jobid):
    deletedata=AddJob_Model.objects.get(id=jobid)
    deletedata.delete()
    return redirect('alljobPage')

@login_required
def applyjob(request,jobid):
    applydata=AddJob_Model.objects.get(id=jobid)
    if request.method == 'POST':
        applyjobdata=apply_form(request.POST,request.FILES)
        if applyjobdata.is_valid():
            applyform=applyjobdata.save(commit=False)
            applyform.Applicant=request.user
            applyform.Applied_job=applydata
            applyform.save()
            return redirect('')
    else:
        applyjobdata=apply_form()
    context={
        'applyjobdata':applyjobdata
    }
    return render(request,'seeker/applyjob.html',context)

@login_required
def profilebase(request):
    return render(request,'profile/profilebase.html')
    