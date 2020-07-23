from django import forms
from job.models import Employer,Job,Applicant,Qualification,Experience,Cover_Letter,Referee
from django.core.exceptions import ValidationError
from django.utils import timezone
from datetime import datetime,timedelta, date


class RegisterEmployerForm(forms.ModelForm):

    error_messages = {
        'duplicate_email': ('An employer with the specified email already exists.'),
        'duplicate_mobile': ('Please enter another mobile number.')
    }

    class Meta:
        model = Employer
        fields = ("profile_picture","company_name","email","mobile","location")

        def clean_email(self):
            email = self.cleaned_data['email']
            if not email:
                raise forms.ValidationError('Please enter a valid email')
            if Employer.objects.filter(email__iexact=str(email)).count() > 0:
                raise forms.ValidationError(self.error_messages['duplicate_email'])

            return email

        def clean_mobile(self):
            mobile = slef.cleaned_data['mobile']
            if not mobile:
                raise forms.ValidationError('Please enter a valid mobile number')
            if Employer.objects.filter(mobile__iexact=str(mobile)).count() > 0:
                raise forms.ValidationError(self.error_messages['duplicate_mobile'])

            return mobile


class PostJobForm(forms.ModelForm):
    error_messages = {
        'duplicate_ref_no': ('A job with the specified ref-number already exists')
    }

    class Meta:
        model = Job
        fields = ("job_name","ref_no","industry","summary","description_detail","education",
            "experience","skills","terms_conditions","application_deadline")

        def clean_ref_no(self):
            ref_no = self.cleaned_data['ref_no']
            if not ref_no:
                raise forms.ValidationError('Please enter job reference number')
            if Job.objects.filter(ref_no__iexact=str(ref_no)).count() > 0:
                raise forma.ValidationError(self.error_messages['duplicate_ref_no'])

            return ref_no


class RegisterApplicantForm(forms.ModelForm):

    error_messages= {
        'duplicate_mobile': ('An application with the specified mobile number already exists.'),
    }

    class Meta:
        model = Applicant
        fields = ("profile_picture","first_name","last_name","date_of_birth","skills","email","mobile",
            "id_number","passport_number")

    def clean_mobile(self):
        mobile = self.cleaned_data['mobile']
        if not mobile:
            raise forms.ValidationError('Please enter your mobile number')
        if Applicant.objects.filter(mobile__iexact=str(mobile)).count() > 0:
            raise forms.ValidationError(self.error_messages['duplicate_mobile'])

        return mobile

    def clean_date_of_birth(self):
        date_of_birth = self.cleaned_data['date_of_birth']
        oldest_date = timezone.now().date() - timedelta(days=150*365)

        if date_of_birth < oldest_date:
            raise ValidationError('A person cannot be more than 150 years old')

        return date_of_birth


class SubmitQualificationForm(forms.ModelForm):

    class Meta:
        model = Qualification
        fields = ("institution","course","major","achivement","start_date","end_date")

    # def clean_applicant(self):
    #     applicant = self.cleaned_data["applicant"]
    #     applicant_exists = Qualification.objects.filter(applicant=applicant).exists()
    #     if applicant_exists:
    #         raise ValidationError("Qualification for the applicant already exists")
    #     return applicant

    def clean_start_date(self):
        start_date = self.cleaned_data['start_date']
        if start_date and start_date >= date.today():
            raise  forms.ValidationError('Please enter appropriate start date.')

        return start_date

    def clean_end_date(self):
        start_date_string = self.data.get("start_date")
        # convert date string to date object
        start_date = datetime.strptime(start_date_string, "%Y-%m-%d")
        end_date = self.cleaned_data['end_date']

        if end_date < start_date.date():
            raise forms.ValidationError('Please enter appropriate end date.')

        return end_date


class SubmitExperienceForm(forms.ModelForm):

    class Meta:
        model = Experience
        fields = ("employed","current_employer","last_employer","job_title",
        "responsibilities","start_date","end_date")

    def clean_start_date(self):
        start_date = self.cleaned_data['start_date']

        if start_date and start_date >= date.today():
            raise form.ValidationError('Please enter appropriate date.')

        return start_date

    def clean_end_date(self):
        start_date_string = self.data.get("start_date")

        start_date = datetime.strptime(start_date_string, "%Y-%m-%d")
        end_date = self.cleaned_data['end_date']

        if end_date < start_date.date():
            raise forms.ValidationError('Please enter appropriate end date.')

        return end_date

class AttachCover_LetterForm(forms.ModelForm):

    class Meta:
        model = Cover_Letter
        fields = ("cv_attachment", "description")

        def clean_cv_attachment(self):
            cv_attachment = self.cleaned_data['cv_attachment']
            if not cv_attachment:
                raise form.ValidationError('Please attach your cv here.')
            return cv_attachment

        def clean_description(self):
            description = self.cleaned_data['description']
            if  not description:
                raise form.ValidationError('Please write your application letter.')
            return description

class DeclareRefereeForm(forms.ModelForm):

    error_messages={
    'obsolete_mobile': ('Please enter not more than two numbers in use')
    }

    class Meta:
        model = Referee
        fields = ("full_name","mobile","email")

    def clean_mobile(self):
        mobile = self.cleaned_data['mobile']
        if not mobile:
            raise form.ValidationError('Please enter the referee valid mobile number')

        if Referee.objects.filter(mobile=str(mobile)).count() > 2:
            raise forms.ValidationError(self.error_messages['obsolete_mobile'])
