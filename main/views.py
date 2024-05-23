from django.shortcuts import render
from .models import mainNew, professionNew, tablePrice

def index(request):
    main_news = mainNew.objects.all()
    professions = professionNew.objects.all()
    prices = tablePrice.objects.all()

    context = {
        'main_news': main_news,
        'professions': professions,
        'prices': prices,
    }
    return render(request, 'main/news/index.html', context)
