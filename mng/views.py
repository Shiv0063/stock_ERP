from django.shortcuts import render,redirect
from .models import customers,product,mainamount,purchaser,expenses,dailystatus,sales,stock,salesdt
from .form import customersf,productf,mainamountf,purchaserf
from dglog.forms import Users,Nuserform
from dglog.models import Nuser
from django.db.models import Max
from django.contrib import messages
from datetime import datetime
# Create your views here.
from django.http import HttpResponse,JsonResponse
from django.contrib.auth.decorators import login_required,user_passes_test
from django.contrib.auth.models import User

def Search(request):
    sd='Search data'
    pro=product.objects.all()
    if request.method=='POST':
        sd = request.POST.get('sd')
    try:
        if int(sd):
            cust=customers.objects.filter(Phone_no=sd)
            for i in cust:
                x=i.name
            pur=purchaser.objects.filter(seller_name=x)
            sal=sales.objects.filter(purchaser_name=x)
    except:
        x=sd.upper()
        sal=sales.objects.filter(product_name=x)
        cust=customers.objects.filter(name=sd)
        pur=purchaser.objects.filter(product_name=sd)
    mdt={'sal':sal,'cust':cust,'pur':pur,'sd':sd}
    return render(request,"admin/searchdata.html",mdt)

@login_required(login_url='login')
def main(request):
    data=mainamount.objects.all()
    cust=customers.objects.all().filter(status=0).count()
    prod=product.objects.filter(status=0).count()
    entry=purchaser.objects.all().count()
    sal=sales.objects.all()
    sk=stock.objects.all()
    value=0
    for i in data:
        if i.amount=='':
            pass
        else:
            max_id = int(mainamount.objects.aggregate(Max('id'))['id__max'])
            md = mainamount.objects.filter(id=max_id)
            for i in md:
                value=i.amount
    sas=0
    for j in sal:
        sas=sas+j.amount
    sck=0
    for q in sk:
        sck=sck+q.w_amount
    mdt={
        'stock':sck,
        'value':value,
        'cust':cust,
        'prod':prod,
        'entry':entry,
        'sales':sas
    }
    return render(request,"admin/dashboard.html",mdt)

@login_required(login_url='login')
def customer(request):
    data=customers.objects.all()
    if request.method=='POST':
        name = request.POST.get('name')
        village = request.POST.get('village')
        Phone_no = request.POST.get('Phone_no')
        pn=customers.objects.filter(Phone_no=Phone_no)
        if pn:
            messages.error(request,'phone number is already available')
        else:
            form=customers.objects.create(name=name,village=village,Phone_no=Phone_no)
            form.save()
            messages.success(request,'Add Customer Successfuly...')
        return redirect('/Customers')
    return render(request,"admin/customer.html",{'data':data})

def customerview(request):
    data=customers.objects.all()[::-1]
    return render(request,"admin/customerview.html",{'data':data})

def customerdelete(request,id):
    data=customers.objects.get(id=id)
    data.status=1
    data.save()
    messages.error(request,'Delete Successfuly')
    return redirect('/ViewAllCustomer')

def restorcus(request,id):
    data=customers.objects.get(id=id)
    data.status=0
    data.save()
    messages.success(request,'Restor Successfuly')
    return redirect('/dltcus')

def customerdlt(request,id):
    data=customers.objects.get(id=id)
    data.delete()
    messages.error(request,'Delete Successfuly')
    return redirect('/dltcus')

@login_required(login_url='login')
def products(request):
    data=product.objects.all()
    pl=[]
    for i in data:
        dt=i.name.upper()
        pl.append(dt)
    if request.method=='POST':
        name = request.POST.get('name')
        image = request.FILES['image']
        print(image)
        name = name.upper()
        if name in pl:
            print('yes')
            return redirect('/products')
        else:
            data =product.objects.create(name=name,status=0,image=image)
            data.save()
            messages.success(request,'Product Add Successfully...')
            return redirect('/products')
    return render(request,"admin/product.html")

@login_required(login_url='login')
def productview(request):
    data=product.objects.all()[::-1]
    return render(request,"admin/productview.html",{'data':data})

@login_required(login_url='login')
def prodDetails(request,id):
    cdt=product.objects.get(id=id)
    name=cdt.name
    print(name)
    pur=purchaser.objects.all()
    ttl=0
    for i in pur:
        if i.product_name == cdt.name:
            ttl=ttl+i.amount
    data={
        'pur':pur,
        'cdt':cdt,
        'ttl':ttl,
        'name':name
    }
    return render(request,"admin/prodDetails.html",data)


@login_required(login_url='login')
def deleteprod(request,id):
    data=product.objects.get(id=id)
    data.status=1
    data.save()
    messages.success(request,'Delete prodect successfuly.')
    return redirect('/ViewAllProduct')

def restorpro(request,id):
    data=product.objects.get(id=id)
    data.status=0
    data.save()
    messages.success(request,'Restor prodect successfuly.')
    return redirect('/dltpro')

def pdelete(request,id):
    data=product.objects.get(id=id)
    data.delete()
    messages.success(request,'Delete prodect successfuly.')
    return redirect('/dltpro')

@login_required(login_url='login')
def Purchase(request):
    data=purchaser.objects.all()[::-1]
    pro=product.objects.all()
    sk=stock.objects.all()
    if request.method=='POST':
        seller_name = request.POST.get('seller_name')
        product_name = request.POST.get('product_name')
        rate = request.POST.get('rate')
        weight = request.POST.get('weight')
        w_amount = request.POST.get('w_amount')
        if weight=="KG":
            amount=int(rate)*int(w_amount)
        else:
            amount=int(rate)*int(w_amount)*100

        if mainamount.objects.aggregate(Max('id'))['id__max']:
            max_id = int(mainamount.objects.aggregate(Max('id'))['id__max'])
            md = mainamount.objects.filter(id=max_id)
            for i in md:
                mamount=i.amount
            bkamount=mamount-amount
            for i in md:
                if i.amount == 0:
                    messages.success(request,'You Have 0 Balance. Please Add Money..')
                    return redirect('/Purchase')
                elif i.amount >= amount:
                    form1 = purchaser.objects.create(seller_name=seller_name,product_name=product_name,rate=rate,weight=weight,w_amount=w_amount,amount=amount)
                    form1.save()
                    
                    messages.success(request,'Purchase successfully')
                    if form1.save:
                        max_id = int(mainamount.objects.aggregate(Max('id'))['id__max'])
                        md = mainamount.objects.filter(id=max_id)
                        for i in md:
                            main=i.amount-int(amount)
                            am = mainamount.objects.create(amount=main)
                            am.save()
                    else:
                        print("n")
                    form2 = dailystatus.objects.create(name=seller_name,amount=amount,status=0,bkamount=bkamount)
                    form2.save()
                    if weight=="KG":
                        wa=int(w_amount)
                    else:
                        wa=int(w_amount)*100
                    f3=stock.objects.filter(product_name=product_name,rate=rate)
                    if f3:
                        for i in f3:
                            i.w_amount=i.w_amount+wa
                            i.amount=i.amount+amount
                            i.save()
                            return redirect('/Purchase')
                    else:
                        form3=stock.objects.create(product_name=product_name,w_amount=wa,rate=rate,amount=amount)
                        form3.save()
                        # messages.success(request,'Purchase successfully')
                        return redirect('/Purchase')
                else:
                    messages.success(request,'You Have Not Sufficient Balance.')
    ttl=0
    for i in data:
        ttl=ttl+i.amount

    return render(request,"admin/Purchase.html",{'pro':pro,'data':data,'ttl':ttl})

@login_required(login_url='login')
def salles(request):
    data=sales.objects.all()[::-1]
    pro=stock.objects.all()
    sk=stock.objects.all()
    ttl=0
    if request.method=='POST':
        purchaser_name = request.POST.get('purchaser_name')
        pro_ra = request.POST.get('product_name')
        pn = pro_ra.split()
        product_name =pn[0]
        rate = request.POST.get('rate')
        weight = request.POST.get('weight')
        w_amount = request.POST.get('w_amount')
        if weight=="KG":
            amount=int(rate)*int(w_amount)
        else:
            amount=int(rate)*int(w_amount)*100
        sk1=stock.objects.filter(product_name=pn[0],rate=pn[1])
        for i in sk1:
            if weight=="KG":
                maia=int(w_amount)
            else:
                maia=int(w_amount)*100
            am=int(w_amount)*int(pn[1])
            profit=amount-am
            print(am)
            if int(i.w_amount) >= maia:
                form1 = sales.objects.create(purchaser_name=purchaser_name,product_name=product_name,rate=rate,weight=weight,w_amount=w_amount,amount=amount)
                form1.save()
                form2 = salesdt.objects.create(purchaser_name=purchaser_name,product_name=product_name,old_rate=pn[1],old_amount=1,new_rate=rate,new_amount=amount,profit=profit,weight=weight,w_amount=w_amount)
                form2.save()
                if form1.save:
                    dta=stock.objects.filter(product_name=pn[0],rate=pn[1])
                    for j in dta:
                        j.w_amount=int(j.w_amount)-int(maia)
                        j.save()
                        return redirect('/Sales')
            else:
                print('currently stock is not available')
    for i in data:
        ttl=ttl+i.amount
    return render(request,'admin/sales.html',{'pro':pro,'data':data,'ttl':ttl})

@login_required(login_url='login')
def amount(request):
    data=mainamount.objects.all()
    data2=mainamount.objects.all().count()
    c_amount=0
    if data2==0:
        pass
    else:
        max_id = int(mainamount.objects.aggregate(Max('id'))['id__max'])
        md = mainamount.objects.filter(id=max_id)
        c_amount=0
        for i in md:
            c_amount=i.amount

    if request.method=='POST': 
        amount2 = request.POST.get('amount')
        if c_amount==0:
            main=amount2
        else: 
            max_id = int(mainamount.objects.aggregate(Max('id'))['id__max'])
            md = mainamount.objects.filter(id=max_id)
            for i in md:
                main=i.amount+int(amount2)
        
        am = mainamount.objects.create(amount=main)
        am.save()
        if am.save:
            dsa = dailystatus.objects.create(name="Admin",amount=amount2,status=2,bkamount=main)
            dsa.save()
        messages.success(request,'Amount Add Successfully...')
        return redirect('/Amount')
    return render(request,"admin/amount.html",{'data':data,'c_amount':c_amount})

def amountdelete(request,id):
    data=mainamount.objects.get(id=id)
    data.status=1
    data.save()
    messages.success(request,'Amount has been deleted')
    return redirect('/AllAmount')

def restoramt(request,id):
    data=mainamount.objects.get(id=id)
    data.status=0
    data.save()
    messages.success(request,'Restor successfully...')
    return redirect('/dltamt')

def amountdlt(request,id):
    data=mainamount.objects.get(id=id)
    data.delete()
    messages.error(request,'Amount has been deleted')
    return redirect('/dltamt')

def amout0(request):
    max_id = int(mainamount.objects.aggregate(Max('id'))['id__max'])
    md = mainamount.objects.filter(id=max_id)
    c_amount=0
    for i in md:
        c_amount=i.amount
    data=mainamount.objects.create(amount=0)
    data.save()
    messages.error(request,'Amount Withdraw Successfully')
    if data.save:
        dsa = dailystatus.objects.create(name="Admin",amount=c_amount,status=3,bkamount=0)
        dsa.save()   
    return redirect('/Amount')

@login_required(login_url='login')
def allamount(request):
    data=mainamount.objects.all()[::-1]
    data2=mainamount.objects.all().count()
    c_amount=0
    if data2==0:
        pass
    else:
        max_id = int(mainamount.objects.aggregate(Max('id'))['id__max'])
        md = mainamount.objects.filter(id=max_id)
        c_amount=0
        for i in md:
            c_amount=i.amount
    return render(request,"admin/allamount.html",{'data':data,'c_amount':c_amount})

@login_required(login_url='login')
def details(request,id):
    data=customers.objects.get(id=id)
    pur=purchaser.objects.all()
    ttl=0
    for i in pur:
        if i.seller_name == data.name:
            ttl=ttl+i.amount
    cd=[]
    for i in pur:
        if i.seller_name == data.name:
            cd.append(i.amount)
    
    dp=[]
    for i in pur:
        if i.seller_name == data.name:
            dp.append(i.daypurchas())
            for x in dp:
                if x == dp:
                    pass
                else:
                    pass

    maindt={
        'data':data,
        'pur':pur,
        'ttl':ttl,
        'cd':cd,
        'dp':dp,
        'id':0,
    }
    return render(request,"admin/customerdetail.html",maindt)

def value():
    cdt=product.objects.all()
    pur=purchaser.objects.all()
    ttl=0
    for i in pur:
        for x in cdt:
            if i.product_name == x.name:
                ttl=ttl+i.amount

def testdata(request):
    data=mainamount.objects.all()
    cust=customers.objects.all()
    prod=product.objects.all()
    entry=purchaser.objects.all()
    vlu=[]
    for x in prod:
        vlu.append(x.name)
    a=0
    for i in entry:
        for d in range(len(vlu)):
            if i.product_name == vlu:
                print(vlu[d])
                a=a+i.amount
    
    print(a)

    
    for n in prod:
        if i.product_name == n.name[1]:
            print(i.product_name)
    mdt={
        'data':data,
        'cust':cust,
        'prod':prod,
        'entry':entry,
    }
    return render(request,'admin/testdata.html',mdt)

def cs(val):
    entry=purchaser.objects.all()
    a=0
    for i in entry:
        if i.product_name == val:
            if i.weight == 'Quintal':
                a+=i.w_amount*100
            if i.weight == 'KG':
                a+=i.w_amount
    return a

@login_required(login_url='login')
def stock01(request):
    sk=stock.objects.all()[::-1]
    ttl=0
    amttl=0
    for t in sk:
        ttl=ttl+t.w_amount
        amttl=amttl+t.amount
                
    maindt={
        'sk':sk,
        'ttl':ttl,
        'amttl':amttl
    }
    return render(request,'admin/stock.html',maindt)

@login_required(login_url='login')
def stckDetails(request,product_name,rate):
    cdt=product.objects.get(name=product_name)
    pur=purchaser.objects.all()
    rate=rate
    product_name=product_name
    pro=1
    ttl=0
    for i in pur:
        if i.product_name == cdt.name:
            if i.rate == rate:
                ttl=ttl+i.amount
    data={
        'pur':pur,
        'cdt':cdt,
        'ttl':ttl,
        'pro':pro,
        'rate':rate,
        'product_name':product_name
    }
    return render(request,"admin/stockview.html",data)

@login_required(login_url='login')
def resetdata(request):
    data=purchaser.objects.all()
    data2=customers.objects.all()
    data3=mainamount.objects.all()
    data4=product.objects.all()
    data5=expenses.objects.all()
    data6=dailystatus.objects.all()
    data7=sales.objects.all()
    data8=stock.objects.all()
    data9=salesdt.objects.all()
    if data:
        data.delete()
    if data3:
        data3.delete()
    if data2:
        data2.delete()
    if data4:
        data4.delete()
    if data5:
        data5.delete()
    if data6:
        data6.delete()
    if data7:
        data7.delete()
    if data8:
        data8.delete()
    if data9:
        data9.delete()
    return redirect('/')

@login_required(login_url='login')
def deleted(request):
    return render(request,'admin/deletedata.html')

@login_required(login_url='login')
def dailystatusP_E(request):
    entry=dailystatus.objects.all()
    cur=0
    pse=0
    if entry:
        max_id = int(mainamount.objects.aggregate(Max('id'))['id__max'])
        md = mainamount.objects.filter(id=max_id)
        for i in md:
            cur=i.amount
    mdt={
        'entry':entry,
        'cur':cur,
        'pse':pse
    }
    return render(request,'admin/dailystatusview.html',mdt)

@login_required(login_url='login')
def dailystatus01(request):
    return render(request,'admin/dailystatus.html')

@login_required(login_url='login')
def dltpro(request):
    key='pro'
    data=product.objects.all()
    mdt={
        'data':data,
        'key':key
    }
    return render(request,'admin/dltdataview.html',mdt)

def dltamt(request):
    key='amt'
    data=mainamount.objects.all()
    mdt={
        'data':data,
        'key':key
    }
    return render(request,'admin/dltdataview.html',mdt)

def dltcus(request):
    key='cus'
    data=customers.objects.all()
    mdt={
        'data':data,
        'key':key
    }
    return render(request,'admin/dltdataview.html',mdt)
    
def dltexp(request):
    key='exp'
    data=expenses.objects.all()
    mdt={
        'data':data,
        'key':key
    }
    return render(request,'admin/dltdataview.html',mdt)

@login_required(login_url='login')
def expens(request):
    if request.method=='POST': 
        exname = request.POST.get('exname')
        examount = request.POST.get('examount')
        max_id = int(mainamount.objects.aggregate(Max('id'))['id__max'])
        md = mainamount.objects.filter(id=max_id)
        for i in md:
            mamount=i.amount

        bkamount=mamount-int(examount)
        if mamount >= int(examount):
            data=expenses.objects.create(exname=exname,examount=examount)
            data.save()
            messages.success(request,'Add Expens Successfully')
            form2 = dailystatus.objects.create(name=exname,amount=examount,status=1,bkamount=bkamount)
            form2.save()
            if form2.save:
                max_id = int(mainamount.objects.aggregate(Max('id'))['id__max'])
                md = mainamount.objects.filter(id=max_id)
                for i in md:
                    main=i.amount-int(examount)
                    am = mainamount.objects.create(amount=main)
                    am.save()
                    return redirect('/Expenses')
            else:
                print("expans")
        else:
            print("Amount not avalebal") 
    else:
        pass
    return render(request,"admin/expenses.html")

@login_required(login_url='login')
def expensesview(request):
    data=expenses.objects.all()[::-1]
    date=datetime.now()
    tday=date.strftime('%B %d %Y')
    mdt={
    'data':data,
    'tday':tday,
    }
    return render(request,"admin/expensesview.html",mdt)        

@login_required(login_url='login')
def expdelete(request,id):
    data=expenses.objects.get(id=id)
    data.expstatus=1
    data.save()
    messages.success(request,'Expenses has been deleted')
    return redirect('/ViewAllExpenses')

@login_required(login_url='login')
def restorexp(request,id):
    data=expenses.objects.get(id=id)
    data.expstatus=0
    data.save()
    messages.success(request,'Restor successfully...')
    return redirect('/dltexp')

@login_required(login_url='login')
def expdlt(request,id):
    data=expenses.objects.get(id=id)
    data.delete()
    messages.error(request,'Expenses has been deleted')
    return redirect('/dltexp')


@login_required(login_url='login')
def salesdata(request):
    entry=salesdt.objects.all()[::-1]
    pro=0
    amt=0
    for i in entry:
        pro=pro+i.profit
        amt=amt+i.new_amount

    mdt={
        'entry':entry,
        'pro':pro,
        'amt':amt
    }
    return render(request,"admin/salesdata.html",mdt)

def signup(request):
    if request.method=='POST': 
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        phone_no = request.POST.get('phone_no')
        uname = request.POST.get('uname')
        pword = request.POST.get('pword')
        print(pword)
        uf1 = User.objects.create(first_name=fname,last_name=lname,username=uname,password=pword)
        uf2 = Nuser.objects.create(mobile=phone_no)
        uf1.save()
        uf2.save()
        return redirect('/login')
    return render(request,'admin/signup.html')

# error pages
def error_404_view(request,exception):
    return render(request,"admin/e404p.html")
