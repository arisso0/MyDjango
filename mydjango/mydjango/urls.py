from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
import app.views as a

router = routers.DefaultRouter()
router.register(r'book', a.BookViewSet)
router.register(r'review', a.ReviewViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls'))
]
