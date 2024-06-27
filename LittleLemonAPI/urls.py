from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter(trailing_slash=False)
router.register('menu-items', views.MenuItemView, basename='menu_items')
router.register('cart/menu-items', views.CartView, basename='cart')
router.register('orders', views.OrdersView, basename='orders')
router.register('groups/manager/users', views.ManagersView, basename='managers')
router.register('groups/delivery-crew/users', views.DeliveryCrewsView, basename='delivery_crew')

urlpatterns = router.urls