from django.db import models
from django.utils import timezone
from datetime import datetime
from datetime import date
from django.urls import reverse
import random
import os

# from django.contrib.auth.models import User
# from  django.contrib.auth.mixins import LoginRequiredMixin


# Create your models here.


class Employer(models.Model):
    profile_picture = models.ImageField(
        upload_to="user_e/", help_text="Profile Picture", null=True, blank=True
    )
    company_name = models.CharField(max_length=255, help_text="Employer Name")
    email = models.EmailField(max_length=254, help_text="Official Email")
    mobile = models.CharField(max_length=255, help_text="Enter Mobile Number")
    location = models.CharField(max_length=255, help_text="Enter Company Location")

    @property
    def jobs(self):
        jobs = self.jobs.all()

    def get_absolute_url(self):
        return reverse("employer_detail", args=[str(self.id)])

    def __str__(self):
        return f"{self.company_name}({self.email})"


class Job(models.Model):
    job_name = models.CharField(max_length=255, help_text="Enter Job Title")
    ref_no = models.CharField(max_length=255, help_text="Enter Job Ref Number")
    industry = models.CharField(max_length=254)
    employer = models.ForeignKey(
        "Employer", max_length=255, on_delete=models.CASCADE, related_name="jobs"
    )
    summary = models.TextField(max_length=255, help_text="Job Summary")
    description_detail = models.TextField(
        max_length=254, help_text="Detailed Job Description"
    )
    education = models.CharField(max_length=254, help_text="Education Level")
    experience = models.TextField(max_length=255, help_text="Preferred Experience")
    skills = models.TextField(max_length=254, help_text="Desired Skills")
    terms_conditions = models.TextField(max_length=255)
    application_date = models.DateField(auto_now_add=True)
    application_deadline = models.DateTimeField()

    LOCATION = (
        ("Nrb", "Nairobi"),
        ("Msa", "Mombasa"),
        ("Mch", "Machakos"),
        ("Ksm", "Kisumu"),
        ("Eld", "Eldoret"),
        ("Nks", "Nakuru"),
        ("Thk", "Thika"),
    )

    station = models.CharField(
        max_length=100,
        choices=LOCATION,
        help_text="Where The Job Is Located",
        default="Nrb",
    )

    EMPLOYMENT_CONTRACT = (
        ("per", "permanent"),
        ("ren", "Renewable"),
        ("Int", "Internship"),
        ("Att", "Attachment"),
    )

    contract = models.CharField(
        max_length=100,
        choices=EMPLOYMENT_CONTRACT,
        help_text="Type of Employment",
        default="per",
    )

    def get_absolute_url(self):
        return reverse("job_detail", args=[str(self.id)])

    def __str__(self):
        return self.description_detail


class Applicant(models.Model):

    profile_picture = models.ImageField(
        upload_to="user_e/", null=True, blank=True, help_text="Profile Picture",
    )
    first_name = models.CharField(max_length=100, help_text="Enter First Name")
    last_name = models.CharField(max_length=100, help_text="Enter Last Name")
    date_of_birth = models.DateField()
    skills = models.TextField(max_length=255, help_text="List Your Skills")
    email = models.EmailField(max_length=254, help_text="Enter Email")
    mobile = models.CharField(max_length=255, help_text="Enter Mobile Number")
    id_number = models.CharField(max_length=255, help_text="Enter ID Number")
    passport_number = models.CharField(
        max_length=255, help_text="Enter Passport Number", blank="True", null="True"
    )

    def get_absolute_url(self):
        return reverse("applicant_detail", args=[str(self.id)])

    @property
    def age(self):
        # datetime.strptime(self.date_of_birth, "%Y-%m-%d").date()
        return (date.today() - self.date_of_birth).days // 365

    @property
    def year_of_work_experience(self):
        for experience in self.experiences.all():
            if experience.start_date and experience.end_date:
                return (experience.end_date - experience.start_date).days // 365
            else:
                return (date.today() - experience.start_date).days // 365

    @property
    def title(self):
        for experience in self.experiences.all():
            if experience.job_title:
                return experience.job_title
            else:
                return experience.responsibilities

    @property
    def education(self):
        qualifications = self.qualifications.all()

    @property
    def Referee(self):
        for referee in self.referees.all():
            if referee.full_name and referee.mobile:
                return f"{referee.full_name}{referee.mobile}"
            else:
                return referee.mobile

    SEX = (
        ("M", "Male"),
        ("F", "Female"),
    )

    gender = models.CharField(
        max_length=255, choices=SEX, default="F", help_text="Select Your Gender",
    )

    GRADUATED_STATUS = (
        ("DR", "Dropped Out"),
        ("SC", "Schooling"),
        ("YT", "Yet To graduate"),
        ("GR", "graduated"),
    )

    status = models.CharField(
        max_length=100,
        choices=GRADUATED_STATUS,
        default="GR",
        help_text="Education Progress",
    )

    ACADEMIC_LEVEL = (
        ("C", "Certificate"),
        ("D", "Diploma"),
        ("HD", "Higher-Diploma"),
        ("D", "Degree"),
        ("M", "Masters"),
        ("DR", "Doctorate"),
        ("PHD", "Professor"),
    )

    level = models.CharField(
        max_length=100, choices=ACADEMIC_LEVEL, default="D", help_text="Academic Level",
    )

    LANGUAGE = (
        ("ksw", "Kiswahil"),
        ("eng", "English"),
        ("shg", "Sheng"),
        ("lhy", "Luhya"),
        ("kky", "Kikuyu"),
    )

    language = models.CharField(
        max_length=100, choices=LANGUAGE, default="ksw", help_text="Fluet Language",
    )

    COUNTRY = (
        ("ky", "Kenya"),
        ("ug", "Uganda"),
        ("tz", "Tanzania"),
        ("rw", "Rwanda"),
        ("sd", "Sudan"),
        ("ng", "Nigeria"),
        ("gh", "Ghana"),
    )

    location = models.CharField(
        max_length=100, choices=COUNTRY, default="ky", help_text="Your country",
    )

    class Meta:
        ordering = ["first_name"]


class Qualification(models.Model):
    applicant = models.ForeignKey(
        "Applicant", on_delete=models.PROTECT, related_name="qualifications"
    )
    institution = models.CharField(max_length=255, null="True", blank="True")
    course = models.CharField(max_length=254, null="True", blank="True")
    major = models.CharField(max_length=100)
    achivement = models.TextField(max_length=255, help_text="Enter Attainment")
    start_date = models.DateField(auto_now=False)
    end_date = models.DateField(auto_now=False)

    def get_absolute_url(self):
        return reverse("qualification_detail", args=[str(self.id)])

    def __str__(self):
        return f"{self.applicant}{self.institution}"


class Experience(models.Model):
    employed = models.BooleanField(default=False, help_text="Are You Employed?")
    applicant = models.ForeignKey(
        "Applicant", default="0", on_delete=models.PROTECT, related_name="experiences"
    )
    current_employer = models.CharField(max_length=254)
    last_employer = models.CharField(max_length=254)
    job_title = models.CharField(max_length=250, help_text="Name Your Specialisation")
    responsibilities = models.TextField()
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)

    def get_absolute_url(self):
        return reverse("experience_detail", args=[str(self.id)])

    def __str__(self):
        return f"{self.applicant} ({self.responsibilities})"


#
# def get_filename_ext(filepath):
#     base_name = os.path.basename(filename)
#     name, ext = os.path.splitext(base_name)
#     return name, ext
#
# def upload_file_path(instance, filename):
#     #print(instance)
#     #print(filename)
#     new_filename = random.randint(1,436545545)
#     name, ext = get_filename_ext(filename)
#     final_filename = f'{new_filename}{ext}'  #.format(new_filename=new_filename,ext=ext)
#
#     return "uploads/{new_filename}/{new_filename}".format(new_filename=new_filename,
#     final_filename=final_filename)


class Cover_Letter(models.Model):
    cv_attachment = models.FileField(
        upload_to="uploads/cvs/", help_text="Attach Your Curriculum Vitae"
    )
    description = models.TextField()

    def cv_uploads_path(cv_attachment, uploads):
        return "Cover_Letter_{0}/{1}".format(cv_attachment.Cover_Letter.id, uploads)

    def get_absolute_url(self):
        return reverse("cover_letter_detail", args=[str(self.id)])

    def __str__(self):
        return self.description


class Referee(models.Model):
    applicant = models.ForeignKey(
        "Applicant", max_length=255, on_delete=models.PROTECT, related_name="referees"
    )
    full_name = models.CharField(max_length=255, help_text="Enter Full Names")
    mobile = models.CharField(max_length=255, help_text="Enter Number")
    email = models.EmailField(max_length=254, help_text="Enter Email")

    class meta:
        ordering = ["full_name"]

    def get_absolute_url(self):
        return reverse("referee_detail", args=[str(self.id)])

    def Referees(self):
        referee = []
        referee = referees()
        return self.referee


# class Contact(models.Model):
#     your_name=models.CharField(max_length=255,help_text='Enter your name')
#     email=models.CharField(max_length=255)
#     mobile=models.CharField(max_length=254)
#
#     NEEDED_SERVICES=(
#         ('CR','Charges'),
#         ('SR','Services'),
#         ('SI','Signing Up'),
#         ('JS','Job Seeker'),
#         ('EM','Employer'),
#         ('AO','Any Other'),
#     )
#
#     services=models.CharField(
#         max_length=255,
#         choices=NEEDED_SERVICES,
#         default='CR',
#         help_text=''
#     )
#
#     message=models.TextField(max_length=255,help_text="Your message here...")
