from django.urls import path
from .views import Home, WebApps, WebDevelopment, ContactView

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('webapps/', WebApps.as_view(), name='webapps'),
    path('webdevelopment/', WebDevelopment.as_view(), name='webdevelopment'),
    path('contact/', ContactView.as_view(), name='contact'),
]