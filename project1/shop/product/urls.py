from django.urls import path
from .views import register1

urlpatterns = [
    path('', register1, name='home'),  # Define the root URL pattern
    path('reg/', register1, name='register1'),
]
