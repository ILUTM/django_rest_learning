from django.urls import path, include
from . import views
from django.contrib.auth.views import LogoutView
from rest_framework import routers
from . views import CoffeeViewSet

router = routers.DefaultRouter()
router.register(r'coffee', CoffeeViewSet)

urlpatterns = [
    path('drinks', views.show_menu, name='drinks'),
    path('logout', LogoutView.as_view(next_page='drinks'), name='logout'),
    path('registration', views.Registration.as_view(), name='register'),
    path('login', views.login, name='login'),
#======================Hometask==============================
    path('', include(router.urls)),
    path('auth/', include('rest_framework.urls', namespace='rest_framework'))
]
