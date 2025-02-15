from rest_framework import viewsets
from rest_framework.views import APIView, Response, status
from .models import StudyCenter, CustomUser, Course, Certificate, SocialStatus
from .serializers import StudyCenterSerializer, UserSerializer, CertificateSerializer, SocialStatusSerializer, CourseSerializer
from .cerificate_generator import Certificates

# Create your views here.
class StudyCenterViewSet(viewsets.ModelViewSet):
    queryset = StudyCenter.objects.filter(active=True)
    serializer_class = StudyCenterSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.filter(active=True)
    serializer_class = UserSerializer

class SocialStatusViewSet(viewsets.ModelViewSet):
    queryset = SocialStatus.objects.filter(active=True)
    serializer_class = SocialStatusSerializer

class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.filter(active=True)
    serializer_class = CourseSerializer

class CertificateViewSet(viewsets.ModelViewSet):
    queryset = Certificate.objects.filter(active=True)
    serializer_class = CertificateSerializer

class GenerateCertificate(APIView):
    def post(self, request, *args, **kwargs):
        import urllib.parse
        pk = kwargs.get('pk')
        course = CourseSerializer(Course.objects.get(id=pk)).data
        url = Certificates.generateCertificate(urllib.parse.unquote(course.get('image')), request.POST.get('text'), int(request.POST.get('x')), int(request.POST.get('y')), int(request.POST.get('size')), int(request.POST.get('thickness')))
        return Response({'url':url}, status=status.HTTP_200_OK)