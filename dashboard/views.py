from django.shortcuts import render
from resume_builder.models import Resume

def dashboard(request):
    resumes = Resume.objects.filter(user=request.user)
    return render(request, 'dashboard/dashboard.html', {'resumes': resumes})
