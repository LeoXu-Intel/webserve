from django.urls import path
from . import views
urlpatterns = [
    path('SearchPlatform', views.SearchPlatform),
    path('SearchTestCycle', views.SearchTestCycle),
    path('SearchCycleConfig', views.SearchCycleConfig),
    path('SearchTestCase', views.SearchTestCase),
    path('api/login/', views.login_view),
]
