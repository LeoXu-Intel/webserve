from django.urls import path
from . import views
urlpatterns = [
    path('test', views.test_view),
    path('test_P', views.test_view_P),
    path('searchById',views.searchById),
]
