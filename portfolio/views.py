from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth import authenticate, login, logout
from .forms import NewsFilterForm
import requests
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request,'index.html')

def contactHandler(request):
    if request.method=="POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject2 = request.POST.get('subject')
        message1 = request.POST.get('message')
        print(name)
        query = Contact(name=name,email=email,subject=subject2,message=message1)
        query.save()

        subject = 'THANK YOU FOR CONTACTING ME '
        message = f'Hi {name}, Thank you so much for reaching out to me. Your message brightened my day! '
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [email, ]
        send_mail( subject, message, email_from, recipient_list )

        
        subject1 = 'HELLOW SIR YOU GOT A NEW MAIL'
        message = f'Hi k satyanarayana chary,  Some one contacted you details are:- \n username - {name},\n  email - {email},\n subject - {subject2},\n message - {message1} \n'
        email_from = settings.EMAIL_HOST_USER
        recipient_list1 = ['charysatheesh4@gmail.com', ]
        send_mail( subject1, message, email_from, recipient_list1 )

        messages.success(request,"Thanks for contacting me ,I will look forward to utilize this oppertunity.....")
        return redirect('/contact/')
    
    return render(request, 'contact.html')

def logout_view(request):
    logout(request)
    return redirect('login')

def project(request):
    projects = Projects.objects.all()
    return render(request,'projects.html',{'projects':projects})

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request,'Youre logged in')
            return redirect('home')
        else:
            messages.success(request,'invalid creditials')
            return redirect('/login/')
    return render(request,"login.html")

def logout_user(request):
	logout(request)
	messages.success(request,('Youre now logged out'))
	return redirect('/')
    

def blogs(request):
    selected_category = request.GET.get('category')
    categories = Category.objects.all()
    posts = Post.objects.all()
    
    if selected_category:
        posts = posts.filter(cate_id=selected_category)
    
    return render(request, "blogs.html", {
        'categories': categories,
        'posts': posts,
        'selected_category': selected_category
    }) 

from django.shortcuts import get_object_or_404

def post_detail(request, url):
    post = get_object_or_404(Post, url=url)
    return render(request, 'post_detail.html', {'post': post})


