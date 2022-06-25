from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse

from .models import Resume
from .utils import render_to_pdf

# Create your views here.

class GenerateResume(View):
    """generate a pdf resume"""

    def get(self, request, pk, *args, **kwargs):
        """ view to generate a pdf invoice of customer orders """
        resume = Resume.objects.get(pk=pk)
        pdf = render_to_pdf('resume_builder/test_resume.html',
                            {'resume': resume})
        return HttpResponse(pdf, content_type='application/pdf')
