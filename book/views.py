from django.shortcuts import render
import datetime
from django.http import HttpResponse


def about_me(request):
    if request.method == 'GET':
        return HttpResponse(
            'Привет, меня зовут Мухаммадали, мне 18 лет, '
            'моя цель стать лучшим бэкенд-разработчиком.'
        )


def favorite_writers(request):
    if request.method == 'GET':
        writers = [
            'Чингиз Айтматов',
            'Алыкул Осмонов',
            'Төлөгөн Касымбеков',
            'Түгөлбай Сыдыкбеков',
            'Зуура Сооронбаева',
        ]
        return HttpResponse('<br>'.join(writers))


def current_datetime(request):
    if request.method == 'GET':
        now = datetime.datetime.now()
        return HttpResponse(now.strftime('%d.%m.%Y %H:%M:%S'))
