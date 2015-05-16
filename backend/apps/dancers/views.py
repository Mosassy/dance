from rest_framework import generics
from serializers import *
from models import *





# Create your views here.

class ParentListView(generics.ListAPIView):
    model = Parent
    serializer_class = ParentSerializer
    queryset = Parent.objects.all()

class StudentIntakeFormListView(generics.ListAPIView):
    model = StudentIntakeForm
    serializer_class = StudentIntakeFormSerializer
    queryset = StudentIntakeForm.objects.all()

