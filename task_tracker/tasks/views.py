from django.shortcuts import render, redirect
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Project, Task, User, Comment
from .serializers import RegUserSerializer, ProjectSerializer, TaskSerializer, ProfileSerializer, CommentSerializer

# Create your views here.


class RegisterUser(APIView):
    def post(self, request):
        serializer = RegUserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
def Hello_ntest(request):
    return HttpResponse("Hello, it's test")

class ProjectsView(APIView):
    def get(self, request):
        if request.user.is_superuser:
            queryset = Project.objects.all()
            ser = ProjectSerializer(queryset, many=True)
            if queryset != None:
                return Response(ser.data)
            else:
                return HttpResponse('На данный момент нет созданных задач')
        elif request.user.is_authenticated:
            queryset = Project.objects.filter(team=request.user)
            ser = ProjectSerializer(queryset, many=True)
            if queryset != None:
                return Response(ser.data)
            else:
                return HttpResponse('Для вас нет проектов')
        else:
            return HttpResponse('Вы не вошли в систему! Пожалуйста пройдите аутентификацию')
    
    def post(self, request):
        if request.user.is_superuser:
            serializer = ProjectSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data)
        else:
            return HttpResponse('У вас недостаточно прав для выполнения данной операции')
    
class TasksView(APIView):
    def get(self, request):
        if request.user.is_authenticated:
            queryset = Task.objects.all()
            res = []
            for task in queryset:
                if task.executor == request.user or task.tester == request.user or request.user.is_superuser:
                    res.append(task)
            ser = TaskSerializer(res, many=True)
            if res != []:
                return Response(ser.data)
            else:
                return HttpResponse('Для вас нет задач')
        else:
            return HttpResponse('Вы не вошли в систему! Пожалуйста пройдите аутентификацию')
    
    def post(self, request):
        if request.user.is_superuser:
            serializer = TaskSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data)
        else:
            return HttpResponse('У вас недостаточно прав для выполнения данной операции')
    
class ProfileView(APIView):
    def get(self, request):
        queryset = User.objects.all()
        for user in queryset:
            if user == request.user:
                queryset2 = User.objects.filter(email=request.user).get()
                ser = ProfileSerializer(queryset2)
                return Response(ser.data)
        return HttpResponse('Вы не авторизованы, пожалуйста войдите в ваш аккаунт')
    
class CommentView(APIView):
    def get(self, request):
        if request.user.is_authenticated:
            queryset = Comment.objects.all()
            res=[]
            for com in queryset:
                if com.task.executor == request.user or com.task.tester == request.user or request.user.is_superuser:
                    res.append(com)
            ser = CommentSerializer(res, many=True)
            if res != []:
                return Response(ser.data)
            else:
                return HttpResponse('Нет коммантариев к вашим задачвм')
        else:
            return HttpResponse('Вы не вошли в систему! Пожалуйста пройдите аутентификацию')
        
    def post(self, request):
        # queryset = Comment.objects.all()
        # for com in queryset:
            # if com.task.executor == request.user or com.task.tester == request.user or request.user.is_superuser:
        if request.user.is_authenticated:
                serializer = CommentSerializer(data=request.data)
                serializer.is_valid(raise_exception=True)
                serializer.save()
                return Response(serializer.data)
        return HttpResponse('У вас недостаточно прав для выполнения данной операции')