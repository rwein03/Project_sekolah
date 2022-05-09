from django.http import Http404
from requests import request
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Computer, request_action 
from .serializers import ComputerSerializer, actionSerializer
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from django_filters import rest_framework as filters


#Generics
class ComputerFilter(filters.FilterSet):
    class Meta:
        model = Computer
        fields = '__all__'

class userComputer(generics.ListAPIView):
    serializer_class = ComputerSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Computer.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_class = ComputerFilter

class actionFilter(filters.FilterSet):
    class Meta:
        model: request_action
        fields = '__all__'
        
class getAction(generics.ListAPIView):
    serializer_class =  actionSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = request_action.objects.all()
    filter_backend = [DjangoFilterBackend]
    # filterset_class = actionFilter
    filterset_fields = ['isStatus']

#using API VIEW
class listData(APIView):
    # authentication_classes = [SessionAuthentication, BasicAuthentication]
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    
    def get(self, request, format=None):
        computer = Computer.objects.all()
        serializer = ComputerSerializer(computer, many= True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = ComputerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

#APIView Action
class actionData(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    
    def get(self, request, format=None):
        action = request_action.objects.all()
        serializer = actionSerializer(action, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = actionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class detailAction(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    
    def get_object(self, pk):
        try:
            action = request_action.objects.get(id=pk)
            return action
        except Computer.DoesNotExist:
            raise Http404
    
    def get(self, request, pk, format= None):
        action = self.get_object(pk)
        serializer = actionSerializer(action)
        return Response(serializer.data)
    
    def put(self, request, pk, format=None):
        action = self.get_object(pk)
        serializer = actionSerializer(action, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None):
        action = self.get_object(pk)
        action.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class listDataDetail(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    
    def get_object(self, mac):
        try:
            computer = Computer.objects.get(mac_addr=mac)
            return computer
        except Computer.DoesNotExist:
            raise Http404
    
    def get(self, request, mac, format= None):
        computer = self.get_object(mac)
        serializer = ComputerSerializer(computer)
        return Response(serializer.data)
    
    def put(self, request, mac, format=None):
        computer = self.get_object(mac)
        serializer = ComputerSerializer(computer, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, mac, format=None):
        computer = self.get_object(mac)
        computer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


#using Regular procedure
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

@api_view(['GET','PUT','DELETE'])
def data_detail(request, id_data):
    print(request.method)
    try:
        computer = Computer.objects.get(id=id_data)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method=='GET':
        serializer = ComputerSerializer(computer)
        return Response(serializer.data)
    
    if request.method == 'PUT':
        serializer = ComputerSerializer(computer, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        computer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        