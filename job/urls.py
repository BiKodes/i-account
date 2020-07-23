from django.urls import path, re_path
from . import views


urlpatterns = [
    path('',views.home_view, name='home'),
    path('jobs/',views.job_list_view, name='jobs'),
    path('contact/',views.contact, name='contact'),
    # path('job/<int:pk>',views.JobDetailView.as_view(), name='job-detail'),


    path('employers_list/',views.employer_list_view, name='employers_list'),
    path('register_employer/',views.register_employer, name="register_employer"),
    re_path(r'^employer_detail/(?P<id>\d+)/$',views.employer_detail_view, name='employer_detail'),


    path('jobs_list/',views.job_list_view,name='jobs_list'),
    path('register_job/',views.post_job,name="register_job"),
    re_path(r'^job_detail/(?P<id>\d+)/$',views.job_detail_view, name='job_detail'),

    path('applicants_list/',views.applicant_list_view, name='applicants_list'),
    path('register_applicant/',views.register_applicant, name='register_applicant'),
    re_path(r'^applicant_detail/(?P<id>\d+)/$',views.applicant_detail_view, name='applicant_detail'),


    path('qualifications_list/',views.qualification_list_view, name='qualifications_list'),
    path('qualification/',views.submit_qualification, name='qualification'),
    re_path(r'^qualification_detail/(?P<id>\d+)$',views.qualification_detail_view, name='qualification_detail'),


    path('experiences_list/',views.experience_list_view, name='experiences_list'),
    path('experience/',views.submit_experience, name='experience'),
    re_path(r'^experience_detail/(?P<id>\d+)$',views.experience_detail_view, name='experience_detail'),


    path('cover_letters_list/',views.cover_letter_list_view, name='cover_letters_list'),
    path('cover_letter/',views.attach_cover_letter, name='cover_letter'),
    re_path(r'^cover_letter_detail/$',views.cover_letter_detail_view, name='cover_letter_detail'),


    path('referees_list/',views.referee_list_view, name='referees_list'),
    path('referee/',views.submit_referee, name='referee'),
    re_path(r'^referee_detail/(?P<id>\d+)$',views.referee_detail_view, name='referee_detail'),


    path('employer/create/', views.EmployerCreateView.as_view(), name='employer_create'),
    path('employer/<int:pk>/update/', views.EmployerUpdateView.as_view(), name='employer_update'),
    path('employer/<int:pk>/delete/', views.EmployerDeleteView.as_view(), name='employer_delete'),

    path('job/create/', views.JobCreateView.as_view(), name='job_create'),
    path('job/<int:pk>/update/', views.JobUpdateView.as_view(), name='job_update'),
    path('job/<int:pk>/delete/', views.JobDeleteView.as_view(), name='job_delete'),

    path('applicant/create/', views.applicant_create_view, name='applicant_create'),
    path('applicant/<int:pk>/update/', views.applicant_update_view, name='applicant_update'),
    path('applicant/<int:pk>/delete/', views.applicant_delete_view, name='applicant_delete'),

    path('qualification/create/', views.qualification_create_view, name='qualification_create'),
    path('qualification/<int:pk>/update/', views.qualification_update_view, name='qualification_update'),
    path('qualification/<int:pk>/delete/', views.qualification_delete_view, name='qualification_delete'),

    path('experience/create/', views.experience_create_view, name='experience_create'),
    path('experience/<int:pk>/update/', views.experience_update_view, name='experience_update'),
    path('experience/<int:pk>/delete/', views.experience_delete_view, name='experience_delete'),

    path('cover_letter/create/', views.Cover_LetterCreateView.as_view(), name='cover_letter_create'),
    path('cover_letter/<int:pk>/update/', views.Cover_LetterUpdateView.as_view(), name='cover_letter_update'),
    path('cover_letter/<int:pk>/delete/', views.Cover_LetterDeleteView.as_view(), name='cover_letter_delete'),

    path('referee/create/', views.RefereeCreateView.as_view(), name='referee_create'),
    path('referee/<int:pk>/update/', views.RefereeUpdateView.as_view(), name='referee_update'),
    path('referee/<int:pk>/delete/', views.RefereeDeleteView.as_view(),name='referee_delete'),



]
