from django.urls import path
from .views import JetList, JetDetail

urlpatterns = [
  path('', JetList.as_view(), name='jet_list'),
  path('<int:pk>', JetDetail.as_view(), name='jet_detail')
]