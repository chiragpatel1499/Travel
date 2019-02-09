from django.db import models
import django.utils.timezone

class Tuser(models.Model):
    user_id=models.CharField(max_length=30,primary_key='true')
    username=models.CharField(max_length=30)
    phoneno=models.CharField(max_length = 30)
    bdate=models.DateTimeField()
    email=models.CharField(max_length=30)
    password=models.CharField(max_length=20)

class TravelTicket(models.Model):
    travel_ticket_id=models.CharField(max_length=30,primary_key='true')
    travel_from_city=models.CharField(max_length=100)
    travel_to_city=models.CharField(max_length=100)
    travel_price=models.IntegerField()

class HotelTicket(models.Model):
    hotel_ticket_id=models.CharField(max_length=30,primary_key='true')
    hotel_name=models.CharField(max_length=100)
    hotel_room_type=models.CharField(max_length=100)
    hotel_price=models.IntegerField()

class FlightTicket(models.Model):
    flight_ticket_id=models.CharField(max_length=30,primary_key='true')
    flight_name=models.CharField(max_length=50)
    flight_from_city=models.CharField(max_length=100)
    flight_to_city=models.CharField(max_length=100)
    flight_price=models.IntegerField()

class TravelUserData(models.Model):
    user_id=models.ForeignKey('Tuser',on_delete='true')    
    travel_ticket_id=models.ForeignKey('TravelTicket',on_delete='true')
    travel_ticket_from_city=models.CharField(max_length=100)
    travel_ticket_to_city=models.CharField(max_length=100)
    travel_arrival_date=models.DateTimeField()
    travel_no_of_ticket=models.IntegerField()
    travel_ticket_price=models.IntegerField()
    travel_ticket_payment=models.CharField(max_length=10)

class HotelUserData(models.Model):
    user_id=models.ForeignKey('Tuser',on_delete='true')    
    hotel_ticket_id=models.ForeignKey('HotelTicket',on_delete='true')
    hotel_ticket_name=models.CharField(max_length=100)
    hotel_ticket_room_type=models.CharField(max_length=100)
    hotel_checkin=models.DateTimeField()
    hotel_no_of_day=models.IntegerField()
    hotel_no_of_ticket=models.IntegerField()
    hotel_ticket_price=models.IntegerField()
    hotel_ticket_payment=models.CharField(max_length=10)

class FlightUserData(models.Model):
    user_id=models.ForeignKey('Tuser',on_delete='true')
    flight_ticket_id=models.ForeignKey('FlightTicket',on_delete='true')
    flight_ticket_name=models.CharField(max_length=50)
    flight_ticket_from_city=models.CharField(max_length=100)
    flight_ticket_to_city=models.CharField(max_length=100)
    flight_arrival_date=models.DateTimeField()
    flight_no_of_ticket=models.IntegerField()
    flight_ticket_price=models.IntegerField()
    flight_ticket_payment=models.CharField(max_length=10)

class PaymentData(models.Model):       
    user_id=models.ForeignKey('Tuser',on_delete='true')
    payment_ticket_id=models.CharField(max_length=30)
    payment_full_name_on_card=models.CharField(max_length=50)
    Payment_card_type=models.CharField(max_length=30)
    payment_card_number=models.IntegerField()
    payment_amount=models.IntegerField()
    payment_card_expairy_date=models.DateTimeField()
    payment_cvv=models.IntegerField()   
    payment_date=models.DateField()
    payment_time=models.TimeField()

class Feedback(models.Model):
    faq_id = models.CharField(max_length = 30,primary_key = 'true')
    faq_name=models.CharField(max_length=30)
    faq_mobileno=models.IntegerField()
    faq_email=models.CharField(max_length=30)
    faq_subject=models.CharField(max_length=100)
    faq_country=models.CharField(max_length=20)
    faq_message=models.CharField(max_length=200)
# Create your models here.
