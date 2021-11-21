from django.urls import path

from . import views

urlpatterns = [
    # test view
    path("users/create", views.create_user),
    path("users/<username>/list", views.list_user),
    path("groups/create", views.create_group),
    path("groups/add_user", views.add_user_to_group),
    path("elections/create", views.create_election),
    path("elections/<int:election_id>", views.list_election),
    path("elections/<int:election_id>/propose", views.make_proposal),
    path("elections/<int:election_id>/vote", views.vote_in_election),
]