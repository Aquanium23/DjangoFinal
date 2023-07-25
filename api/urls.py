from django.urls import path
from .views import JobListView, JobUpdateView, ContactListView, ContactCreateView, MyJobListView, JobCreateView, \
    JobApply, ViewAppliedJobs, UserRegisterView, UserVerificationView, UserProfileCreateView, UserProfileUpdateView
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token

router = DefaultRouter()
router.register("my-jobs", MyJobListView, basename="my_jobs")
router.register('job-create', JobCreateView, basename="create_jobs")
router.register('contacts', ContactCreateView, basename="create_contacts")

urlpatterns = [
                  path('', JobListView.as_view()),
                  path('update/<int:pk>/', JobUpdateView.as_view()),
                  path('login/', obtain_auth_token, name="api_login"),
                  path('contacts-list/', ContactListView.as_view(), name="list_contacts"),
                  path('job-apply/', JobApply.as_view(), name="job_apply"),
                  path('view-applied-jobs/', ViewAppliedJobs.as_view(), name="view_applied_jobs"),
                  path('register/', UserRegisterView.as_view(), name="user_register"),
                  path('verify/<int:user_id>/', UserVerificationView.as_view(), name="user_verify"),
                  path('create-profile/', UserProfileCreateView.as_view(), name="create_profile"),
                  path('update-profile/', UserProfileUpdateView.as_view(), name="update_profile"),
              ] + router.urls
