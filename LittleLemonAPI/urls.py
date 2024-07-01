from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter(trailing_slash=False)
router.register('menu-items', views.MenuItemView, basename='menu_item')
router.register('cart/menu-items', views.CartView, basename='cart')
router.register('orders', views.OrderView, basename='order')
router.register('groups/manager/users', views.ManagerView, basename='manager')
router.register('groups/delivery-crew/users', views.DeliveryCrewView, basename='delivery_crew')

urlpatterns = router.urls