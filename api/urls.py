from django.urls import path
from . import views
urlpatterns = [
    # path('api/', views.index.as_view(), name="main"),
    path('api/start', views.start, name="start"),
    path('api/', views.index, name="main"),
]
