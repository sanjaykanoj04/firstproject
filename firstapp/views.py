from rest_framework import viewsets
from rest_framework import permissions
from .models import TutorReg
from firstapp.serializers import FirstappSerializer 

class FirstappViewSet(viewsets.ModelViewSet):
    queryset = TutorReg.objects.all()
    serializer_class = FirstappSerializer
