from django.urls import path
from . import views

urlpatterns = [
    path('api/instruments', views.InstrumentList.as_view(), name='instrument_list'),
    path('api/instruments/<int:pk>', views.InstrumentDetail.as_view(), name='instrument_detail'),
]