import random

from django.http import HttpResponse
from django.template import Context, loader


def index(request):
    num = str(random.randint(1, 999))
    username = "guest" +num
    password = "somewrongpassword"
    template = loader.get_template('chat.html')
    context = Context({
        'user': username,
        'hash':"somepassword",
        })
    return HttpResponse(template.render(context))