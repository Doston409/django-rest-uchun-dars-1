from rest_framework.serializers import ModelSerializer
from .models import Universitet
from .models import Teacher
from .models import Student
from .models import Group

class UniversitetSerializer(ModelSerializer):

    class Meta:
        model = Universitet
        fields = ['id', 'name', 'is_active']

class TeacherSerializer(ModelSerializer):

    class Meta:
        model = Teacher
        fields = ['id', 'name', 'mutaxasislik', 'oylik']


class StudentSerializer(ModelSerializer):

    class Meta:
        model = Student
        fields = ['id', 'name', 'age', 'is_active','address']


class GroupSerializer(ModelSerializer):

    class Meta:
        model = Group
        fields = ['id', 'name', 'universitet', 'students','teacher','is_active']