from django.urls import path
from . import views
urlpatterns = [
    path('', views.index_view, name='index'),
    path('add/', views.add_weekly_page, name='add_weekly'),
    path('add/post', views.post_weekly_data, name="post_weekly_data"),
]
