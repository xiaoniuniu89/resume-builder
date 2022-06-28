from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse

from django.conf import settings
# from easy_pdf.views import PDFTemplateResponseMixin
from django.views.generic import DetailView

from .models import Resume
from .utils import render_to_pdf

from wkhtmltopdf.views import PDFTemplateView


# Create your views here.

class GenerateResume(PDFTemplateView):
    """generate a pdf resume"""

    template_name = 'resume_builder/cthulhu.html'
    cmd_options = {
        'margin-top': 3,
    }
    
    def get_context_data(self, pk, **kwargs):
        context = super().get_context_data(**kwargs)
        context["resume"] = Resume.objects.get(pk=pk)
        return context
    
    
    
        
        
        
        
def generate_cv(request, pk):
    resume = Resume.objects.get(pk=pk)
    pdf = render_to_pdf('resume_builder/plain_feather.html',
                        {'resume': resume})
    return HttpResponse(pdf, content_type='application/pdf')
