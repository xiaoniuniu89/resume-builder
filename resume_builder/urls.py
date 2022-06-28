from django.urls import path
from .views import (
    GenerateResume,
    generate_cv
)

urlpatterns = [
    path('<int:pk>/', GenerateResume.as_view(), name='make_pdf'),
  
]