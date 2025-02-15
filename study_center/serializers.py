from rest_framework import serializers
from .models import StudyCenter, CustomUser, SocialStatus, Course, Certificate

class StudyCenterSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudyCenter
        fields = ('id', 'name', 'manager', 'contact_number', 'location','address','longitude','latitude',)

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'full_name', 'email', 'password', 'photo', 'phone_number','is_manager',)
        write_only_fields  = ('password',)
        extra_kwargs ={
            'password':{'write_only': True}
        }

class SocialStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialStatus
        fields = ('id', 'name', 'slug',)

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ('id', 'name', 'image', 'social_status',)

class CertificateSerializer(serializers.ModelSerializer):
    social_status = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Certificate
        fields = ('id', 'name', 'social_status', 'birthdate', 'contact_number', 'course', 'gender')
    