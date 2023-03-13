from django.contrib import admin
from django.urls import path
from shoes import views

# make up of a url is the name of the route  , package with templates and then method in templates function.
urlpatterns = [
    path('admin/', admin.site.urls),
    path('show', views.show),
    path('edit/<int:id>', views.edit),
    path('update/<int:id>', views.update),
    path('delete/<int:id>', views.destroy),
    path('',views.show)
]
