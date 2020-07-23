from django.shortcuts import (
    render,
    get_object_or_404,
)  # shortcut function to generate an HTML file using a template and data:
from job.models import (
    Employer,
    Job,
    Applicant,
    Qualification,
    Experience,
    Cover_Letter,
    Referee,
)
from .forms import (
    RegisterApplicantForm,
    PostJobForm,
    RegisterEmployerForm,
    SubmitQualificationForm,
    SubmitExperienceForm,
    AttachCover_LetterForm,
    DeclareRefereeForm,
)
from django.contrib import messages
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.views import generic, View

# from django.contrib.auth.decorators import permission_required
# from django.http import HttpResponseRedirect
# Create your views here.

def home_view(request, *args, **kwargs):

    return render(request, "home.html", {})

def employer_list_view(request):
    employer_list = Employer.objects.all()

    data = {
        "employer_list": employer_list,
    }

    return render(request, "employer_list.html", context=data)


def job_list_view(request):
    jobs_list = Job.objects.all()

    content = {
        "jobs_list": jobs_list,
    }
    return render(request, "job_list.html", context=content)


def applicant_list_view(request):
    applicants_list = Applicant.objects.all()

    data = {
        "applicants_list": applicants_list,
    }
    return render(request, "applicant_list.html", context=data)


def qualification_list_view(request):
    qualifications_list = Qualification.objects.all()

    context = {
        "qualifications_list": qualifications_list,
    }
    return render(request, "qualification_list.html", context=context)


def experience_list_view(request):
    experiences_list = Experience.objects.all()

    data = {
        "experiences_list": experiences_list,
    }

    return render(request, "experience_list.html", context=data)


def cover_letter_list_view(request):
    cover_letter_list = Cover_Letter.objects.all()

    context = {
        "cover_letter_list": cover_letter_list,
    }

    return render(request, "cover_letter_list.html", context=context)


def referee_list_view(request):
    referee_list = Referee.objects.all()

    data = {
        "referee_list": referee_list,
    }
    return render(request, "referee_list.html", context=data)



def employer_detail_view(request, id):
    try:
        employer = Employer.objects.get(id=id)

    except Employer.DoesNotExist:
        raise Http404("Employer does not exist")

    return render(request, "employer_detail.html", context={"employer": employer})


def job_detail_view(request, id):
    job = get_object_or_404(Job, id=id)

    context = {"job": job}
    return render(request, "job_detail.html", context={"job": job})


def applicant_detail_view(request, id):
    applicant = get_object_or_404(Applicant, id=id)

    context = {"applicant": applicant}
    return render(
        request, "applicant_detail.html", context={"applicant": applicant}
    )


def qualification_detail_view(request, id):
    try:
        qualification = Qualification.objects.get(id=id)

    except Qualification.DoesNotExist:
        raise Http404("Qualification does not exist")

    return render(
        request,
        "qualification_detail.html",
        context={"qualification": qualification},
    )


def experience_detail_view(request, id):
    experience = get_object_or_404(Experience, id=id)

    experience = {"experience": experience}

    return render(
        request, "experience_detail.html", context={"experience": experience}
    )


def cover_letter_detail_view(request, id):
    cv_attachment = get_object_or_404(Cover_Letter, id=id)

    context = {"cv_attachment": cv_attachment}

    return render(
        request, "cover_detail.html", context)


def referee_detail_view(request, id):
    try:
        referee = Referee.objects.get(id=id)

    except Referee.DoesNotExist:
        raise Http404("Referees do not exist ")
    return render(request, "referee_detail.html", content={"referee": referee})


# class JobDetailView(generic.DetailView):
# model = Job

# class ApplicantListView(generic.ListView):
#    model = Applicant
#    paginate_by = 10

# class QualificationListView(generic.ListView):
#    model = Qualification

# class ExperienceListView(generic.ListView):
#    model = Experience


# class RefereeListView(generic.ListView):
#    model = Referee


class EmployerObjectMixin(object):
    model = Employer
    lookup = "id"


    def get_object(self):
        id = self.kwargs.get(self.lookup)
        obj = None
        if id is not None:
            obj = get_object_or_404(self.model, id=id)

        return obj


class EmployerCreateView(EmployerObjectMixin,View):
    template_name="employer_create.html"

    def get(self, request, *args, **kwargs):
        forms = RegisterEmployerForm()
        context = {
            "form": form
        }
        return render(request,self.template_name, context)

    def post(self, request, *args, **kwargs):
        forms = RegisterEmployerForm(request.POST)
        if form.is_valid():
            form.save()

        context = {
            "form": form
        }
        return render(request, self.template_name, context)


class EmployerUpdateView(EmployerObjectMixin, View):
    template_name = "employer_update.html"

    def get(self, request, *args, **kwargs):
        context = {}
        obj = self.object.get()

        if obj is not None:
            forms = RegisterEmployerForm(instance=obj)
            context['object'] = obj
            context['form'] = form
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        context = {}
        obj = self.object.get()

        if obj is not None:
            forms = RegisterEmployerForm(request.POST, instance=obj)
            if form.is_valid():
                form.save()
            context['object'] = obj
            context['form'] = form

        return render(request, self.template_name, context)



class EmployerDeleteView(EmployerObjectMixin, View):
    template_name = "employer_delete.html"


    def get(self, request, *args, **kwargs):
        context = {}
        obj = self.object.get()

        if obj is not None:
            context['object'] = obj

        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        context = {}
        obj = self.object.get()

        if obj is not None:
            obj.delete()
            context['object'] = None
            return redirect('employers_list')

        return render(request, self.template_name, context)


class JobObjectMixin(object):
    model = Job
    lookup = "id"

    def get_object(self):
        id = self.kwargs.get(self.lookup)
        obj = None

        if id is not None:
            obj = get_object_or_404(self.model, id=id)

        return obj


class JobCreateView(View):
    template_name = "job_create.html"

    def get(self, request, *args, **kwargs):
        froms = PostJobForm()
        context = {
            "form": form
        }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        froms = PostJobForm(request.POST)
        if form.is_valid():
            form.save()
        context = {
            "form": form
        }
        return render(request, self.template_name, context)


class JobUpdateView(JobObjectMixin, View):
    template_name = "job_update.html"

    def get(self, request, *args, **kwargs):
        context = {}
        obj = self.object.get()

        if obj is not None:
            forms = PostJobForm(instance=obj)
            context['object'] = obj
            context['form'] = form

        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        context = {}
        obj = self.object.get()

        if obj is not None:
            froms = PostJobForm(request.POST, instance=obj)
            if form.is_valid():
                form.save()
            context['object'] = obj
            context['form'] = form

        return render(request, self.template_name, context)


class JobDeleteView(JobObjectMixin, View):
    template_name = "job_delete.html"

    def get(self, request, *args, **kwargs):
        context = {}
        obj = self.object.get()

        if obj is not None:
            context['object'] = obj

        return render(request, self.template_name, context)


    def post(self, request, *args, **kwargs):
        context = {}
        obj = self.object.get()

        if obj is not None:
            obj.delete()
            context['object'] = None
            return redirect("jobs_list")

        return render(request, self.template_name, context)


def applicant_create_view(request):
    form = RegisterApplicantForm()
    if request.method == 'POST':
        form = RegisterApplicantForm(request.POST)
        if form.is_valid():
            Applicant.objects.create(**form.cleaned_data)
            form.save()
        else:
            return(form.errors)

    context = {
        "form": form
    }
    return render(request, 'applicant_create.html', context)


def applicant_update_view(request):
    form = RegisterApplicantForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = RegisterApplicantForm()

        context = {
            "form": form
        }
    return render(request, "applicant_update.html", context)


def applicant_delete_view(request, id):
    obj = get_object_or_404(Applicant, id=id)

    if request.method == "POST":
        obj.delete()
        return redirect('applicant_list.html')

        context = {
            "object": obj
        }
        return render(request,'applicant_delete.html', context)


def qualification_create_view(request):
    form = SubmitQualificationForm(request.POST or None)
    if form.is_valid():
        form.save()

    context = {
        "form": form
    }

    return render(request,'qualification_create.html', context)


def qualification_update_view(request):
    form = SubmitQualificationForm(request.POST, None)
    if form.is_valid():
        form.save()
        form = SubmitQualificationForm()

        context = {
            "form": form
        }
    return render(request,'qualification_update.html', context)

class QualificationDelete(DeleteView):
    model = Qualification
    success_url = reverse_lazy("qualifications")


def qualification_delete_view(request, id):
    obj = get_object_or_404(Qualification, id=id)

    if request.method == "POST":
        obj.delete()

        return redirect('qualification_list.html')

    context = {
        "form": obj
    }

    return render(request,"qualification_delete.html", context)


def experience_create_view(request):
    form = SubmitExperienceForm(request.POST or None)

    if form.is_valid():
        form.save()

    context = {
        "form": form
    }
    return render(request,'experience_create.html', context)


def experience_update_view(request):
    form = SubmitExperienceForm()

    if form.is_valid():
        form.save()

        form = SubmitExperienceForm()

        context = {
            "form": form
        }
    return render(request,'experience_update.html', context)


def experience_delete_view(request, id):
    obj = get_object_or_404(Experience, id=id)

    if request.method == "POST":
        obj.delete()

        return redirect('experience_list.html')

    context = {
        "object":obj
    }
    return render(request,'experience_delete.html', context)


class RefereeCreateView(CreateView):
    template_name = 'referee_create.html'

    form = DeclareRefereeForm
    queryset = Referee.objects.all()
    # success_url = '/'

    def form_valid(self, form):
        return super().form_valid(form)


class RefereeUpdateView(UpdateView):
    template_name = 'referee_update.html'

    form = DeclareRefereeForm

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Referee, id=id)

    def form_valid(self, form):
        return super().form_valid(form)


class RefereeDeleteView(DeleteView):
    template_name = 'referee_delete.html'

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Referee, id=id)

    def get_success_url(self):
        return reverse('referee_list.html')


class Cover_LetterCreateView(CreateView):
    template_name = 'cover_letter_create.html'

    form = AttachCover_LetterForm
    queryset = Cover_Letter.objects.all()


    def form_valid(self, form):
        return super().form_valid(form)


class Cover_LetterUpdateView(UpdateView):
    template_name = "cover_letter_update.html"

    form = AttachCover_LetterForm

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Cover_Letter, id=id)

    def form_valid(self, form):
        return super().form_valid(form)


class Cover_LetterDeleteView(DeleteView):
    template_name = 'cover_letter_delete.html'

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Cover_Letter, id=id)

    def get_success_url(self):
        return reverse('cover_letter_list.html')


def register_employer(request):
    if request.method == "POST":
        form = RegisterEmployerForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Your company has been registered")
            return render(request, "thankyou.html", {})

    else:
        form = RegisterEmployerForm()
    return render(request, "register_employer.html", {"form": form})


def post_job(request):
    if request.method == "POST":
        form = PostJobForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Your company job has been posted")
            return render(request, "thankyou.html", {})
    else:
        form = PostJobForm()
    return render(request, "post_job.html", {"form": form})


def register_applicant(request):
    if request.method == "POST":
        form = RegisterApplicantForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Complete your profile registration")
            return render(request, "thankyou.html", {})

        # redirect to anew URL:
        # return HttpResponseRedirect(reverse('index'))
    else:
        form = RegisterApplicantForm()
    return render(request, "register_applicant.html", {"form": form})


def submit_qualification(request):
    if request.method == "POST":
        form = SubmitQualificationForm(request.POST, request.FILES)
        if form.is_valid():
            applicant = Applicant.objects.get(id=request.user)
            form.cleaned_data["applicant"] = applicant
            form.save()
            messages.success(request, "Your qualifications have been submitted")
            return render(request, "thankyou.html", {})
    else:
        form = SubmitQualificationForm()
    return render(request, "submit_qualification.html", {"form": form})


def submit_experience(request):
    if request.method == "POST":
        form = SubmitExperienceForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Your experiences have been submitted")
            return render(request, "thankyou.html", {})

    else:
        form = SubmitExperienceForm()
    return render(request, "submit_experience.html", {"form": form})


def attach_cover_letter(request):
    if request.method == "POST":
        form = AttachCover_LetterForm(request.POST, request.FILES)
        if form.is_valid():
            # handle_uploaded_file(request.FILES['cv_attachment'])
            form.save()
            messages.success(request, "Your application letter has been attached")

            return render(request, "thankyou.html", {})
    else:
        form = AttachCover_LetterForm()
    return render(request, "attach_cover_letter.html", {"form": form})


def submit_referee(request):
    if request.method == "POST":
        form = DeclareRefereeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Your referees list has been binded")
            return render(request, "thankyou.html", {})

    else:
        form = DeclareRefereeForm()
    return render(request, "submit_referee.html", {"form": form})


def contact(request):
    return render(request, "contact.html", {})


# class EmployerListView(generic.ListView):
#    model = Employer
#    paginate_by = 40

# class JobListView(generic.ListView):
#    model = Job
#    paginate_by = 10

#    def get_queryset(self):
#        return Job.objects.filter(application_deadline__exact='')
