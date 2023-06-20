from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.views import View
from django.contrib.auth import login, authenticate, logout
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from .models import UserProfile,Bike,RentOrder
from .forms import RegisterForm
from django.contrib.sessions.models import Session
    
class Home(View):
    def get(self,request):
        bikes = Bike.objects.all()[0:3]
        context ={'bikes':bikes}
        return render(request,'home.html',context)

class BikesPage(View):
    def get(self,request):
        bikes = Bike.objects.filter(is_avaiable=True)
        context ={'bikes':bikes}
        return render(request,'bikes.html',context)

    
class BikeDisplay(View):
    def get(self,request,bike_id):
        bike = Bike.objects.get(id=bike_id)
        bikes = Bike.objects.all()
        context = {'bike':bike,'bikes':bikes}
        return render(request,'bike.html',context)

class BikeReservation(View):
    def get(self, request, bike_id):
        bike = Bike.objects.get(id=bike_id)
        context = {'bike': bike}
        return render(request, 'bike_reservation.html', context)

    def post(self, request, bike_id):
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        rental_end_day = request.POST['rental_end_day']

        if request.user.is_authenticated:
            user = UserProfile.objects.get(user=request.user)
            order = RentOrder.objects.create(
                user=user,
                firstname=firstname,
                lastname=lastname,
                email=email,
                bike=Bike.objects.get(id=bike_id),
                rental_end_day=rental_end_day
            )
        else:
            session_key = request.session.session_key
            if not session_key:
                request.session.save()
                session_key = request.session.session_key
            order = RentOrder.objects.create(
                session_key=session_key,
                firstname=firstname,
                lastname=lastname,
                email=email,
                bike=Bike.objects.get(id=bike_id),
                rental_end_day=rental_end_day
            )

        bike = Bike.objects.get(id=bike_id)
        bike.is_available = False
        bike.save()

        return redirect('home-page')

    
class RentedBikesPage(View):
    def get(self, request):
        if request.user.is_authenticated:
            user_rentals = RentOrder.objects.filter(user__user=request.user)
            context = {'rentals': user_rentals}
            return render(request, 'rented_bikes.html', context)
        else:
            return render(request, 'rented_bikes.html')
        
class LoginPage(View):
    def get(self,request):
        form = AuthenticationForm()
        context ={'login_form':form}
        return render(request,'login.html',context)
    
    def post(self,request):
        form = AuthenticationForm(request,data=request.POST)
        return self.form_validation(form)

    def form_validation(self,form):
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username,password=password)
            if user is not None:
                login(self.request,user)
                return redirect('home-page')
            else:
                return HttpResponse('Not valid data')
        else:
            return HttpResponse('Not valid data')

    
class RegisterPage(View):
    def get(self,request):
        form = RegisterForm()
        context ={'register_form':form}
        return render(request,'register.html',context)
    
    def post(self,request):
        form = RegisterForm(request.POST)
        return self.form_validation(form)

    def form_validation(self,form):
        if form.is_valid():
            user = form.save()
            UserProfile.objects.create(
                user = user,
                username = user.username,
                firstname = user.first_name,
                lastname = user.last_name
            )
            return redirect('login-page')
        else:
            return HttpResponse('Not valid data')
        
class LogoutRequest(View):
    def get(self,request):
        logout(request)
        return redirect('home-page')
    