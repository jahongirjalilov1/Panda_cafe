from django.shortcuts import redirect, render
from django.views.generic import ListView

from app.forms import ContactModelForm
from app.models import Food, Chef, Contact


class Indexpage(ListView):
    starter = Food.objects.all()
    breakfast = Food.objects.all()
    chef = Chef.objects.all()
    lunch = Food.objects.all()
    dinner = Food.objects.all()
    template_name = 'index.html'
    model = Food
    extra_context = {
        'starter': starter,
        'breakfast': breakfast,
        'lunch': lunch,
        'dinner': dinner,
        'chef': chef
    }


def contact_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        contact = Contact(name=name, email=email, message=message)
        contact.save()
        return redirect('index')
    return render(request, 'contact.html')
