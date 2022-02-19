from django.http import HttpResponse
from django.shortcuts import render


def home_page(request):
    return render(request, 'mate/index.html')

from .models import Pidrov

def index(request):
    news = Pidrov.objects.all()
    return render(request,  'news/index.html' , {'news when we talk about jasur': news, 'title': 'The list that tells all the news about Jasur'})

# from django.http import HttpResponse
#
# def home (request):
#     return HttpResponse ('<h1>Hello world, It is crazy</h1>')
#
# # def test (request):
# #     return HttpResponse ('<h1>Its just test. Dont worry, I dont want to hack the pentagon</h1>')
# #
# # def pozdravlenie (request):
# #     return HttpResponse ('<h1>Так как ты не знаешь англ (я про асрора, не про тебя еврей) я напишу на русском.'
# #                          'Rahmat, что не поленился проверить мой код</h1>')
# #
# # def The_End (request):
# #     return HttpResponse ('<h1>This is where I fucking ended. This is fucking end, goodbye. (Тут слишком много слов'
# #                          'fucking, потому что Асрор не шпрехает по английски</h1>')
