from msilib.schema import AdminExecuteSequence
from rest_framework import routers
from .views import RatingViewSets

router = routers.DefaultRouter()
router.register('rating', RatingViewSets)

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
