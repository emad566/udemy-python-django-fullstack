from django.shortcuts import render

from django.views.generic import View, TemplateView, ListView, DetailView
from . import models
# from django.http import HttpResponse

class SchoolListView(ListView):
    model = models.School

class SchoolDetailsView(DetailView):
    model = models.School


# class IndexView(TemplateView):
#     template_name = 'index.html'

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['injectme'] = 'Basic Injaction'
#         return context

# class CBView(View):
#     def get(self, request):
#         return HttpResponse("Class Based View Are Cool!")


# Create your views here.
# def index(request):
#     return render(request, "/index.html", context={})
