from django.conf.urls import url, include
import views

urlpatterns = [
	url(r'^$', views.index, name='home'),
	url(r'^246321517:AAF3A8cpRNvEmJj5A2gOBsBPySrkBeHQ2GM/' , views.hook)

]
