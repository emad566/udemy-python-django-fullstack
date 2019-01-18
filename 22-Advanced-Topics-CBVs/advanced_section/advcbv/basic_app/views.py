from django.shortcuts import render
from django.views.generic import View, TemplateView, ListView, DetailView
from . import models
# from django.http import HttpResponse

class IndexView(TemplateView):
    template_name = 'index.html'

class SchoolListView(ListView):
    # default template_name = 'school_list'
    # If it commented will be sended as school_list
    # template_name = 'basic_app/school_list.html'
    context_object_name = 'schools'
    model = models.School

class SchoolDetailsView(DetailView):
    # default template_name = 'school_detail'
    # If it commented will be sended as schools
    # template_name = 'basic_app/school_detail.html'
    context_object_name = 'school_detail'
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
