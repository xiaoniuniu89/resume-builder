from django.urls import path
from .views import (
    GenerateResume,
)

urlpatterns = [
    path('<int:pk>/', GenerateResume.as_view(), name='make_pdf'),
  
]