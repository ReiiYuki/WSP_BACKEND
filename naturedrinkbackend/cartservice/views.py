from rest_framework import viewsets,renderers,status
from rest_framework.response import Response
from .serializers import CartItemLineSerializer, ItemPropertySerializer,OrderSerializer,PaymentMethodSerializer
from .models import ItemLine , ItemProperty, Order, PaymentMethod
from rest_framework.decorators import list_route
from product.models import Product,ProductOption,ProductChoice
from member.models import Address
from rest_framework.decorators import list_route
from product.serializers import ProductSerializer,ProductOptionSerializer,ProductChoiceSerializer
# Create your views here.

class CartViewSet(viewsets.ModelViewSet) :
    queryset = ItemLine.objects.filter(order=None)
    serializer_class = CartItemLineSerializer

    def list(self,request) :
        itemLines = ItemLine.objects.filter(order=None,user=request.user)
        content = []
        for i in range(0,len(itemLines)) :
            content[i] = self.retreive(request,itemLines[i].id)
        return Response(content)

    def create(self,request) :
        product = Product.objects.get(id=request.data['product'])
        quantity = request.data['quantity']
        itemLine = ItemLine.objects.create(product=product,quantity=quantity,user=request.user,order=None)
        itemLine.save()
        options = request.data['options']
        for op in options :
            choice = ProductChoice.objects.get(id=op['choice'])
            option = ProductOption.objects.get(id=op['id'])
            itemproperty = ItemProperty.objects.create(item=itemLine,option=option,choice=choice)
            itemproperty.save()
        return self.retreive(request,itemLine.id)

    def retreive(self,request,pk=None) :
        item = ItemLine.objects.get(id=pk)
        content = CartItemLineSerializer(item).data
        content['product'] = ProductSerializer(item.product)
        properties = ItemProperty.objects.filter(item=item)
        content['property'] = ItemPropertySerializer(properties).data
        i = 0
        for prop in properties :
            option = prop.option
            choice = prop.choice
            content['property'][i]["option"] = ProductOptionSerializer(option).data
            content['property'][i]["choice"] = ProductChoiceSerializer(choice).data
            i+=1
        return Response(content)

    @list_route(methods=['post'],renderer_classes=[renderers.JSONRenderer])
    def pay(self,request) :
        if len(ItemLine.objects.filter(user=request.user,order=None)) == 0 :
            return Response({"detail":"Empty Cart..."},status=status.HTTP_400_BAD_REQUEST)
        address = Address.objects.get(id=request.data['address'])
        method = PaymentMethod.objects.get(id=request.data['method'])
        order = Order.objects.create(address=address,method=method,user=request.user)
        order.save()
        content = OrderSerializer(order).data
        count = 0
        content["productlines"] = []
        for i in ItemLine.objects.filter(user=request.user,order=None) :
            i.order = order
            i.save()
            content["productlines"][count] = self.retreive(request,i.id)
        return Response(content)

    def update(self,request,pk=None) :
        item = ItemLine.objects.get(id=pk)
        if item.order != None :
            return Response({"detail" : "Bad Request"},status=status.HTTP_400_BAD_REQUEST)
        quantity = request.data['quantity']
        item.quantity = quantity
        item.save()
        return self.retreive(request,item.id)
class PaymentMethodViewSet(viewsets.ModelViewSet) :
    queryset = PaymentMethod.objects.all()
    serializer_class = PaymentMethodSerializer
