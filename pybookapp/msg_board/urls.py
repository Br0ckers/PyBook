from django.conf.urls import url
from django.urls import path
from msg_board import views


urlpatterns = [
    url(r'^$', views.HomePageView.as_view()),
    url(r'^user', views.UserListView.as_view()),
    url(r'^player', views.UserListProperView.as_view()),
    path('home/', views.home, name='pybook-home'),
    path('about/', views.about, name='pybook-about'),
]
