from django.conf.urls import url
from django.conf.urls import include
from park import views
from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static

urlpatterns = [
		url(r'^$', views.home, name = "landingpage"),
		url(r'^api/get_user$', views.getUser.as_view(), name='api-get-user'),
		url(r'^logout',views.user_logout,name='logout'),

]
