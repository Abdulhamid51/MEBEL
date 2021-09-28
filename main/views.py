from django.shortcuts import render
from django.views import View
# Create your views here.

class HomeView(View):
    def get(self,request):
        return render(request,'index-2.html')


class AccountView(View):
    def get(self,request):
        return render(request,'my-account.html')