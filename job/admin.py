from django.contrib import admin
from .models import Employer,Job,Applicant,Qualification,Experience, Cover_Letter, Referee
# Register your models here.
#admin.site.register(Employer)
#admin.site.register(Job)
#admin.site.register(Applicant)
#admin.site.register(Qualifications)
#admin.site.register(Experience)
#admin.site.register(Referee)

#@admin.register(Job)
#class JobAdmin(admin.ModelAdmin):
#    pass

#@admin.register(Applicant)
#class ApplicantAdmin(admin.ModelAdmin):
#    pass

#@admin.register(Qualification)
#class QualificationsAdmin(admin.ModelAdmin):
#    pass

#@admin.register(Experience)
#class ExperienceAdmin(admin.ModelAdmin):
#    pass

class JobInline(admin.TabularInline):
    model=Job

@admin.register(Employer)
class EmployerAdmin(admin.ModelAdmin):
    model=[JobInline]


@admin.register(Referee)
class RefereeAdmin(admin.ModelAdmin):
    pass


@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display=('job_name', 'skills', 'experience')
    list_filter=('station', 'contract', 'application_date')
    fields=[('job_name','industry','employer'),'summary','description_detail','education','experience',
    'skills',('application_deadline','terms_conditions')]

class RefereeInline(admin.TabularInline):
    model=Referee

@admin.register(Applicant)
class ApplicantAdmin(admin.ModelAdmin):
    list_display=('first_name','mobile','skills')
    list_filter=('status','level','location')
    fields=[('first_name','last_name'),'skills','email','mobile','date_of_birth']
    inlines=[RefereeInline]


@admin.register(Qualification)
class QualificationAdmin(admin.ModelAdmin):
    fieldsets=(
        ('Education',{'fields': ('applicant','institution','course','major')
        }),
        ('Period',{'fields': ('start_date','end_date')
        }),
    )

@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    fieldsets=(
        ('Company',{'fields': ('employed','applicant','current_employer','last_employer','job_title','responsibilities')
        }),
        ('Period',{'fields': ('start_date','end_date')
        }),
    )
