from django.urls import path
from .import views
urlpatterns = [
    path('index/',views.index,name='index'),
    path('update/<int:pk>',views.update,name='update'),
    path('delete/<int:pk>/', views.delete, name='todos-delete'),
]
