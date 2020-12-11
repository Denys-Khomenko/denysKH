from django.shortcuts import render


def index(request):
    return render(request, "index.html")


def cv(request):
    return render(request, 'firstapp/cv.html')


def cv_ua(request):
    return render(request, 'firstapp/cv_ua.html')
