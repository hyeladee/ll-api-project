#from datetime import date
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User, Group
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from .models import Category, MenuItem, Cart, OrderItem, Order, User
from .serializers import CategorySerializer, MenuItemSerializer, CartSerializer, OrderItemSerializer, OrderSerializer, UserSerializer


# Create your views here.
class MenuItemView(viewsets.ModelViewSet):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    permission_classes = [IsAuthenticated]
    
    def create(self, request):
        if request.user.groups.filter(name='Manager').exists():
            new_menu = MenuItemSerializer(data=request.data)
            if new_menu.is_valid():
                new_menu.save()
                return Response(new_menu.data, status=status.HTTP_201_CREATED)
            return Response(new_menu.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_403_FORBIDDEN)
    
    def update(self, request, pk):        
        if request.user.groups.filter(name='Manager').exists():
            menu_item = get_object_or_404(MenuItem, pk=pk)
            menu_update = MenuItemSerializer(menu_item, data=request.data)
            if menu_update.is_valid():
                menu_update.save()
                return Response(menu_update.data, status=status.HTTP_200_OK)
            return Response(menu_update.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_403_FORBIDDEN)

    def partial_update(self, request, pk):        
        if request.user.groups.filter(name='Manager').exists():
            menu_item = get_object_or_404(MenuItem, pk=pk)
            partial_menu_update = MenuItemSerializer(menu_item, data=request.data, partial=True)
            if partial_menu_update.is_valid():
                partial_menu_update.save()
                return Response(partial_menu_update.data, status=status.HTTP_200_OK)
            return Response(partial_menu_update.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_403_FORBIDDEN)

    def destroy(self, request, pk):        
        if request.user.groups.filter(name='Manager').exists():
            menu_item = get_object_or_404(MenuItem, pk=pk)
            menu_item.delete()
            return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_403_FORBIDDEN)

 
class CartView(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    permission_classes = [IsAuthenticated]
    
    def list(self, request):
        cart_items = Cart.objects.filter(user=request.user)
        serializer = CartSerializer(cart_items, many=True)
        return Response(serializer.data)

    def create(self, request):
        cart_serializer = CartSerializer(data=request.data)
        
        if cart_serializer.is_valid():
            menuitem_id = cart_serializer.validated_data['menuitem'].id
            quantity = cart_serializer.validated_data['quantity']
            
            menu_item = get_object_or_404(MenuItem, id=menuitem_id)
            existing_cart_item = Cart.objects.filter(user=request.user, menuitem=menu_item).first()
            
            if existing_cart_item:
                existing_cart_item.quantity += quantity
                existing_cart_item.price = existing_cart_item.unit_price * existing_cart_item.quantity
                existing_cart_item.save()
                cart_item = existing_cart_item
            else:
                cart_item = cart_serializer.save(
                    user=request.user,
                    unit_price=menu_item.price,
                    price=menu_item.price * quantity
                )

            response_serializer = CartSerializer(cart_item)
            return Response(response_serializer.data, status=status.HTTP_201_CREATED)
        return Response(cart_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        if pk is not None:
            cart_item = get_object_or_404(Cart, pk=pk, user=request.user)
            cart_item.delete()
            return Response(status=status.HTTP_200_OK)
        else:
            cart_items = Cart.objects.filter(user=request.user)
            cart_items.delete()
            return Response(status=status.HTTP_200_OK)


class OrdersView(viewsets.ModelViewSet):
    pass


class ManagersView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def list(self, request):
        if request.user.groups.filter(name='Manager').exists():
            managers = Group.objects.get(name='Manager').user_set.all()
            serializer = UserSerializer(managers, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_403_FORBIDDEN)

    def create(self, request):
        if request.user.groups.filter(name='Manager').exists():
            username = request.data['username']
            if username:
                user = get_object_or_404(User, username=username)
                managers = Group.objects.get(name='Manager')
                managers.user_set.add(user)
                return Response(status=status.HTTP_201_CREATED)
            return Response(status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_403_FORBIDDEN)

    def destroy(self, request, pk):
        if request.user.groups.filter(name='Manager').exists():
            user = get_object_or_404(User, pk=pk)
            managers = Group.objects.get(name='Manager')
            managers.user_set.remove(user)
            return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_403_FORBIDDEN)


class DeliveryCrewsView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def list(self, request):
        if request.user.groups.filter(name='Manager').exists():
            delivery_crew = Group.objects.get(name='Delivery_Crew').user_set.all()
            serializer = UserSerializer(delivery_crew, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_403_FORBIDDEN)

    def create(self, request):
        if request.user.groups.filter(name='Manager').exists():
            username = request.data['username']
            if username:
                user = get_object_or_404(User, username=username)
                delivery_crew = Group.objects.get(name='Delivery_Crew')
                delivery_crew.user_set.add(user)
                return Response(status=status.HTTP_201_CREATED)
            return Response(status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_403_FORBIDDEN)

    def destroy(self, request, pk):
        if request.user.groups.filter(name='Manager').exists():
            user = get_object_or_404(User, pk=pk)
            delivery_crew = Group.objects.get(name='Delivery_Crew')
            delivery_crew.user_set.remove(user)
            return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_403_FORBIDDEN)

