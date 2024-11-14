'''
# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('service-requests/new/', views.ServiceRequestCreateView.as_view(), name='create_service_request'),
    path('service-requests/', views.ServiceRequestListView.as_view(), name='list_service_requests'),
    path('service-requests/<int:pk>/', views.ServiceRequestDetailView.as_view(), name='service_request_detail'),
]
'''

from django.urls import path
from . import views

urlpatterns = [
    path('new/', views.ServiceRequestCreateView.as_view(), name='create_service_request'),  # For submitting new requests
    path('', views.ServiceRequestListView.as_view(), name='list_service_requests'),          # For listing all requests
    path('<int:pk>/', views.ServiceRequestDetailView.as_view(), name='service_request_detail'),  # For viewing a specific request
]
