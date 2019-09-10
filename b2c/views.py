from django.shortcuts import render
from b2c.b2c import B2C
from django.views.decorators.csrf import csrf_exempt
import pprint
import json

def index(request):
    return render(request, 'index.html', {})

def b2c(request):
    b2c = B2C()
    access_token = b2c.access_token()   
    print(access_token)
    r = b2c.payment_request(access_token)
    print(r.json())
    return render (request, 'b2c/index.html', {})

@csrf_exempt
def process_b2c_callback(request):
    data = json.loads(request.body)
    pprint.pprint(data)
    return render(request, 'b2c/b2c_results.html', {})



