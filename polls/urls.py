from django.urls import path
from . import views

urlpatterns = [
	path('',views.index,name='home'),
	path('create/',views.create,name='create'),
	path('result/',views.results,name='results'),
	path('vote/<poll_id>/',views.vote,name='vote'),
	path('detailedresult/<poll_id>/',views.detailedresult,name='detailedresult')
]