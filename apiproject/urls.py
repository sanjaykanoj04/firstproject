from django.contrib import admin
from django.urls import path,include
from rest_framework import routers
from firstapp import views

router = routers.DefaultRouter()
router.register(r'abc',views.FirstappViewSet)


           
urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]