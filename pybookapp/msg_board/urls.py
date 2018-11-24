from django.conf.urls import url
from msg_board import views


urlpatterns = [

    # old stuff
    url(r'^$', views.HomePageView.as_view()),
    url(r'^user', views.UserListView.as_view()),
    url(r'^player', views.UserListProperView.as_view()),

    #new stuff
    url(r'^user/?$', views.ViewUsers.as_view(), name='user-list'),
    url(r'^user/update/(?P<id>\d+)/$', views.UpdateUser.as_view(), name='user-update'),
    url(r'^user/login/(?P<id>\d+)/$', views.LoginUser.as_view(), name='user-login'),
    url(r'^user/forgot/(?P<id>\d+)/$', views.RemindPasswordUser.as_view(), name='user-password-remind'),
    url(r'^user/create/$', views.CreateUser.as_view(), name='user-create'),
    url(r'^user/delete/(?P<id>\d+)/$', views.DeleteUser.as_view(), name='user-delete'),

]
