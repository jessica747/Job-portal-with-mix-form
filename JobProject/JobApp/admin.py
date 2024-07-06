from django.contrib import admin
from JobApp.models import *

class CustomeUser_model_Display(admin.ModelAdmin):
    list_display=['username','User_Type','Gender']


admin.site.register(CustomeUser_model,CustomeUser_model_Display)
admin.site.register(BasicInformation_model)
admin.site.register(ContactInformation_model)
admin.site.register(EducationQualifiction)
admin.site.register(WorkExperiance)
admin.site.register(AddJob_Model)
admin.site.register(Applyjob_Model)
