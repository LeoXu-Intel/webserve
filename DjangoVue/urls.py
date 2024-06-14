from django.views.generic import TemplateView
from django.urls import path
from django.urls import include
from backend import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('',TemplateView.as_view(template_name="index.html")),
    path('',include('backend.urls')),
    path('SearchPlatform', views.SearchPlatform),
    path('SearchTestCycle', views.SearchTestCycle),
    path('SearchCycleConfig', views.SearchCycleConfig),
    path('SearchTestCase', views.SearchTestCase),
    path('api/login/', views.login_view),
    path('BuildENV', views.BuildENV),
    path('Building', views.Building),
]
