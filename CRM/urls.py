from django.contrib import admin
from django.urls import path, include
from leads.views import LandingPageView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', LandingPageView.as_view(), name='home'),
    path('leads/', include('leads.urls', namespace='leads'))
]
