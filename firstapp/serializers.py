from .models import TutorReg
from rest_framework import serializers

class FirstappSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TutorReg
        fields = ['password', 'mobileno','fname']

      