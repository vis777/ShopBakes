from django.shortcuts import render,redirect
from Shopapp.models import CategoryDb,ProductDb
from Frontapp.models import ContactDb,RegisterDb,CartDb,Checkoutdb
from django.contrib import messages
import razorpay
# Create your views here.
def homepage(request):
    cat = CategoryDb.objects.all()
    return render(request,"Home.html", {'cat':cat})
def productspage(request):
    cat = CategoryDb.objects.all()
    pro = ProductDb.objects.all()
    return render(request,"Products.html",{'pro':pro, 'cat':cat})
def product_filter_page(request, cat_name):
    cat = CategoryDb.objects.all()
    data = ProductDb.objects.filter(Product_Category=cat_name)
    return render(request, "Products_Filtered.html", {'data':data, 'cat':cat})
def singleproductpage(request, proid):
    cat = CategoryDb.objects.all()
    data = ProductDb.objects.get(id=proid)
    return render(request, "SingleProduct.html", {'data':data, 'cat':cat})
def contactpage(request):
    cat = CategoryDb.objects.all()
    return render(request, "Contact.html", {'cat':cat})
def aboutpage(request):
    cat = CategoryDb.objects.all()
    return render(request, "AboutUs.html",{'cat':cat})
def servicepage(request):
    cat = CategoryDb.objects.all()
    return render(request, "Services.html",{'cat':cat})
def savecontact(request):
    if request.method == "POST":
        na = request.POST.get('name')
        em = request.POST.get('email')
        sub = request.POST.get('subject')
        mes = request.POST.get('message')
        obj = ContactDb(Contact_Name=na, Contact_Email=em, Subject=sub, Message=mes)
        obj.save()
        return redirect(contactpage)
def user_login(request):
    return render(request,"Register.html")
def savereg(request):
    if request.method == "POST":
        na = request.POST.get('name')
        mob = request.POST.get('mobile')
        eml = request.POST.get('email')
        use = request.POST.get('username')
        pas = request.POST.get('password')
        obj = RegisterDb(Name=na, Mobile_Number=mob, Email=eml ,UserName=use, PassWord=pas)
        obj.save()
        return redirect(user_login)
def userlogin(request):
    if request.method=="POST":
        un=request.POST.get('user_name')
        pwd=request.POST.get('pass_word')
        if RegisterDb.objects.filter(UserName=un,PassWord=pwd).exists():
            request.session['UserName']=un
            request.session['PassWord']=pwd
            messages.success(request, "WELCOME")
            return redirect(homepage)
        else:
            messages.error(request, "Invalid Username or Password")
            return redirect(user_login)
    return redirect(user_login)
def user_logout(request):
    del request.session['UserName']
    messages.success(request, "Logout Successful")
    return redirect(user_login)
def cartpage(request):
    data = CartDb.objects.filter(Username=request.session['UserName'])
    total_price = 0
    for i in data:
        total_price = total_price+i.Total_Price
    return render(request,"Cart.html" , {'data':data, 'total_price':total_price})
def savecart(request):
    if request.method == "POST":
        na = request.POST.get('username')
        pna = request.POST.get('productname')
        qty = request.POST.get('quantity')
        tp = request.POST.get('total')
        des = request.POST.get('description')
        obj = CartDb(Username = na, Productname = pna, Quantity = qty, Total_Price = tp, Description = des)
        obj.save()
        return redirect(cartpage)
def deletecart(request, dataid):
    cart = CartDb.objects.filter(id=dataid)
    cart.delete()
    return redirect(cartpage)
def checkoutpage(request):
    return render(request, "Checkout.html")
def checkoutpage(request):
    data = CartDb.objects.filter(Username=request.session['UserName'])
    total_price = 0
    for i in data:
        total_price = total_price + i.Total_Price
    return render(request,"Checkout.html",{'data':data,'total_price':total_price})
def save_checkout(request):
    if request.method=="POST":
        fn=request.POST.get('fname')
        ln= request.POST.get('lname')
        ema = request.POST.get('email')
        add = request.POST.get('addr')
        city = request.POST.get('city')
        count = request.POST.get('country')
        tel = request.POST.get('tele')
        obj=Checkoutdb(FirstName=fn,LastName=ln,EmailId=ema,Address=add,City=city,Country=count,Telephone=tel)
        obj.save()
        messages.success(request, "Checkout save successfully....!")
        return redirect(checkoutpage)
def yourorder(request):
    messages.success(request, "Place order has been success....!")
    return redirect(homepage)

def paymentpage(request):
    if request.method == "GET":
        data = CartDb.objects.filter(Username=request.session['UserName'])
        amount = 0
        for i in data:
            amount = amount + i.Total_Price
        order_currency="INR"
        client = razorpay.Client(auth=('rzp_test_8ZlQ5ZrMiHMwmU','f59o6eHBPsp6w3F2RW6ExcgZ'))
        payment=client.order.create({'amount':amount*100,'currency':order_currency,'payment_capture':'1'})
        return render(
            request,
            "payment.html",
            {
                "razorpay_key": 'rzp_test_W3mMQR6ikpp5sy',
                "payment": payment,
            },
        )
    return render(request,"payment.html")
