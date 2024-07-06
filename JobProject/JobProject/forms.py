from django import forms
from JobApp.models import *

class addjob_form(forms.ModelForm):
    class Meta:
        model=AddJob_Model
        fields='__all__'
        exclude=['recruiteruser']
        widgets={
            'Dead_Line':forms.DateInput(attrs={'type':'date', 'class':'date-field'}),
        }

class apply_form(forms.ModelForm):
    class Meta:
        model=Applyjob_Model
        fields=['Skills','Resume','Seeker_Profile_Pic']

class customeUser_form(forms.ModelForm):
    class Meta:
        model=CustomeUser_model
        fields=['City','Profile_Picture','email']

class basicinfo_form(forms.ModelForm):
    class Meta:
        model=BasicInformation_model
        fields='__all__'
        exclude=['portaluser']

class contactinfo_form(forms.ModelForm):
    class Meta:
        model=ContactInformation_model
        fields='__all__'
        exclude=['portaluser']

class educationinfo_form(forms.ModelForm):
    class Meta:
        model=EducationQualifiction
        fields='__all__'
        exclude=['seekeruser']

class workexperiance_form(forms.ModelForm):
    class Meta:
        model=WorkExperiance
        fields='__all__'
        exclude=['seekeruser']