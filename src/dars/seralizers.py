from rest_framework.serializers import ModelSerializer
from .models import Universitet
from .models import Teacher

class UniversitetSerializer(ModelSerializer):

    class Meta:
        model = Universitet
        fields = ['id', 'name', 'is_active']

class TeacherSerializer(ModelSerializer):

    class Meta:
        model = Teacher
        fields = ['id', 'name', 'mutaxasislik', 'oylik']