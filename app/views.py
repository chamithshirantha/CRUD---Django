from django.shortcuts import render,redirect,loader

# Create your views here.
from django.http import HttpResponse
from .models import Info


# read
def index(request):
    db = Info.objects.all()
    data = {'data':db}
    return render(request,"index.html",data)


# create
def create(request):
    if request.method == 'POST':
        _first_name = request.POST['first-name']
        _last_name = request.POST['last-name']
        _DOB = request.POST['date-birth']
        _address = request.POST['address']
        _mobile = request.POST['mobile']

        obj = Info(first_name=_first_name,last_name=_last_name,date_of_birth=_DOB,address=_address,mobile=_mobile)
        obj.save()
    else:
        redirect('/')
    return render(request,"create.html")

#update
def update(request,id):
    db = Info.objects.get(id=id)
    template = loader.get_template("update.html")
    data = {'data':db}

    if request.method == 'POST':
        _first_name = request.POST['first-name']
        _last_name = request.POST['last-name']
        _DOB = request.POST['date-birth']
        _address = request.POST['address']
        _mobile = request.POST['mobile']

        updb = Info.objects.get(id=id)
        updb.first_name = _first_name
        updb.last_name = _last_name
        updb.date_of_birth =_DOB
        updb.address = _address
        updb.mobile = _mobile
        updb.save()

        redirect('create')

    return HttpResponse(template.render(data,request))

#delete
def delete(request,id):
    db = Info.objects.get(id=id)
    db.delete()

    return redirect('index')