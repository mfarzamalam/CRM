from django.contrib import admin
from django.urls import path, include
from leads.views import LandingPageView, SignupView
from django.contrib.auth.views import LoginView,LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', LandingPageView.as_view(), name='home'),
    path('leads/', include('leads.urls', namespace='leads')),
    path('signup/', SignupView.as_view(), name='signup'),
    path('login/', LoginView.as_view(template_name='leads/registration/login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
]
