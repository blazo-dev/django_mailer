from django.urls import path
from .views import DashboarHomeView

app_name = "dashboard"

urlpatterns = [
    path('', DashboarHomeView.as_view(), name='home')
]
