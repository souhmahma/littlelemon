from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User, Group
from .models import Category, MenuItem, Cart, Order, OrderItem
from .serializers import MenuItemSerializer, CategorySerializer, UserSerializer, CartSerializer, OrderSerializer
from .permissions import IsManager, IsDeliveryCrew
from datetime import date

# MENU ITEMS
class MenuItemsView(generics.ListCreateAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    search_fields = ['title', 'category__title']
    ordering_fields = ['price', 'category']

    def get_permissions(self):
        if self.request.method == 'GET':
            return [IsAuthenticated()]
        return [IsManager()]

class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer

    def get_permissions(self):
        if self.request.method == 'GET':
            return [IsAuthenticated()]
        return [IsManager()]

# GROUP MANAGEMENT
class ManagerUsersView(generics.ListCreateAPIView):
    serializer_class = UserSerializer
    permission_classes = [IsManager]

    def get_queryset(self):
        return User.objects.filter(groups__name='Manager')

    def post(self, request, *args, **kwargs):
        username = request.data.get('username')
        user = get_object_or_404(User, username=username)
        manager_group = Group.objects.get(name='Manager')
        user.groups.add(manager_group)
        return Response({"message": "User added to Manager group"}, status.HTTP_201_CREATED)

# CART MANAGEMENT
class CartView(generics.ListCreateAPIView, generics.DestroyAPIView):
    serializer_class = CartSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Cart.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        menuitem = self.request.data.get('menuitem')
        item = get_object_or_404(MenuItem, id=menuitem)
        quantity = self.request.data.get('quantity')
        unit_price = item.price
        price = int(quantity) * unit_price
        serializer.save(user=self.request.user, unit_price=unit_price, price=price)

    def delete(self, request, *args, **kwargs):
        Cart.objects.filter(user=request.user).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# ORDER MANAGEMENT
class OrderView(generics.ListCreateAPIView):
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.groups.filter(name='Manager').exists():
            return Order.objects.all()
        elif user.groups.filter(name='Delivery crew').exists():
            return Order.objects.filter(delivery_crew=user)
        return Order.objects.filter(user=user)

    def post(self, request, *args, **kwargs):
        cart_items = Cart.objects.filter(user=request.user)
        if not cart_items.exists():
            return Response({"message": "Cart is empty"}, status.HTTP_400_BAD_REQUEST)
        
        total = sum([item.price for item in cart_items])
        order = Order.objects.create(user=request.user, status=False, total=total, date=date.today())
        
        for item in cart_items:
            OrderItem.objects.create(order=order, menuitem=item.menuitem, quantity=item.quantity, unit_price=item.unit_price, price=item.price)
            item.delete()
            
        return Response({"message": "Order created"}, status.HTTP_201_CREATED)