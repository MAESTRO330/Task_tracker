from rest_framework import serializers
from .models import User, Project, Task, Comment

class RegUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'user_avatar', 'user_role', 'user_position', 'password']
        extra_kwargs = {'user_avatar':{'default':'avatars\\Login_default_Avatar.png'}}

    def create(self, validated_data):
        user = User.objects.create(first_name=validated_data['first_name'], last_name=validated_data['last_name'], username=validated_data['username'], email=validated_data['email'], user_avatar=validated_data['user_avatar'], user_role=validated_data['user_role'], user_position=validated_data['user_position'])
        user.set_password(validated_data['password'])
        user.save()
        return user
    
class ProjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = Project
        fields = '__all__'

    def create(self, validated_data):
        project = Project.objects.create(title=validated_data['title'], description=validated_data['description'], deadline=validated_data['deadline'])
        project.team.add(*validated_data['team'])
        project.save()
        return project

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'

    def create(self, validated_data):
        task = Task.objects.create(title=validated_data['title'], description=validated_data['description'], project=validated_data['project'], executor=validated_data['executor'], status=validated_data['status'], priority=validated_data['priority'], deadline=validated_data['deadline'], tester=validated_data['tester'])
        task.save()
        return task
    
class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ['password', 'is_superuser', 'is_staff', 'is_active', 'date_joined', 'groups', 'user_permissions']

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"

    def create(self, validated_data):
        comment = Comment.objects.create(author=validated_data['author'], message=validated_data['message'], task=validated_data['task'])
        comment.save()
        return comment