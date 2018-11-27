from django.conf.urls import url, include
from django.urls import path,reverse_lazy
from msg_board import views
from django.contrib.auth.views import LoginView,LogoutView

app_name = 'msg_board'

urlpatterns = [

    # old stuff
    path('/', views.home, name='msg_board-home'),
    path('about/', views.about, name='pybook-about'),
    # url(r'^$', views.HomePageView.as_view(), name='home'),

    #new stuff
    url(r'^member/$', views.MemberViewAll.as_view(), name='member_list'),
    url(r'^member/detail/(?P<id>\d+)/$', views.MemberViewDetail.as_view(), name='member_detail'),
    # url(r'^member/login/$', LoginView.as_view(template_name='msg_board/registration/login.html'),name='member_login'),
    url(r'^$', LoginView.as_view(template_name='msg_board/registration/login.html'),name='member_login'),
    url(r'^member/logout/$', LogoutView.as_view(), name='member_logout'),
    url(r'^member/forgot/(?P<id>\d+)/$', views.MemberRemindPassword.as_view(), name='member_password_remind'),
    url(r'^member/create/$', views.MemberCreate.as_view(), name='member_create'),
    url(r'^member/update/(?P<id>\d+)/$', views.MemberUpdate.as_view(), name='member_update'),
    url(r'^member/delete/(?P<id>\d+)/$', views.MemberDelete.as_view(), name='member_delete'),
    url(r'^member/addfriend/(?P<id>\d+)/$', views.MemberAddFriend.as_view(), name='member_add_friend'),
    url(r'^member/message/(?P<id>\d+)/$', views.MemberMessageViewAll.as_view(), name='member_message_list'),
    url(r'^member/friend/(?P<id>\d+)/$', views.MemberFriendViewAll.as_view(), name='member_friend_list'),

    url(r'^message/$', views.MessageViewAll.as_view(), name='message_list'),
    url(r'^message/detail/(?P<pk>\d+)/$', views.MessageViewDetail.as_view(), name='message_detail'),
    url(r'^message/create/$', views.MessageCreate.as_view(), name='message_create'),
    url(r'^message/update/(?P<pk>\d+)/$', views.MessageUpdate.as_view(), name='message_update'),
    url(r'^message/delete/(?P<pk>\d+)/$', views.MessageDelete.as_view(), name='message_delete'),
    url(r'^message/like/(?P<pk>\d+)/$', views.MessageLike.as_view(), name='message_like'),

]
