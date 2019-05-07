from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.urls import reverse
from django.core.paginator import Paginator

from religion.forms import MessageForm
from religion.models import *

def index(request):
    services = Service.objects.all()
    return render(request, 'index.html', context={'services': services})


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
    on_page = 3
    text = None
    if request.method == 'POST':
        id = request.POST.get('id')
        message = Message.objects.filter(id=id).first()
        # print(message.is_active)
        message.is_active = False
        message.save()
        text = 'Ви виконали прохання "' + message.service.name + '" для ' + message.user

    messages = Message.objects.filter(is_active=True)

    paginator = Paginator(messages, on_page)
    page_number = request.GET.get('page', 1)
    page = paginator.get_page(page_number)

    is_paginated = page.has_other_pages()

    if page.has_previous():
        prev_url = '?page={}'.format(page.previous_page_number())
    else:
        prev_url = ''

    if page.has_next():
        next_url = '?page={}'.format(page.next_page_number())
    else:
        next_url = ''

    context = {
        'page': page,
        'is_paginated': is_paginated,
        'next_url': next_url,
        'prev_url': prev_url,
        'text': text,

    }

    return render(request, 'messages_list.html', context=context)
