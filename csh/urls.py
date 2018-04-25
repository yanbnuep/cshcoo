from django.urls import path
from django.urls import include
from . import views
urlpatterns = [
    path('', views.index_view, name='index'),
    path('accounts/', include('django.contrib.auth.urls'), name='login'),
    path('<str:year>/<str:month>/<str:day>', views.specify_weekly, name='specify_week'),
    path('add/', views.add_weekly_page, name='add_weekly'),
    path('add/<str:year>/<str:month>/<str:day>', views.add_specify_week, name='add_specify_week'),
    path('add/post', views.post_weekly_data, name="post_weekly_data"),
]
