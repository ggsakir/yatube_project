from django.urls import path
from . import views

app_name = 'yatube'
app_name = 'posts'

urlpatterns = [
    path('', views.index, name='yatube_list'),
    path('group/<slug:slug>/', views.group_posts, name='posts_list'),
]