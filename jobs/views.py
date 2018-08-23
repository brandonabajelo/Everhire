from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import Job
from .serializers import JobSerializer


class JobView(viewsets.ModelViewSet):
    queryset = Job.objects.all()
    serializer_class = JobSerializer


