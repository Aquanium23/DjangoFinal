from rest_framework import serializers
from core.models import Job, Contact, JobApplication
from django.contrib.auth.models import User as DjangoUser
from account.models import User, UserProfile

class JobModelSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Job
        fields = ['title', 'description', 'category', 'application_deadline', 'is_active']

    def get_fields(self):
        fields = super().get_fields()
        return fields

class ContactModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Contact
        fields = ['name', 'email', 'phone_number', 'message']

    def get_fields(self):
        fields = super().get_fields()
        return fields

class JobApplicationModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = JobApplication
        fields = ['job_id', 'status', 'created_at', 'updated_at']

    def get_fields(self):
        fields = super().get_fields()
        return fields

class UserModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'account_activated', 'password']

        def get_fields(self):
            fields = super().get_fields()
            return fields

class UserProfileModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ["profile_picture", "resume", "address", "phone_number", "about_me"]