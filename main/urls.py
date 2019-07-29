from django.urls import path
from django.contrib.auth.decorators import login_required

from main import views

urlpatterns = [
  path('', views.Index.as_view()),
  path('contests', views.Contests.as_view(), name = 'contests'),
  path('contests/<int:pk>', login_required(views.Contest.as_view()), name = 'contest'),
  path('contests/<int:contest_id>/problem/<int:pk>', login_required(views.Problem.as_view()), name = 'problem'),
  path('problem_create/', views.ProblemCreate.as_view())
]
