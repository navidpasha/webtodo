from django.shortcuts import render,redirect
from django.contrib.auth.models  import User
from django.contrib.auth import authenticate,login as auth_login,logout
from django.contrib import messages
# Create your views here.
from django.http import HttpResponse,HttpResponseRedirect
from home.models import todo as to
from home.form import *
from django.urls import reverse
from django.contrib.auth.decorators import login_required

@login_required
def todo(request):
    if request.method =='POST':
        task=request.POST.get('task')
        new_todo=to(user=request.user,todo_name=task)
        new_todo.save()
    all_todos=to.objects.filter(user=request.user)
    context={
        'todos':all_todos
    }
    return render(request,'todo.html',context)



def register(request):
    if request.user.is_authenticated:
        return redirect('todo')
    if request.method == 'POST':
        username = request.POST.get('username')
        try:
            user=User.objects.get(username=username)

            messages.error(request,f"{username}! username already exists,try another plzzz")
            return redirect('register')
        except:
            pass
        email=request.POST.get('email')
        password = request.POST.get('password')
        if len(password)<5:
            messages.error(request,"OOPS!password should be atleast 5 characters")
            return redirect('register')
        new_user=User.objects.create_user(username=username,email=email,password=password)
        new_user.save()
        messages.success(request,'Successfully created!Login now')
        return redirect('login')

    return render(request,'register.html')
def logout_view(request):
    logout(request)
    return redirect('login')

def login(request):
    if request.user.is_authenticated:
        return redirect('todo')
    if request.method == 'POST':
        username=request.POST.get("uname")
        password=request.POST.get("pass")


        validate_user= authenticate(username=username,password=password )
        if validate_user is not None:
            auth_login(request,validate_user)
            return redirect('todo')
        else:
            messages.error(request,"Error!user does not exist ,register now")
            return redirect('register')
    return render(request,'login.html')
@login_required
def delete_todo(request,name):
       dele = to.objects.get(user=request.user,todo_name=name)
       dele.delete()
       return redirect(reverse('todo'))
@login_required
def update(request,name):
    upd =to.objects.get(user=request.user,todo_name=name)
    upd.status=True
    upd.save()
    return redirect(reverse('todo'))

      
    
    

   


