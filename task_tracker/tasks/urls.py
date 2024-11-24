from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import RegisterUser, Hello_ntest, ProjectsView, TasksView, ProfileView, CommentView

urlpatterns = [
    path('register', RegisterUser.as_view(), name='sign_up_page'),
    path('register/', RegisterUser.as_view(), name='sign_up_page'),
    path('login', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('login/refresh', TokenRefreshView.as_view(), name='token_refresh'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('', Hello_ntest, name='test_page'),
    path('projects', ProjectsView.as_view(), name='projects_page'),
    path('projects/', ProjectsView.as_view(), name='projects_page'),
    path('tasks', TasksView.as_view(), name='task_page'),
    path('tasks/', TasksView.as_view(), name='task_page'),
    path('profile', ProfileView.as_view(), name='profile_page'),
    path('profile/', ProfileView.as_view(), name='profile_page'),
    path('comments', CommentView.as_view(), name='comment_page'),
    path('comments/', CommentView.as_view(), name='comment_page'),
]