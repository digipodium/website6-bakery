from django.urls.conf import path
from .views import homeview

urlpatterns = [
    path('',homeview, name='home')
]