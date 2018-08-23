from django.urls import include, path
from . import views
from rest_framework import routers

router = routers.DefaultRouter()

router.register('jobs', views.JobView)

urlpatterns = [
    path('', include(router.urls))
]