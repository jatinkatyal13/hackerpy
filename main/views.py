from django.shortcuts import render
from django.views.generic import (
  TemplateView,
  ListView,
  DetailView,
  CreateView
)

from main import models

# Create your views here.
class Index(TemplateView):
  template_name = 'main/index.html'

class Contests(ListView):
  model = models.Contest
  template_name = 'main/contests.html'

class Contest(DetailView):
  model = models.Contest
  template_name = 'main/contest.html'

class ProblemCreate(CreateView):
  model = models.Problem
  template_name = 'main/problem_create.html'
  fields = '__all__'
  success_url = '/'

class Problem(DetailView):
  template_name = 'main/problem.html'

  def get_queryset(self):
    return models.Contest.objects.get(id = self.kwargs['contest_id']).problems
