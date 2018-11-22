from django.conf.urls import url
from msg_board import views


urlpatterns = [
    url(r'^$', views.HomePageView.as_view()),
    url(r'^user', views.UserListView.as_view()),
    url(r'^player', views.UserListProperView.as_view()),

]
