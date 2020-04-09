from django.shortcuts import render, get_object_or_404
from .models import Laptop, Phones, Computers, Iphones, Quiz


def index(request):
    comps = Laptop.objects.all()
    phons = Phones.objects.all()
    questions = Quiz.objects.all()
    context ={
        'comps': comps,
        'phons': phons,
        'questions': questions
    }
    return render(request, 'lappy/index.html', context)


def computers(request):
    pcs = Computers.objects.all()
    context = {
        'pcs': pcs
    }
    return render(request, 'lappy/computers.html', context)


def detail(request, pc_id):
    pc = get_object_or_404(Computers, pk=pc_id)
    context = {
        'pc': pc
    }
    return render(request, 'lappy/detail.html', context)


def iphones(request):
    sets = Iphones.objects.all()
    context = {

        'sets': sets
    }
    return render(request, 'lappy/iphones.html', context)


def phone(request, set_id):
    set = get_object_or_404(Iphones, pk=set_id)
    context = {
        'set': set
    }
    return render(request, 'lappy/phone.html', context)














