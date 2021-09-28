from django.shortcuts import render
from django.views import View
# Create your views here.

class HomeView(View):
    def get(self,request):
        return render(request,'index-2.html')

class CatalogView(View):
    def get(self,request):
        return render(request,'shop.html')

class AboutView(View):
    def get(self,request):
        return render(request,'about-us.html')


class BlogView(View):
    def get(self,request):
        return render(request,'blog.html')

class RegisterctView(View):
    def get(self,request):
        return render(request,'login-register.html')

class ProfileView(View):
    def get(self,request):
        return render(request,'my-account.html')