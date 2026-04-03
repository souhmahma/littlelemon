from django.urls import path
from . import views


# urlpatterns = [
#     path('', views.home, name="home"),
#     path('about/', views.about, name="about"),
#     path('book/', views.book, name="book"),
#     path('reservations/', views.reservations, name="reservations"),
#     path('menu/', views.menu, name="menu"),
#     path('menu_item/<int:pk>/', views.display_menu_item, name="menu_item"),  
#     path('bookings/', views.bookings, name='bookings'), 
#     path('menu/', views.MenuItemsView.as_view(), name='menu-items'),
#     path('menu/<int:pk>', views.SingleMenuItemView.as_view(), name='single-menu-item'),

# ]
from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),

    # Pages (HTML)
    path('book/', views.book, name="book"),
    path('reservations/', views.reservations, name="reservations"),
    path('menu/', views.menu, name="menu"),
    path('menu_item/<int:pk>/', views.display_menu_item, name="menu_item"),
    path('bookings/', views.bookings, name='bookings'),

    # API (DRF)
    path('api/menu/', views.MenuItemsView.as_view(), name='menu-items'),
    path('api/menu/<int:pk>/', views.SingleMenuItemView.as_view(), name='single-menu-item'),
    path('api-token-auth/', obtain_auth_token),

]