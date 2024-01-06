from django.shortcuts import render,redirect
from Shopapp.models import CategoryDb,ProductDb
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User
from Frontapp.models import ContactDb
from django.contrib import messages
# Create your views here.
def indexpage(request):
    return render(request, "index.html")

def categorypage(request):
    return render(request,"AddCategory.html")

def savecategory(request):
    if request.method == "POST":
        na = request.POST.get('name')
        des = request.POST.get('description')
        cimg = request.FILES['image']
        obj = CategoryDb(Category_Name=na, Description=des, Category_Image=cimg)
        obj.save()
        messages.success(request, "Category added successfully...!")
        return redirect(categorypage)

def category_display(request):
    cat = CategoryDb.objects.all()
    return render(request,'DisplayCategory.html',{'cat':cat})

def editcategory(request,dataid):
    cats = CategoryDb.objects.get(id=dataid)
    return render(request,"EditCategory.html",{'cats':cats})

def updatecategory(request,dataid):
    if request.method == "POST":
        cn = request.POST.get('name')
        des = request.POST.get('description')
        try:
            img = request.FILES['image']
            fs = FileSystemStorage()
            file = fs.save(img.name,img)
        except MultiValueDictKeyError:
            file = CategoryDb.objects.get(id=dataid).Category_Image
        CategoryDb.objects.filter(id=dataid).update(Category_Name=cn, Description=des, Category_Image=file)
        return redirect(category_display)

def deletecategory(request, dataid):
        cats = CategoryDb.objects.filter(id=dataid)
        cats.delete()
        return redirect(category_display)

def productpage(request):
    catdis = CategoryDb.objects.all()
    return render(request, "AddProduct.html", {'catdis':catdis})

def saveproduct(request):
    if request.method == "POST":
        cat = request.POST.get('categoryname')
        na = request.POST.get('name')
        des = request.POST.get('description')
        pri = request.POST.get('price')
        pimg = request.FILES['image']
        obj = ProductDb(Product_Category=cat, Product_Name=na, Description=des, Product_Price=pri, Product_Image=pimg)
        obj.save()
        messages.success(request, "Product added successfully...!")
        return redirect(productpage)

def product_display(request):
    prod = ProductDb.objects.all()
    return render(request,'DisplayProduct.html',{'prod':prod})
def editproduct(request,dataid):
    cat = CategoryDb.objects.all()
    prods = ProductDb.objects.get(id=dataid)
    return render(request,"EditProduct.html",{'cat':cat, 'prods':prods})
def updateproduct(request,dataid):
    if request.method == "POST":
        cp = request.POST.get('categoryname')
        nam = request.POST.get('name')
        des = request.POST.get('description')
        pri = request.POST.get('price')
        try:
            img = request.FILES['image']
            fs = FileSystemStorage()
            file = fs.save(img.name,img)
        except MultiValueDictKeyError:
            file = ProductDb.objects.get(id=dataid).Product_Image
        ProductDb.objects.filter(id=dataid).update(Product_Category=cp, Product_Name=nam, Description=des, Product_Price=pri, Product_Image=file)
        return redirect(product_display)

def deleteproduct(request, dataid):
    prods = ProductDb.objects.filter(id=dataid)
    prods.delete()
    return redirect(product_display)

def admin_login(request):
    return render(request,"AdminLogin.html")
def adminlogin(request):
    if request.method=="POST":
        un=request.POST.get('user_name')
        pwd=request.POST.get('pass_word')
        if User.objects.filter(username__contains=un).exists():
            x = authenticate(username=un, password=pwd)
            if x is not None:
                login(request, x)
                request.session['username']=un
                request.session['password']=pwd
                messages.success(request, "Login successful")
                return redirect(indexpage)
            else:
                messages.error(request, "Invalid Username or Password")
                return redirect(admin_login)
        else:
            messages.error(request, "Invalid Username or Password")
            return redirect(admin_login)
def admin_logout(request):
    del request.session['username']
    messages.success(request, "Logout successfull")
    return redirect(admin_login)
def contact_display(request):
    con = ContactDb.objects.all()
    return render(request,'DisplayContact.html',{'con':con})
def deletecontact(request, dataid):
    cont = ContactDb.objects.filter(id=dataid)
    cont.delete()
    return redirect(contact_display)