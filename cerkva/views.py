from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.urls import reverse


from religion.forms import MessageForm
from religion.models import *

def index(request):
    # services = Service.objects.all()
    return render(request, 'index.html')


def order_service(request):
    if request.method == 'GET':
        form = MessageForm()
        form.initial['service'] = request.GET.get('service')
        return render(request, 'order_service.html', context={'form': form})
    if request.method == 'POST':
        bound_form = MessageForm(request.POST)

        if bound_form.is_valid():
            new_message = bound_form.save()
            return redirect(reverse('index'))
        return render(request, 'order_service.html', context={'form': bound_form})

@login_required
def messages_list(request):
    messages = Message.objects.filter(is_active=True)

    return render(request, 'messages_list.html', context={'messages': messages})
