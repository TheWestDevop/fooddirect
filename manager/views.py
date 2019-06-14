

import hashlib
import random
import string

from django.contrib import messages
from django.contrib.auth import logout as AuthLogOut
from django.core.exceptions import ObjectDoesNotExist
from django.core.files.storage import FileSystemStorage
from django.shortcuts import redirect, render
from django.template.context_processors import request

from models.models import *

# Create your views here.


#Product
def listProduct(request):
    if request.session.has_key('token'):
       products = Product.objects.all().order_by("-id")
       return render(request,'manager/dashboard.html',{'products': products}) 
    else:
       return redirect(login)

def createProduct(request):
    if request.session.has_key('token'):
        products = Product.objects.all().order_by("-id")
        if request.method == "POST":
            name = request.POST.get('name')
            description = request.POST.get('description')
            weight = request.POST.get('weight')
            unit = request.POST.get('unit') 
            price = request.POST.get('price')
            priceper = request.POST.get('priceper')
            perunit  = request.POST.get('unit')
            aisle = request.POST.get('aisle')
            category = request.POST.get('category')
            img = request.FILES['img']
            fs = FileSystemStorage()
            imgname = fs.save(img.name.strip(), img)
            iconid = request.POST.get('iconid')
            color = request.POST.get('color')
            
            
            Product.objects.create(
                        name=name,
                        description=description,
                        weight=weight,
                        unit=unit,
                        price=price,
                        priceper=priceper,
                        aisle=aisle,
                        category=category,
                        img=imgname,
                        iconid=iconid,
                        color=color,
                        searchitem='',
                        searchstrength=0
                        )
            
            return redirect(listProduct)
        return redirect(listProduct)
            
    else:
       return redirect(login)
    
def editProduct(request,id):
    if request.session.has_key('token'):
       product =  Product.objects.get(id=id)
       if request.method == "POST":
           product.name = request.POST.get('name')
           product.description = request.POST.get('description')
           product.weight = request.POST.get('weight')
           product.unit = request.POST.get('unit') 
           product.price = request.POST.get('price')
           product.priceper = request.POST.get('priceper')
           product.perunit  = request.POST.get('unit')
           product.aisle = request.POST.get('aisle')
           product.category = request.POST.get('category')
           img = request.FILES['img']
           fs = FileSystemStorage()
           imgname = fs.save(img.name.strip(), img)
           product.img = imgname
           product.iconid = request.POST.get('iconid')
           product.color = request.POST.get('color')
           product.save()
           return redirect(listProduct) 
       
       else:
        return render(request,'manager/editProduct.html',{'product':product})
    else:
        return redirect(login)

def deleteProduct(request,id):
     if request.session.has_key('token'):
          product =Product.objects.get(id=id)
          product.delete()
          return redirect(listProduct)  
     else:
            return redirect(login)

#Order
def listOrder(request):
    if request.session.has_key('token'):
       orders = Orders.objects.all().order_by("-id")
       return render(request,'manager/orders.html',{'orders': orders}) 
    else:
       return redirect(login)

#Deliveries
def listDeliveries(request):
    if request.session.has_key('token'):
       deliveries = Deliveries.objects.all().order_by("-id")
       return render(request,'manager/deliveries.html',{'deliveries': deliveries}) 
    else:
       return redirect(login)

#Admin crud 
def createAdmin(request):
      if request.session.has_key('token'):
        products = Product.objects.all().order_by("-id")
        if request.method == "POST":
            username = request.POST.get('username')
            plainpassword= request.POST.get('password')
            secret = secretGenerator()
            admintype = request.POST.get('admintype') 
            
            password = hashPassword(plainpassword+secret)
            
            Admin.objects.create(
              username=username,
              password=password,
              secret=secret,
              admintype=admintype,
              status=0)
            
            return redirect(listAdmin)
        return redirect(listAdmin)
            
      else:
       return redirect(login)

def listAdmin(request):
    if request.session.has_key('token'):
       admins = Admin.objects.all().order_by("-id")
       return render(request,'manager/admin.html',{'admins': admins}) 
    else:
       return redirect(login)

def deleteAdmin(request,id):
     if request.session.has_key('token'):
          admin = Admin.objects.get(id=id)
          admin.delete()
          return redirect(listAdmin)  
     else:
            return redirect(login)


#User crud
def createUser(request):
      if request.session.has_key('token'):
        products = Product.objects.all().order_by("-id")
        if request.method == "POST":
            username = request.POST.get('username')
            plainpassword= request.POST.get('password')
            secret = secretGenerator()
            usertype = request.POST.get('usertype') 
            
            password = hashPassword(plainpassword+secret)
            
            User.objects.create(
              username=username,
              password=password,
              secret=secret,
              usertype=usertype
              )
            
            return redirect(listUser)
        return redirect(listUser)
            
      else:
       return redirect(login)

def listUser(request):
    if request.session.has_key('token'):
       users = User.objects.all().order_by("-id")
       return render(request,'manager/users.html',{'users': users}) 
    else:
       return redirect(login)

def deleteUser(request,id):
     if request.session.has_key('token'):
          user =User.objects.get(id=id)
          user.delete()
          return redirect(listUser)  
     else:
            return redirect(login)


#Log in and Log out Authentication
def login(request):
     return render(request,'manager/sign_in.html',{})
 
def logout(request):
     AuthLogOut(request)
     msg = "You Have successfully log out"
     messages.success(request,msg,extra_tags="success")
     return redirect(login)

def auth(request):
    if request.method == 'POST':
           username      = request.POST.get('username')
           plainpassword = request.POST.get('password')
    try :   
            user = Admin.objects.get(username=username)

            secret = user.secret
           
            passwordConfirm = hashPassword(plainpassword+secret)
            if User.objects.filter(username=username).count()>1:
                 errormsg = "Multiple Account Found"
                 messages.error(request,errormsg)
                 return redirect(login)

            if passwordConfirm == user.password :
              request.session['token'] = user.secret
              return redirect(listProduct)
              pass
        
            else:
               errormsg = "Invalid Username or Password"
               messages.error(request,errormsg)
               return redirect(login)
               pass
    except ObjectDoesNotExist:

               errormsg = " Username Does Not Exist"
               messages.error(request,errormsg)
               return redirect(login)
               pass

    else:
         return redirect(login)

def secretGenerator():
    letters = string.ascii_lowercase + string.digits + string.punctuation
    return ''.join(random.choice(letters) for i in range(10))

def hashPassword(word):
    password = hashlib.sha256(word.encode()).hexdigest()
    return password
