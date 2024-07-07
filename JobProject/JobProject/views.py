from django.shortcuts import render,redirect,get_object_or_404
from JobApp.models import *
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from JobProject.forms import *
from django.contrib.auth.hashers import check_password
from django.contrib.auth import update_session_auth_hash



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
            messages.success(request,message_box['signup_success'])
                
            return redirect ('siginPage')
        else:
            messages.warning(request,message_box['password_warning'])
            return redirect('signupPage')
    return render(request,'common/signupPage.html')


def siginPage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user = authenticate(username=username,password=password) 
        if user:
            login(request,user)
            messages.success(request,message_box['signin_success'])
            return redirect ('dashboard')
        else:
            messages.warning(request,message_box['signin_warning'])
            return redirect('siginPage')
    return render(request,'common/signinPage.html')

@login_required
def dashboard(request):
    return render(request,'common/dashboard.html')

@login_required
def logoutPage(request):
    logout(request)
    return redirect('siginPage')

@login_required
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
            return redirect('appliedjob')
    else:
        applyjobdata=apply_form()
    context={
        'applyjobdata':applyjobdata
    }
    return render(request,'seeker/applyjob.html',context)

@login_required
def profilebase(request):
    return render(request,'profile/profilebase.html')
    
@login_required
def appliedjob(request):
    applieddata=Applyjob_Model.objects.filter(Applicant=request.user)
    context={
        'applieddata':applieddata
    }
    return render(request,'profile/appliedjob.html',context)

@login_required
def postedjob(request):
    posteddata=AddJob_Model.objects.filter(recruiteruser=request.user)
    context={
        'posteddata':posteddata
    }
    return render(request,'profile/postedjob.html',context)

@login_required
def viewjob(request,jobid):
    viewjobdata=AddJob_Model.objects.get(id=jobid)
    context={
        'viewjobdata':viewjobdata
    }
    return render(request,'common/viewjob.html',context)


@login_required
def basicinfoPage(request):
    basicinfo=BasicInformation_model.objects.filter(portaluser=request.user)
    context={
        'basicinfo':basicinfo
    }
    return render(request,'profile/basicinfoPage.html',context)

@login_required
def contactinfoPage(request):
    contactinfo=ContactInformation_model.objects.filter(portaluser=request.user)
    context={
        'contactinfo':contactinfo
    }
    return render(request,'profile/contactinfoPage.html',context)
    
@login_required
def educationinfoPage(request):
    educationdata=EducationQualifiction.objects.filter(seekeruser=request.user)
    context={
        'educationdata':educationdata
    }
    return render(request,'profile/educationinfoPage.html',context)


@login_required
def applicantPage(request,jobid):
    job=AddJob_Model.objects.get(id=jobid)
    applicantdata=Applyjob_Model.objects.filter(Applied_job=job)

    context={
        'applicantdata':applicantdata
    }
    return render(request,'recruiter/applicantPage.html',context)


@login_required
def rejectcandidate(request,jobid):
    job=Applyjob_Model.objects.get(id=jobid)
    job.Status='Rejected'
    job.save()
    return redirect('applicantPage',jobid=job.Applied_job.id)


@login_required
def callinterview(request,jobid):
    job=Applyjob_Model.objects.get(id=jobid)
    job.Status='Approved'
    job.save()
    return redirect('applicantPage',jobid=job.Applied_job.id)


@login_required
def workexperiencePage(request):
    workinfo=WorkExperiance.objects.filter(seekeruser=request.user)
    context={
        'workinfo':workinfo
    }   
    return render(request,'profile/workexperiencePage.html',context)

def editprofilePage(request):
    basicmodel=BasicInformation_model.objects.get(portaluser=request.user)
    contactmodel=ContactInformation_model.objects.get(portaluser=request.user)
    if request.user.User_Type== 'jobseeker':
        edumodel=EducationQualifiction.objects.get(seekeruser=request.user)
        workmodel=WorkExperiance.objects.get(seekeruser=request.user)

    if request.method == 'POST':
        editpro=customeUser_form(request.POST,request.FILES,instance=request.user)
        basic=basicinfo_form(request.POST,instance=basicmodel)
        contact=contactinfo_form(request.POST,instance=contactmodel)
        if request.user.User_Type== 'jobseeker':
            education=educationinfo_form(request.POST,instance=edumodel)
            work=workexperiance_form(request.POST,instance=workmodel)
        if editpro.is_valid():
            editpro.save()
        if basic.is_valid():
            basic.save()
        if contact.is_valid():
            contact.save()
        if education.is_valid():
            education.save()
        if work.is_valid():
            work.save()
            return redirect('profilebase')
    else:
        editpro=customeUser_form(instance=request.user)
        basic=basicinfo_form(instance=basicmodel)
        contact=contactinfo_form(instance=contactmodel)
        if request.user.User_Type== 'jobseeker':
            education=educationinfo_form(instance=edumodel)
            work=workexperiance_form(instance=workmodel)
            context={
                'editpro':editpro,
                'basic':basic,
                'contact':contact,
                'education':education,
                'work':work,

            }
    context={
    'editpro':editpro,
    'basic':basic,
    'contact':contact,


}  
    return render(request,'profile/editprofilePage.html',context)




@login_required
def changepassword(request):
    current_user=request.user
    if request.method=="POST":
        current_pass=request.POST.get('current_pass')
        new_pass=request.POST.get('new_pass')
        confirm_new_pass=request.POST.get('confirm_new_pass')
        
        pass_check = check_password(current_pass,current_user.password)
        if pass_check:
            if new_pass==confirm_new_pass:
                current_user.set_password(new_pass)
                current_user.save()
                update_session_auth_hash(request,current_user)
                return redirect('profilebase')
    return render(request,'profile/changepassword.html')

    