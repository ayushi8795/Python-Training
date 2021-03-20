from django.urls import path
from . import views

urlpatterns = [
    path('delete/<int:pk>/', views.Post_delete, name="post_delete"),
    path('postform/', views.Post_form, name="post_new"),
    path('', views.Post_list, name='Post_view'),

]
