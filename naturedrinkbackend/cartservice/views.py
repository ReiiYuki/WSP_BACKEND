from rest_framework import viewsets
from rest_framework.response import Response
from .serializers import CartItemLineSerializer, ItemPropertySerializer
from .models import ItemLine , ItemProperty, Order
from rest_framework.decorators import list_route
from product.models import Product,ProductOption,ProductChoice

# Create your views here.

''' WARNING THIS SYSTEM STILL UNTEST!!!! '''
class CartViewSet(viewsets.ModelViewSet) :
    queryset = ItemLine.objects.filter(order=None)
    serializer_class = CartItemLineSerializer

    def list(self,request) :
        itemLines = ItemLine.objects.filter(order=None,user=request.user)
        content = CartItemLineSerializer(itemLines,many=True).data
        for i in range(0,len(content)) :
            content[i]['property'] = ItemPropertySerializer(ItemProperty.objects.filter(item=itemLines[i]),many=True).data
        return Response(content)

    def create(self,request) :
        product = Product.objects.get(id=request.data['product'])
        quantity = request.data['quantity']
        itemLine = ItemLine.objects.create(product=product,quantity=quantity,user=request.user,order=None)
        options = request.data['options']
        for op in options :
            choice = ProductChoice.objects.get(id=op['choice'])
            option = ProductOption.objects.get(id=op['id'])
            itemproperty = ItemProperty.objects.create(item=itemLine,option=option,choice=choice)
        return self.retreive(request,itemLine.id)

    def retreive(self,request,pk=None) :
        item = ItemLine.objects.get(id=pk)
        content = CartItemLineSerializer(item).data
        content['property'] = ItemPropertySerializer(ItemProperty.objects.filter(item=item),many=True).data
        return Response(content)

    # @list_route
    # def pay(self,request) :
    #     items = ItemLine.objects.filter(user=request.user)
    #     order = Order.objects.create(status="U",user=request.user)
    #     content =
    #     for item in items :
    #         item.order = order
    #     return Response()
