from django.shortcuts import render_to_response,redirect,render
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib import auth
from django.template.context_processors import csrf
from django.contrib.auth.decorators import login_required
from login.models import *
from django.contrib.auth import *
from datetime import datetime
from login.forms import *
# Create your views here.

def login1(request):
    c={}
    c.update
    return render(request,'signin.html',c)

def auth_view(request):
	username = request.POST.get('username', '')
	password = request.POST.get('password', '')
	user = auth.authenticate(username=username, password=password)
	tuser=Tuser.objects.filter(user_id=username)
	count=tuser.count()
	if user is not None:
		auth.login(request, user)
		if int(count)>0:
                    return HttpResponseRedirect('/login/loggedin/')
	else:
		return HttpResponseRedirect('/login/invalidlogin/')

@login_required(login_url = '/login/')
def loggedin(request):
	if request.user.is_authenticated:
		return HttpResponseRedirect('/login/home/')
	else:
		return HttpResponseRedirect('/login/invalidlogin/')

def invalidlogin(request):
	c ={}
	c.update(csrf(request))
	c['q']="Invalid UserName or PassWord"
	return render(request,'signin.html',c)
    

def storedata(request): #view to store the new user data in to datbase...
	username= request.POST.get('username', '')
	name= request.POST.get('name','')
	password1= request.POST.get('password1', '')
	password2= request.POST.get('password2', '')
	email= request.POST.get('email','')
	phone= request.POST.get('phone', '')
	date= request.POST.get('date', '')
	c ={}
	c.update(csrf(request))
	form = SignUpForm(request.POST)
	c['form']=form;
	c['role'] = 'member'
	if form.is_valid():
			profile= Tuser(user_id=username,
                                       username=name,
                                       email=email,
                                       phoneno=phone,
                                       bdate=date,
                                       password=password1)
			profile.save()
			form.save()
			username = form.cleaned_data.get('username')
			raw_password = form.cleaned_data.get('password1')
			user = authenticate(username=username, password=raw_password)
			login(request, user)
			return render(request,'home.html')
	return render(request,'signup.html',c)

@login_required(login_url = '/login/')    
def travelbooking(request):
    c ={}
    c.update(csrf(request))
    id = request.user.id
    tuser1=User.objects.get(id=id)
    tuser=Tuser.objects.get(user_id=tuser1.username)
    tf=request.POST.get('travel_city_from','')
    tt=request.POST.get('travel_city_to','')
    travel_object=TravelTicket.objects.get( travel_from_city=tf, travel_to_city=tt)
    travel_price=int(travel_object.travel_price)
    travel_ticket_from_city=travel_object.travel_from_city
    travel_ticket_to_city=travel_object.travel_to_city
    travel_arrival_date=request.POST.get('travel_arrival_date','')
    travel_no_of_tickets=request.POST.get('travel_no_of_tickets','')
    travel_ticket_price=int(int(travel_price)*int(travel_no_of_tickets))
    travel_ticket_payment='Done'
    tuser=TravelUserData(user_id=tuser,
                         travel_ticket_id=travel_object,
                         travel_ticket_from_city=travel_ticket_from_city,
                         travel_ticket_to_city=travel_ticket_to_city,
                         travel_arrival_date=travel_arrival_date,
                         travel_no_of_ticket=int(travel_no_of_tickets),
                         travel_ticket_price=travel_ticket_price,
                         travel_ticket_payment=travel_ticket_payment
                         )
    tuser.save()
    return HttpResponseRedirect('/login/travelbookingdata/')

@login_required(login_url = '/login/')
def hotelbooking(request):
    c ={}
    c.update(csrf(request))
    id = request.user.id
    tuser1=User.objects.get(id=id)
    tuser=Tuser.objects.get(user_id=tuser1.username)
    hotel_name=request.POST.get('hotel_name','')
    hotel_room_type=request.POST.get('hotel_room_type','')
    hotel_object=HotelTicket.objects.get(hotel_room_type=hotel_room_type,hotel_name=hotel_name)
    hotel_price=int(hotel_object.hotel_price)
    hotel_ticket_name=hotel_object.hotel_name
    hotel_ticket_room_type=hotel_object.hotel_room_type
    hotel_no_of_rooms=request.POST.get('hotel_no_of_rooms','')
    hotel_checkin=request.POST.get('hotel_checkin','')
    hotel_no_of_day=request.POST.get('hotel_no_of_day','')
    hotel_room_type=request.POST.get('hotel_room_type','')
    hotel_no_of_ticket=request.POST.get('hotel_no_of_person','')
    hotel_ticket_price=int(int(hotel_price)*int(hotel_no_of_rooms)*int(hotel_no_of_day))
    hotel_ticket_payment='Done'
    huser=HotelUserData(user_id=tuser,
                        hotel_ticket_id=hotel_object,
                        hotel_ticket_name=hotel_ticket_name,
                        hotel_ticket_room_type=hotel_ticket_room_type,
                        hotel_checkin=hotel_checkin,
                        hotel_no_of_day=int(hotel_no_of_day),
                        hotel_no_of_ticket=int(hotel_no_of_ticket),
                        hotel_ticket_price=int(hotel_ticket_price),
                        hotel_ticket_payment=hotel_ticket_payment
                        )
    huser.save()
    return HttpResponseRedirect('/login/hotelbookingdata/')

@login_required(login_url = '/login/')
def flightbooking(request):
    c ={}
    c.update(csrf(request))
    id = request.user.id
    tuser1=User.objects.get(id=id)
    tuser=Tuser.objects.get(user_id=tuser1.username)
    ff=request.POST.get('flight_city_from','')
    ft=request.POST.get('flight_city_to','')
    flight_object=FlightTicket.objects.get(flight_from_city=ff,flight_to_city=ft)
    flight_price=int(flight_object.flight_price)
    flight_ticket_name=flight_object.flight_name
    flight_ticket_from_city=flight_object.flight_from_city
    flight_ticket_to_city=flight_object.flight_to_city
    flight_arrival_date=request.POST.get('flight_arrival_date','')
    flight_no_of_ticket=request.POST.get('flight_no_of_tickets','')
    flight_ticket_price=int(int(flight_price)*int(flight_no_of_ticket))
    flight_ticket_payment='Done'
    fuser=FlightUserData(user_id=tuser,
                         flight_ticket_id=flight_object,
                         flight_ticket_name=flight_ticket_name,
                         flight_ticket_from_city=flight_ticket_from_city,
                         flight_ticket_to_city=flight_ticket_to_city,
                         flight_arrival_date=flight_arrival_date,
                         flight_no_of_ticket=int(flight_no_of_ticket),
                         flight_ticket_price=flight_ticket_price,
                         flight_ticket_payment=flight_ticket_payment)
    fuser.save()
    return HttpResponseRedirect('/login/flightbookingdata/')

@login_required(login_url = '/login/')    
def makepaymentstore(request):
    c ={}
    c.update(csrf(request))
    payment_amount=request.POST.get('payment_amount','')
    payment_card_type=request.POST.get('payment_card_type','')
    payment_card_number=request.POST.get('payment_card_number','')
    payment_card_expairy_date=request.POST.get('payment_card_expairy_date','')
    payment_cvv=request.POST.get('payment_cvv','')
    payment_full_name_on_a_card=request.POST.get('payment_full_name_on_a_card','')
    now=datetime.datetime.now()
    payment_date=now.date+'/'+now.month+'/'+now.year
    payment_time=now.hour+':'+now.minute+':'+now.second
    puser=PaymentData(username=username,payment_ticket_id= payment_ticket_id,payment_full_name_on_card=payment_full_name_on_card,payment_card_type=payment_card_type,payment_card_number=payment_card_number,payment_amount=payment_amount,payment_card_expairy_date=payment_card_expairy_date,payment_cvv=payment_cvv,payment_date=payment_date, payment_time=payment_time)
    puser.save() 
    return render(request,'home.html',c)

def faqstore(request):
    c ={}
    c.update(csrf(request))
    faq_id=request.POST.get('faq_id','')
    faq_name=request.POST.get('faq_name')
    faq_mobileno=request.POST.get('faq_mobileno','')
    faq_emailid=request.POST.get('faq_emailid','')
    faq_subject=request.POST.get('faq_subject','')
    faq_city=request.POST.get('faq_city','')
    faq_country=request.POST.get('faq_country','')
    faq_message=request.POST.get('faq_message','')
    fuser=Feedback(faq_id=faq_id,faq_name=faq_name,faq_mobileno=faq_mobileno,faq_email=faq_email,faq_subject=faq_subject,faq_country=faq_country,faq_message=faq_message)
    fuser.save()
    return render(request,'home.html',c)

def signin(request):
    c ={}
    c.update(csrf(request))
    return render(request,'signin.html',c)


def signup(request):
    c ={}
    c.update(csrf(request))
    return render(request,'signup.html',c)


def forgotpassword(request):
    c ={}
    c.update(csrf(request))
    return render(request,'forgotpassword.html',c)

def forgotpassworddata(request):
    c ={}
    c.update(csrf(request))
    username= request.POST.get('username', '')
    bdate=request.POST.get('bdate','')
    newpassword=request.POST.get('newpassword','')
    renewpassword=request.POST.get('renewpassword','')
    u=Tuser.objects.get(user_id=user_id,bdate=bdate)
    if u is not None:
        if(renewpassword=newpassword):
            u
            u.password(password=password)
        
    return render(request,'forgotpassword.html',c)

@login_required(login_url = '/login/')   
def home(request):
    c ={}
    c.update(csrf(request))
    return render(request,'home.html',c)

@login_required(login_url = '/login/')
def profile(request):
    c ={}
    c.update(csrf(request))
    id = request.user.id
    tuser=User.objects.get(id=id)
    p=Tuser.objects.get(user_id=tuser.username)
    c['p']=p
    return render(request,'profile.html',c)

@login_required(login_url = '/login/')
def travelbookingdata(request):
    c ={}
    c.update(csrf(request))
    id = request.user.id
    tuser1=User.objects.get(id=id)
    tuser=Tuser.objects.get(user_id=tuser1.username)
    travel_object_list=TravelUserData.objects.filter(user_id=tuser.user_id)
    c['travel_object_list']=travel_object_list
    return render(request,'travelbooking.html',c)

@login_required(login_url = '/login/')
def flightbookingdata(request):
    c ={}
    c.update(csrf(request))
    id = request.user.id
    tuser1=User.objects.get(id=id)
    tuser=Tuser.objects.get(user_id=tuser1.username)
    flight_object_list=FlightUserData.objects.filter(user_id=tuser.user_id)
    c['flight_object_list']=flight_object_list
    return render(request,'flightbooking.html',c)

@login_required(login_url = '/login/')
def hotelbookingdata(request):
    c ={}
    c.update(csrf(request))
    id = request.user.id
    tuser1=User.objects.get(id=id)
    tuser=Tuser.objects.get(user_id=tuser1.username)
    hotel_object_list=HotelUserData.objects.filter(user_id=tuser.user_id)
    print(hotel_object_list)
    c['hotel_object_list']=hotel_object_list
    return render(request,'hotelbooking.html',c)

@login_required(login_url = '/login/')
def payment(request):
    c ={}
    c.update(csrf(request))
    return render(request,'payment.html',c)

@login_required(login_url = '/login/')
def makepayment(request):
    c={}
    c.update=(csrf(request))
    return render(request,'makepayment.html',c)


def aboutus(request):
    c ={}
    c.update(csrf(request))
    return render(request,'aboutus.html',c)

def contactus(request):
    c ={}
    c.update(csrf(request))
    return render(request,'contactus.html',c)

def blog(request):
    c ={}
    c.update(csrf(request))
    return render(request,'blog.html',c)

def discount(request):
    c ={}
    c.update(csrf(request))
    return render(request,'discount,html',c)

def faq(request):
    c={}
    c.update(csrf(request))
    return render(request,'faq.html',c)

def cliamandrefund(request):
    c ={}
    c.update(csrf(request))
    return render(request,'cliamandrefund.html',c)

def logout(request):
	auth.logout(request)
	return render(request,'signin.html')
