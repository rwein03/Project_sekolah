from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Computer
from .serializers import ComputerSerializer
from rest_framework import status

@api_view(['GET', 'POST'])
def getData(request):
    if request.method == 'GET':
        computer = Computer.objects.all()
        serializer = ComputerSerializer(computer, many=True)
        return Response(serializer.data)
    
    if request.method == 'POST':
        serializer = ComputerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
