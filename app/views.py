from django.shortcuts import render,redirect
from app.models import User
from random import randint

# Create your views here.
def get_master(request):
     if request.method=='POST':
          fname=request.POST['firstname']
          lname=request.POST['lname']
          phone=request.POST['phone']
          subject=request.POST['subject']
          email=request.POST['email']
          message=request.POST['message']
          user_exist=User.objects.filter(email=email).exists()
          if not user_exist:
               otp=randint(1000,9999)
               
               user=User(first_name=fname,last_name=lname,phone=phone,email=email,subject=subject,message=message) 
               user.save()
               user_data=User.objects.get(email=email)
               request.session['user_id']=user_data.id
               
               return redirect('app:master')
          else:
               ms="User already exist"
     return render(request,"app/master.html") 


