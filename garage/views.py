from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import UserCar
from .forms import UserCarForm

@login_required
def my_garage(request):
   
    user_cars = UserCar.objects.filter(user=request.user)
    
    if request.method == 'POST':
        form = UserCarForm(request.POST)
        if form.is_valid():
            car = form.save(commit=False)
            car.user = request.user
            car.save()
            return redirect('my_garage')
    else:
        form = UserCarForm()
        
    return render(request, 'garage/my_garage.html', {
        'user_cars': user_cars,
        'form': form,
    })

@login_required
def edit_car(request, car_id):
    
    car = get_object_or_404(UserCar, id=car_id, user=request.user)
    
    if request.method == 'POST':
        form = UserCarForm(request.POST, instance=car)
        if form.is_valid():
            form.save()
            return redirect('my_garage')
    else:
        form = UserCarForm(instance=car)
        
    return render(request, 'garage/edit_car.html', {'form': form, 'car': car})

@login_required
def delete_car(request, car_id):
   
    car = get_object_or_404(UserCar, id=car_id, user=request.user)
    
    if request.method == 'POST':
        car.delete()
        return redirect('my_garage')
        
    return render(request, 'garage/delete_confirm.html', {'car': car})
