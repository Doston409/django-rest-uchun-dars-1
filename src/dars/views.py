from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Universitet
from .models import Teacher
from .seralizers import UniversitetSerializer
from .seralizers import TeacherSerializer


# Create your views here.

class UniversitetAPIView(APIView):
    def get (self, request):
        universitet = Universitet.objects.all()
        data = UniversitetSerializer(universitet,many=True).data
        return Response(data, status=status.HTTP_200_OK)
    
    def post(self,request):
        ser = UniversitetSerializer(data=request.data)
        if ser.is_valid(raise_exception=True):
            ser.save()
        return Response(ser.data, status=status.HTTP_201_CREATED)
    
class TeacherAPIView(APIView):
    def get (self, request):
        ustozlar = Teacher.objects.all()
        data = TeacherSerializer(ustozlar,many=True).data
        return Response(data, status=status.HTTP_200_OK)
    
    def post(self,request):
        ser = TeacherSerializer(data=request.data)
        if ser.is_valid(raise_exception=True):
            ser.save()
        return Response(ser.data, status=status.HTTP_201_CREATED)