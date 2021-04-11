from django.urls import path
from . views import StationList, LineList, LineCreate, StationCreate, LineDelete, StationDelete, LineEdit, StationEdit
from . import views



app_name = 'peron'

urlpatterns = [    
    path('station/', StationList.as_view(), name='stationList'),
    path('station_add/', StationCreate.as_view(), name='addStation'),
    path('station_delete/<int:pk>', StationDelete.as_view(), name='deleteStation'),
    path('station_edit/<int:pk>', StationEdit.as_view(), name='editStation'),
    path('line/', LineList.as_view(), name='lineList'),
    path('line_add/', LineCreate.as_view(), name='addLine'),
    path('line_delete/<int:pk>', LineDelete.as_view(), name='deleteLine'),      
    path('line_edit/<int:pk>', LineEdit.as_view(), name='editLine'),
    path('', views.home, name='home'),
    path('map/', views.map, name='map'),
]