from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import requests
from django.shortcuts import render
import json

headers = {"Content-type": "application/json"}
username = '6254224e2734182ab5fb2c64a8da3036'
password = 'ac0a71c6a9e42f4ee2acdcf83b9b1f40'
mystore = 'mystore1920'
base_url = 'https://{}:{}@{}.myshopify.com'.format(username, password, mystore)

data = {
    "order": {
        "line_items": [
                {
                "variant_id":15259627487332, 
                "quantity":1
                }
            ]
        }
    }

query_params = {"inventory_behavior": "decrement_obeying_policy"}




def render_products(request):
    r = requests.get('{}/admin/products.json'.format(base_url),
                     headers=headers)
    # Insert 200 check codes here
    k = json.loads((r.content).decode("utf-8"))
    return render(request, "app1/products.html",
                  context={'products':k})


def order_product(request):
    # This should be called by clicking an button from the
    # products page, use a form to collect and make the post
    # refer to the corresponding order_product url
    r = requests.post('{}/admin/orders.json'.format(base_url),
                      headers=headers, data=json.dumps(data),
                      params=query_params)
    # Check for 201
    return HttpResponse("order_created")