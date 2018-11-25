from django.conf.urls import url, include
from msg_board import views
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy


app_name = 'msg_board'

urlpatterns = [

    # old stuff
    url(r'^$', views.HomePageView.as_view(), name='home'),
    url(r'^player', views.UserListProperView.as_view()),

    #new stuff
    #url(r'^user/?$', views.UserList.as_view(), name='user_list'),
    #url(r'^user/detail/(?P<id>\d+)/$', views.UserViewDetail.as_view(), name='user_detail'),
    url(r'^user/login/$', LoginView.as_view(template_name='registration/login.html'),name='user_login'),
    #url(r'user/', include('django.contrib.auth.urls'),name='user_login'),
    url(r'^user/forgot/(?P<id>\d+)/$', views.UserRemindPassword.as_view(), name='user_password_remind'),
    url(r'^user/create/$', views.UserCreate.as_view(), name='user_create'),
    url(r'^user/update/(?P<id>\d+)/$', views.UserUpdate.as_view(), name='user_update'),
    url(r'^user/delete/(?P<id>\d+)/$', views.UserDelete.as_view(), name='user_delete'),

    url(r'^message/$', views.MessageViewAll.as_view(), name='message_list'),
    url(r'^message/detail/(?P<pk>\d+)/$', views.MessageViewDetail.as_view(), name='message_detail'),
    url(r'^message/create/$', views.MessageCreate.as_view(), name='message_create'),
    url(r'^message/update/(?P<pk>\d+)/$', views.MessageUpdate.as_view(), name='message_update'),
    url(r'^message/delete/(?P<pk>\d+)/$', views.MessageDelete.as_view(), name='message_delete'),
    url(r'^message/like/(?P<pk>\d+)/$', views.MessageLike.as_view(), name='message_like'),

]
