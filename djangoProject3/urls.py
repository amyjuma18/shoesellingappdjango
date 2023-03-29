from django.contrib import admin
from django.urls import path, include
from shoes import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('shoes', views.shoes),
    path('show', views.show),
    path('edit/<int:id>', views.edit),
    path('update/<int:id>', views.update),
    path('delete/<int:id>', views.destory),
    path('check_out/<int:id>', views.check_out),
    path('mpesa', views.mpesa),
    path('checkout/<int:id>', views.checkout),
    path('', views.show)
]