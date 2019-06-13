

from django.contrib import messages
from django.contrib.auth import logout as AuthLogOut
from django.core.files.storage import FileSystemStorage
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import redirect, render
from django.template.context_processors import request
import hashlib
import random
import string
from models.models import *

# Create your views here.

def gen(request):
    Admin.objects.create(
        username="adminOne",
        password="cfa44e98e50114bac02bf1e465dcc687ba72467fc7bacb36898e59a1321166e6",
        secret="49'nv?42><",
        admintype=1,
        status=1,
        createdate='2019-05-08 10:48:34.343278+00')
    return redirect(login)

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
