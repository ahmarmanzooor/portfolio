from django.shortcuts import render, HttpResponse
from home.models import Contact

# Create your views here.

def home(request):
    # return HttpResponse("This is the homepage (/)")
    context={'name':'ahmar','cource': 'django'}
    return render(request, 'home.html',context)

def about(request):
    # return HttpResponse("This is the aboutpage (/)")
    return render(request, 'about.html')


def projects(request):
    # return HttpResponse("This is the projectspage (/)")   
    context={'ahmark':'ahmad', 'asadk':42}  
    return render(request, 'projects.html', context)

def contact(request):
    if request.method=='POST':
        email=request.POST['email']
        name=request.POST.get('name') 
        address=request.POST['address'] 
        phone=request.POST['phone'] 
        # print(email, name, address, phone)

        ins=Contact(email=email, name=name, address=address, phone=phone)
        ins.save()
        

    # return HttpResponse("This is the contactpage (/)")  
     
    return render(request, 'contact.html', )
