from django.shortcuts import render

from .models import *


def get_cart(request):
    session_id = request.session.session_key
    if session_id:
        session_id = request.session.create()
    cart = Cart.objects.filter(session_id=session_id)
    if cart.exists():
        cart = cart.first()
    else:
        cart = Cart(session_id=session_id).save()


    return cart 