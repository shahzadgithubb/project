from django.shortcuts import render

# Create your views here.
def master(request) :
    return render(request,'bookapp/master.html')
    
def registration(request) :
    return render(request,'bookapp/registration.html')

def gallery(request) :
    return render(request,'bookapp/gallery.html')

def booking(request) :
    return render(request,'bookapp/booking.html')