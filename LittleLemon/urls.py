"""
URL configuration for LittleLemon project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views:
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views:
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf:
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from LittleLemonAPI.views import LoginView, LogoutView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


# Catch-All View for unmatched API routes
class CatchAllView(APIView):
    def get(self, request, *args, **kwargs):
        return Response({"detail": f"The uri '{request.path}' was not found."}, status=status.HTTP_404_NOT_FOUND)

    # def post(self, request, *args, **kwargs):
    #     return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)

    # def put(self, request, *args, **kwargs):
    #     return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)

    # def delete(self, request, *args, **kwargs):
    #     return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)

    # def patch(self, request, *args, **kwargs):
    #     return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)


urlpatterns = [
    # path('admin/', admin.site.urls),

    path('api/alt-login', LoginView.as_view(), name='login'),
    path('api/logout/', LogoutView.as_view(), name='logout'),

    # Include API routes
    path('api/', include('LittleLemonAPI.urls')),
    path('api/', include('djoser.urls')),
    path('api/', include('djoser.urls.authtoken')),

    # Catch-All for unmatched API requests
    re_path(r'^.*$', CatchAllView.as_view(), name='catch-all-404'),
]
