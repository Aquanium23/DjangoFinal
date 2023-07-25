from django.shortcuts import render, redirect, get_object_or_404
from rest_framework.generics import ListCreateAPIView, UpdateAPIView, ListAPIView, CreateAPIView, GenericAPIView, \
    RetrieveUpdateAPIView
from core.models import Job, Contact, JobApplication
from .serializers import JobModelSerializer, ContactModelSerializer, JobApplicationModelSerializer, UserModelSerializer, \
    UserProfileModelSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated
from .permissions import IsSuperAdmin
from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from rest_framework.response import Response
from account.models import User, UserProfile
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse
from commons.utils import send_account_activation_mail, is_profile_complete
from account.models import UserAccountActivationKey


class JobListView(ListAPIView):
    queryset = Job.objects.all()
    serializer_class = JobModelSerializer
    permission_classes = [AllowAny, ]

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context["title"]: "List Jobs"
        return context


class JobCreateView(ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = JobModelSerializer
    permission_classes = [IsSuperAdmin, ]

    def get_permissions(self):
        if self.action == "create":
            return [IsSuperAdmin(), ]
        return [IsAuthenticated(), ]

    def get_queryset(self):
        return Job.objects.all()

    def create_job(self, *args, **kwargs):
        create_jobs = Job.objects.filter()
        serializer = self.get_serializer(create_jobs, many=True)
        return Response(serializer.data)


class JobUpdateView(UpdateAPIView):
    queryset = Job.objects.all()
    serializer_class = JobModelSerializer
    permission_classes = [IsSuperAdmin, ]


class ContactListView(ListAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactModelSerializer
    permission_classes = [IsAuthenticated, ]

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context["title"]: "List Contacts"
        return context


class ContactCreateView(ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactModelSerializer
    permission_classes = [IsAuthenticated, ]

    def get_permissions(self):
        if self.action == "create":
            return [IsAuthenticated(), ]

    def get_queryset(self):
        return Contact.objects.all()

    def create_contacts(self, *args, **kwargs):
        create_contacts = Contact.objects.filter()
        serializer = self.get_serializer(create_contacts, many=True)
        return Response(serializer.data)


class MyJobListView(ModelViewSet):
    queryset = JobApplication.objects.all()
    serializer_class = JobApplicationModelSerializer
    permission_classes = [IsAuthenticated, ]

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context["title"]: "View Applied Jobs"
        return context

    @action(detail=True)
    def job_application(self, *args, **kwargs):
        my_jobs = Student.objects.filter()
        serializer = self.get_serializer(my_jobs, many=True)
        return Response(serializer.data)


class JobApply(ListCreateAPIView):
    queryset = JobApplication.objects.all()
    serializer_class = JobApplicationModelSerializer
    permission_classes = [IsAuthenticated, ]

    def perform_create(self, serializer):
        job_id = self.request.data.get('job')
        job = Job.objects.get(pk=job_id)
        serializer.save(user=self.request.user, job=job)


class ViewAppliedJobs(ListAPIView):
    serializer_class = JobApplicationModelSerializer
    permission_classes = [IsAuthenticated, ]

    def get_queryset(self):
        user = self.request.user
        return JobApplication.objects.filter(user=user)


class UserRegisterView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserModelSerializer
    permission_classes = [AllowAny, ]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            user.set_password(user.password)
            user.save()
            send_account_activation_mail(request, user)

            return Response(serializer.data)
        return Response(serializer.errors)


class UserVerificationView(GenericAPIView):
    permission_classes = [AllowAny, ]

    def get(self, request, user_id):
        user = get_object_or_404(User, pk=user_id)
        if not user.is_active():
            user.account_activated = True
            user.save()
            return Response('User Verified!')
        else:
            return Response('User not Found!')


class UserProfileCreateView(CreateAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileModelSerializer
    permission_classes = [IsAuthenticated, ]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class UserProfileUpdateView(RetrieveUpdateAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileModelSerializer
    permission_classes = [IsAuthenticated, ]

    def get_object(self):
        return UserProfile.objects.get(user=self.request.user)
