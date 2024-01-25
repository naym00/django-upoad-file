from rest_framework.decorators import api_view
from rest_framework.response import Response
from myapp.models import Uploadfile
from rest_framework import status
from myapp.serializers import UploadfileSerializer

@api_view(['GET'])
def getFiles(request):
    uploadfiles = Uploadfile.objects.all()
    uploadfileserializer = UploadfileSerializer(uploadfiles, many=True)

    return Response(uploadfileserializer.data, status=status.HTTP_200_OK)

@api_view(['POST'])
def uploadFile(request):
    file = request.FILES.get('file')
    strfilename = str(file)

    if '.pdf' in strfilename[len(strfilename)-4:]:
        name = request.data.get('name')
        Uploadfile.objects.create(name=name, file=file)
        return Response({'message': 'File Saved!'}, status=status.HTTP_200_OK)
    else: return Response({'message': 'Only pdf files are allowed!'}, status=status.HTTP_400_BAD_REQUEST)
