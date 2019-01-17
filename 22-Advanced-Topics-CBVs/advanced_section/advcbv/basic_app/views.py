from django.shortcuts import render

from django.views.generic import View
from django.http import HttpResponse

class CBView(View):
    def get(self, request):
        return HttpResponse("Class Based View Are Cool!")


# Create your views here.
# def index(request):
#     return render(request, "/index.html", context={})
