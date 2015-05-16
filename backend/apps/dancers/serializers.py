from rest_framework import serializers
from models import *

class ParentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parent


class StudentIntakeFormSerializer(serializers.ModelSerializer):
     class Meta:
        model = StudentIntakeForm
