from django.urls import path
from . import views

urlpatterns = [
    path('',views.login1),
        path('logout/',views.logout),
        path('auth_view/',views.auth_view),
        path('storedata/',views.storedata),
        path('loggedin/',views.loggedin),
        path('invalidlogin/',views.invalidlogin),
	path('signin/',views.signin),
	path('signup/',views.signup),
        path('forgotpassword/',views.forgotpassword),
        path('home/',views.home),
	path('profile/',views.profile),
	path('travelbooking/',views.travelbooking),
        path('travelbookingdata/',views.travelbookingdata),
	path('flightbooking/',views.flightbooking),
        path('flightbookingdata/',views.flightbookingdata),
        path('hotelbooking/',views.hotelbooking),
        path('hotelbookingdata/',views.hotelbookingdata),
        path('payment/',views.payment),
        path('makepayment/',views.makepayment),
        path('aboutus/',views.aboutus),
        path('contactus/',views.contactus),
        path('blog/',views.blog),
        path('discount/',views.discount),
        path('faq/',views.faq),
        path('cliamandrefund/',views.cliamandrefund),
	
]
