from product.models import Product,Category
from trading.models import ItemLine
from user.models import Address
from django.http import JsonResponse,HttpResponse
import json
def stat_product(request) :
    itemlines = ItemLine.objects.filter(is_active=True)
    dict = {}
    for i in itemlines :
        if str(i.product.id) not in dict :
            dict[str(i.product.id)] = 0
        dict[str(i.product.id)] += i.quantity
    result = []
    for i in dict.items() :
        result.append({"product":i[0],"amount":i[1]})
    return HttpResponse(json.dumps(result),
                    content_type='application/json; charset=utf8')

def stat_category(request) :
    category = Category.objects.filter(is_active=True)
    products = Product.objects.filter(is_active=True)
    result = []
    for i in category :
        result.append({"category":i.id,"amount":len(products.filter(category=category))})
    return HttpResponse(json.dumps(result),
                    content_type='application/json; charset=utf8')

def stat_money(request) :
    itemlines = ItemLine.objects.filter(is_active=True)
    dict = {}
    for i in itemlines :
        if str(i.product.id) not in dict :
            dict[str(i.product.id)] = 0
        dict[str(i.product.id)] += i.quantity*i.product.price
    result = []
    for i in dict.items() :
        result.append({"product":i[0],"amount":i[1]})
    return HttpResponse(json.dumps(result),
                    content_type='application/json; charset=utf8')

def stat_user_pay(request) :
    itemlines = ItemLine.objects.filter(is_active=True).exclude(order=None)
    dict = {}
    for i in itemlines :
        if str(i.user.id) not in dict :
            dict[str(i.user.id)] = 0
        if i.order.is_paid :
            dict[str(i.user.id)] += i.quantity*i.product.price
    result = []
    for i in dict.items() :
        result.append({"user":i[0],"amount":i[1]})
    return HttpResponse(json.dumps(result),
                    content_type='application/json; charset=utf8')

def stat_user_order(request) :
    itemlines = ItemLine.objects.filter(is_active=True).exclude(order=None)
    dict = {}
    for i in itemlines :
        if str(i.user.id) not in dict :
            dict[str(i.user.id)] = 0
        if i.order.is_active :
            dict[str(i.user.id)] += i.quantity
    result = []
    for i in dict.items() :
        result.append({"user":i[0],"amount":i[1]})
    return HttpResponse(json.dumps(result),
                    content_type='application/json; charset=utf8')

def stat_user_shipping(request) :
    itemlines = ItemLine.objects.filter(is_active=True).exclude(order=None)
    dict = {}
    for i in itemlines :
        if str(i.user.id) not in dict :
            dict[str(i.user.id)] = 0
        if i.order.is_shipped :
            dict[str(i.user.id)] += 1
    result = []
    for i in dict.items() :
        result.append({"user":i[0],"amount":i[1]})
    return HttpResponse(json.dumps(result),
                    content_type='application/json; charset=utf8')

def stat_address(request) :
    address = Address.objects.filter(is_active=True)
    dict = {}
    for i in address :
        if i.province not in address :
            dict[str(i.province)] = 0
        dict[str(i.province)] += 1
    result = []
    for i in dict.items() :
        result.append({"province":i[0],"amount":i[1]})
    return HttpResponse(json.dumps(result),
                    content_type='application/json; charset=utf8')
