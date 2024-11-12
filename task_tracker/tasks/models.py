from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    BACK = 'BACK'
    FRONT = 'FRONT'
    DO = 'DO'
    AL = 'AL'
    PM = 'PM'
    DG = 'DG'
    QA = 'QA'

    JS = 'JS'
    S = 'S'
    LS = 'LS'
    CS = 'CS'
    SS = 'SS'

    role_choices = {
        BACK: 'Разработчик Backend',
        FRONT: 'Разработчик Frontend',
        DO: 'DevOps',
        AL: 'Аналитик',
        PM: 'Project Mananger',
        DG: 'Дизайнер',
        QA: 'QA Тестировщик'
    }

    position_choices = {
        JS: 'Младший специалист',
        S: 'Специалист',
        LS: 'Ведущий специалист',
        CS: 'Главный специалист',
        SS: 'Старший специалист'
    }

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=80)
    username = models.CharField(max_length=150, unique=True)
    user_email = models.EmailField()
    user_avatar = models.ImageField(upload_to='avatars/')
    user_role = models.CharField(choices=role_choices, max_length=5)
    user_position = models.CharField(choices=position_choices, max_length=5)
    # current_projects = models.ForeignKey(Project, on_delete=models.CASCADE)
    # archive_projects = models.ForeignKey(Project, on_delete=models.CASCADE)

class Project(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    date_create = models.DateField(auto_now_add=True)
    date_update = models.DateField(auto_now=True)
    deadline = models.DateTimeField()
    team = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.BooleanField(default=False)

class Task(models.Model):
    GM = 'GM'
    IP = 'IP'
    DV = 'DV'
    DN = 'DN'

    LW = 'LW'
    MD = 'MD'
    HG = 'HG'

    status_choices = {
        GM: 'Grooming',
        IP: 'In Progress',
        DV: 'Dev',
        DN: 'Done',
    }

    prioriy_choices = {
        LW: 'Низкий',
        MD: 'Средний',
        HG: 'Высокий',
    }

    title = models.CharField(max_length=150)
    description = models.TextField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    executor = models.ForeignKey(User, on_delete=models.CASCADE) #Исполнитель
    status = models.CharField(choices=status_choices, max_length=5)
    priority = models.CharField(choices=prioriy_choices, max_length=5)
    date_create = models.DateField(auto_now_add=True)
    date_update = models.DateField(auto_now=True)
    deadline = models.DateTimeField()
    tester = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tester')
    # comment = models.TextField(null=True, blank=True)

    def new_comment(self, data):
        new_comment = Comment()
        # new_comment.Author =
        new_comment.Message = data['message']
        new_comment.task = self
        new_comment.save()

class Comment(models.Model):
    Author = models.ForeignKey(User, on_delete=models.CASCADE)
    Message = models.TextField()
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    date_time = models.DateTimeField(auto_now_add=True)