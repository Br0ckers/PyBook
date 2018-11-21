from django.conf.urls import url
from msg_board import views


urlpatterns = [
    url(r'^$', views.HomePageView.as_view()),
]
