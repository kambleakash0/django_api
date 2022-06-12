from django.shortcuts import render
from rest_framework import viewsets
from .models import Repo
from .serializers import RepoSerializer

# Create your views here.
class RepoView(viewsets.ModelViewSet):
    queryset = Repo.objects.all()
    serializer_class = RepoSerializer