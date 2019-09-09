from django.shortcuts import render
from b2c.b2c import B2C

def index(request):
    return render(request, 'index.html', {})

def b2c(request):
    b2c = B2C()
    access_token = b2c.access_token()   

    r = b2c.payment_request(access_token)
    print(r.json())
    return render (request, 'b2c/index.html', {})





