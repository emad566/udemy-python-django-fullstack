from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import View, TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import School
# from django.http import HttpResponse

class IndexView(TemplateView):
    template_name = 'index.html'

class SchoolListView(ListView):
    # default template_name = 'school_list'
    # If it commented will be sended as school_list
    # template_name = 'basic_app/school_list.html'
    context_object_name = 'schools'
    model = School

class SchoolDetailsView(DetailView):
    # default template_name = 'school_detail'
    # If it commented will be sended as schools
    # template_name = 'basic_app/school_detail.html'
    context_object_name = 'school_detail'
    model = School

class SchoolCreateView(CreateView):
    fields = ('name', 'principal', 'location')
    model = School

class SchoolUpdateView(UpdateView):
    model = School
    fields = ('name', 'principal')

class SchoolDeleteView(DeleteView):
    model = School
    success_url = reverse_lazy('basic_app:list')

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
