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