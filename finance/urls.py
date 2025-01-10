from django.urls import path
from . import views


urlpatterns=[
    path('',views.home,name='home'),
    path('login/',views.login_user,name='login'),
    path('signup/',views.signup,name='signup'),
    path('logout/',views.logout_user,name='logout'),
    path('dashboard/',views.dashboard,name='dashboard'),
    path('profile/',views.manage_profile,name='profile'),
    path('category/', views.add_category, name='add_category'),
    path('add_transaction/', views.add_transaction, name='add_transaction'),
    path('update_transaction/<int:transaction_id>/', views.update_transaction, name='update_transaction'),
    path('delete_transaction/<int:transaction_id>/', views.delete_transaction, name='delete_transaction'),
    path("savings/", views.create_savings_goal, name="create_savings_goal"),
    path("update_savings/<int:id>/", views.update_savings_goal, name="update_savings_goal"),
    path("delete_savings/<int:id>/", views.delete_savings_goal, name="delete_savings_goal"),

]