from rest_framework import routers
from .views import *
from django.urls import path, include

router = routers.DefaultRouter()
router.register('study-centers', StudyCenterViewSet)
router.register('users', UserViewSet)
router.register('social-statuses', SocialStatusViewSet)
router.register('courses', CourseViewSet)
router.register('certificates', CertificateViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('generate-certificate/<int:pk>', GenerateCertificate.as_view())
]