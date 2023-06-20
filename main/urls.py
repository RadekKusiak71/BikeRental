from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.Home.as_view(),name='home-page'),
    path('bikes/',views.BikesPage.as_view(),name='bikes-page'),
    path('bikes/rented',views.RentedBikesPage.as_view(),name='rented-bikes-page'),
    path('bike/<int:bike_id>',views.BikeDisplay.as_view(),name='bike'),
    path('bike/reservation/<int:bike_id>',views.BikeReservation.as_view(),name='bike-reservation'),

    path('login/',views.LoginPage.as_view(),name='login-page'),
    path('register/',views.RegisterPage.as_view(),name='register-page'),
    path('logout/',views.LogoutRequest.as_view(),name='logout-request'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
