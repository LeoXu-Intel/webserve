from  django.views.generic.base import TemplateView
from django.urls import path
from django.urls import include
from backend import views


urlpatterns = [
    # path('admin/', admin.site.urls),
    path('',TemplateView.as_view(template_name="index.html")),
    path('',include('backend.urls')),
    path('test', views.test_view),
    
]
