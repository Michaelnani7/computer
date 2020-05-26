from django.shortcuts import render, get_object_or_404
from .models import Laptop, Phones, Computers, Iphones, Quiz
from marketing.models import Signup
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def index(request):
    comps = Laptop.objects.all()
    phons = Phones.objects.all()
    questions = Quiz.objects.all()

    if request.method == "POST":
        email = request.POST["email"]
        new_signup = Signup()
        new_signup.email = email
        new_signup.save()

    paginator = Paginator(comps, 4)
    paginator2 = Paginator(phons, 4)
    page_request_var = 'page'
    page = request.GET.get(page_request_var)

    try:
        paginated_queryset = paginator.page(page)
        paginated_que = paginator2.page(page)

    except PageNotAnInteger:
        paginated_queryset = paginator.page(1)
        paginated_que = paginator2.page(1)

    except EmptyPage:
        paginated_queryset = paginator.page(paginator.num_pages)
        paginated_que = paginator2.page(paginator.num_pages)

    context ={
        'queryset': paginated_queryset,
        'page_request_var': page_request_var,
        'query': paginated_que,
        'questions': questions
    }
    return render(request, 'lappy/index.html', context)


def computers(request):
    pcs = Computers.objects.all()
    paginator = Paginator(pcs, 4)
    page_request_var = 'page'
    page = request.GET.get(page_request_var)

    try:
        paginated_queryset = paginator.page(page)

    except PageNotAnInteger:
        paginated_queryset = paginator.page(1)

    except EmptyPage:
        paginated_queryset = paginator.page(paginator.num_pages)

    context = {
        'queryset': paginated_queryset,
        'page_request_var': page_request_var

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
    paginator = Paginator(sets, 4)
    page_request_var = 'page'
    page = request.GET.get(page_request_var)

    try:
        paginated_queryset = paginator.page(page)

    except PageNotAnInteger:
        paginated_queryset = paginator.page(1)

    except EmptyPage:
        paginated_queryset = paginator.page(paginator.num_pages)
    context = {

        'queryset': paginated_queryset,
        'page_request_var': page_request_var
    }
    return render(request, 'lappy/iphones.html', context)


def phone(request, set_id):
    set = get_object_or_404(Iphones, pk=set_id)
    context = {
        'set': set
    }
    return render(request, 'lappy/phone.html', context)














