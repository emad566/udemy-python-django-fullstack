from django.shortcuts import render
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import View, TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.http import HttpResponse
from . import forms


# Create your views here.
class IndexView(TemplateView):
    template_name = 'index.html'

class SignUp(CreateView):
    form_class = forms.UserCreateForm

    success_url = reverse_lazy('login')
    template_name = 'accounts/signuphtml'

