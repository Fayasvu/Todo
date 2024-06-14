from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from api.serializer import *
from rest_framework.viewsets import ViewSet,ModelViewSet
from rest_framework import authentication,permissions
from work.models import *


class userregister(APIView):

    def post(self,request,*args,**kwargs):
        # qs=User.objects.all()
        serializer=userregistration(data=request.data)
        if serializer.is_valid():
            serializer.save()

        return Response(serializer.data)


class todoviewset(ViewSet):

    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[permissions.IsAuthenticated]

    def list(self,request,*args,**kwargs):
        qs=Taskmodel.objects.all()
        serializer=todoserializer(qs,many=True)

        return Response(serializer.data)
    
    def create(self,request,*args,**kwargs):
        serializer=todoserializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)

        return Response(serializer.data)
    
    def update(self,request,*args,**kwargs):
        id=kwargs.get('pk')
        qs=Taskmodel.objects.get(id=id)
        serializer=todoserializer(data=request.data,instance=qs)
        if serializer.is_valid():
            serializer.save(request.user)

            return Response(serializer.data)
    
    def retrieve(self,request,*args,**kwargs):
        id=kwargs.get('pk')
        qs=Taskmodel.objects.get(id=id)
        serializer=todoserializer(qs)
        
        return Response(serializer.data)
    
    def destroy(self,request,*args,**kwargs):
        id=kwargs.get('pk')
        qs=Taskmodel.objects.get(id=id)
        if qs.user==request.user:
            qs.delete()
            return Response({"message":'Todo object deleted'})
        else:
            raise serializers.ValidationError("not allowed")
           #return Responce({"message":"not allowed"})


class todomodelviewset(ModelViewSet):

    queryset=Taskmodel.objects.all()
    serializer_class=todoserializer
    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[permissions.IsAuthenticated]

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)


    def get_queryset(self):
        return Taskmodel.objects.filter(user=self.request.user)
    
    def perform_update(self, serializer):
        return super().perform_update(serializer)

    def perform_destroy(self, instance):
        instance=Taskmodel.objects.get(id=id)
        if instance.user==self.request.user:
            return instance.delete()
         

            
        



    





