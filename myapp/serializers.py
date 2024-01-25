from rest_framework import serializers
from myapp.models import Uploadfile

class UploadfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Uploadfile
        fields = '__all__'