from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def calc(request):
    return render(request, 'home.html', {'titles': 'prmaod'})


def jod(request):
    a = int(request.POST['text1'])
    b = int(request.POST['text2'])
    addition = a + b
    return render(request, 'result.html', {'result': addition})
