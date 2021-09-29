from django.shortcuts import render
from django.views import View
from django.contrib import messages
from.models import *
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

class WishlistView(View):
    def get(self,request):
        return render(request,'wishlist.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        phone = request.POST['phone']
        message = request.POST['message']
        Contact.objects.create(
        name=name,
        email=email,
        subject=subject,
        phone=phone,
        message=message,
        ),
        messages.add_message(request, messages.SUCCESS, 'Tabriklaymiz a\'loqa muofaqiyatli amalga oshirildi tez orada sayit adminlari sizbilan bog\'lanishadi')
        #bot.send_message(my_id,f"Aloqa xizmatidan xabar bor\nIsmi:  {name}\nTelfon raqami:  {phone}\nEmail:  {email}\n Xabari:  {message}")
    return render(request,'contact-us.html')

class ProfileView(View):
    def get(self,request):
        return render(request,'my-account.html')