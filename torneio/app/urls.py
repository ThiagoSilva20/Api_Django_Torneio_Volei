from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),
    ##################################
    path('get_teams', views.fun_teams_g),
    path('get_athletes', views.fun_athletes_g),
    path('get_coach', views.fun_coach_g),
    ##################################
    path('post_teams', views.fun_team_p),
    path('post_athletes', views.fun_athletes_p),
    path('post_coach', views.fun_coach_p),
    ##################################
    path('del_team/<int:id>', views.fun_team_d ),
    path('del_athletes/<int:id>', views.fun_athletes_d ),
    path('del_coach/<int:id>', views.fun_coach_d ),
    ##################################
    path('put_team/<int:id>', views.fun_teams_put),
    path('put_athletes/<int:id>', views.fun_athletes_put),
    path('put_coach/<int:id>', views.fun_coach_put)

]