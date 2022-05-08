from django.shortcuts import render
from .models import Books

def home(req):
    print('\n\n\n',req.session)
    books=list(Books.objects.all().values());
    d={'books':books}
    d['totq']=0
    if 'totq' in req.session:
        d['totq']=req.session['totq']
    return render(req,'index.html',d)

# def addtocart(req):
#     req.POST

def product(req):
    tmpd={'qty':0}
    if 'add' in req.POST:
        id=req.POST['add']
        book=Books.objects.get(bookid=id)
        tmpd['qty']=req.POST['productqty']
        book.qoh=book.qoh-int(tmpd['qty'])
        book.save()
    else:
        id=req.POST['bookid']
        book=Books.objects.get(bookid=id)


    d={'book':book}
    if 'totq' in req.session:
        d['totq']=int(req.session['totq'])+int(tmpd['qty'])
    else:
        d['totq']=tmpd['qty']

    if book.discount > 0:
     d['price']=book.price - book.discount

    if 'qty' in tmpd:
        if 'totq' in req.session:
            req.session['totq']=int(req.session['totq'])+int(tmpd['qty'])
        else:
            req.session['totq']=int(tmpd['qty'])
        if id in req.session:
            tmpd['qty']=int(req.session[id])+int(tmpd['qty'])
        if 'add' in req.POST:
            req.session[id]=tmpd['qty']
    # print('\n\n\n',req.COOKIES)
    return render(req,'book_details.html',d)

def cart(req):
    r={}
    for i,j in req.session.items():
        print(i)
        try:
            r[int(i)]=j
        except:
            pass
    d={}
    sum=0
    for i in r:
        book=Books.objects.get(bookid=i)
        d[i]={}
        d[i]['id']=i
        d[i]['name']=book.title
        d[i]['qty']=r[i]
        d[i]['desc']=book.description
        d[i]['price']=float(book.price)*float(d[i]['qty'])
        sum=sum+d[i]['price']
    #print(d)
    return render(req,'cart.html',{'data':d,'sum':sum})

def login(req):
    return render(req,'login.html')

def signup(req):
    return render(req,'signup.html')
