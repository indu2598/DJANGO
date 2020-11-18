from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from cruddjangoapp.models import Task
from cruddjangoapp.serializer import TaskSerializer

class MyTask(APIView):
    def post(self, request):
        print(request.data)
        newtask = TaskSerializer(data = request.data)
        if newtask.is_valid():
            newtask.save()
            return Response(newtask.data, status=201)
        return Response(newtask.errors , status= 400)

    def get(self,request):
        mytasks = Task.objects.all()
        task_serialize = TaskSerializer(mytasks, many = True)
        return Response(task_serialize.data)

class DeleteandUpdateTask(APIView):

    def get_data(self, pk):
        try: 
            return Task.objects.get(id=pk)
        except:
            return Response(status=404)

    def get(self,request,pk):
        empobj = self.get_data(pk)
        serialize = TaskSerializer(empobj)
        return Response(serialize.data)
    
    def put(self,request,pk):
        empobj = self.get_data(pk)
        serialize = TaskSerializer(empobj, data= request.data)
        if serialize.is_valid():
            serialize.save()
            return Response(serialize.data, status = 202)
        return Response(serialize.errors , status= 400)

    def delete(self,request,pk):
        taskobj = self.get_data(pk)
        taskobj.delete()
        return Response(status=204)


    
    
