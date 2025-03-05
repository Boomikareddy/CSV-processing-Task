from django.urls import path
from .views import upload_csv  # Import your views

urlpatterns = [
    path('', upload_csv, name='upload_csv'),  # This makes /csv/ work
    path('upload/', upload_csv, name='upload_csv'),  # Keep this if needed
]
