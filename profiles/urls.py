from django.urls import path
from .views import ( 
    my_profile_view, 
    invites_received_view, 
    profiles_list_view,
    ToInviteListView, 
    ProfileDetailView,
    ProfileListView,
    FriendsListView,
    send_invatation,
    remove_from_friends,
    accept_invatation,
    reject_invatation,
)

app_name = 'profiles'

urlpatterns = [
    path('', ProfileListView.as_view(), name='all-profiles-view'),
    path('all-friends/', FriendsListView.as_view(), name='all-friends-view'),
    path('myprofile/', my_profile_view, name='my-profile-view'),
    path('my-invites/', invites_received_view, name='my-invites-view'),
    path('to-invite/', ToInviteListView.as_view(), name='invite-profiles-view'),
    path('send-invite/', send_invatation, name='send-invite'),
    path('remove-friend/', remove_from_friends, name='remove-friend'),
    path('<slug>/', ProfileDetailView.as_view(), name='profile-detail-view'),
    # path('<slug>/', ProfileDetailView.as_view(), name='profile-detail-view'),
    path('my-invites/acctept/', accept_invatation, name='accept-invite'),
    path('my-invites/reject/', reject_invatation, name='reject-invite'),
]