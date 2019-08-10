from django.urls import path
from .views import ApiRoot,DroneList, DroneDetail, DroneCategoryList, DroneCategoryDetail, PilotList, PilotDetail, CompetitionList, CompetitionDetail

urlpatterns = [
	path('drones/', DroneList.as_view(), name = DroneList.name),
	path('drones/<pk>/', DroneDetail.as_view(), name = DroneDetail.name),
	path('drone-categories/', DroneCategoryList.as_view(), name = DroneCategoryList.name),
	path('drones-categories/<pk>/', DroneCategoryDetail.as_view(), name = DroneCategoryDetail.name),
	path('pilots/', PilotList.as_view(), name = PilotList.name),
	path('pilots/<pk>/', PilotDetail.as_view(), name = PilotDetail.name),
	path('competitions/', CompetitionList.as_view(), name = CompetitionList.name),
	path('competitions/<pk>/', CompetitionDetail.as_view(), name = CompetitionDetail.name),
	path('',ApiRoot.as_view() , name=ApiRoot.name),
]