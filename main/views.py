from .models import mainNew, professionNew, tablePrice
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from .forms import PhoneForm
from django.contrib import messages


def index(request):
    if request.method == 'POST':
        form = PhoneForm(request.POST)
        if form.is_valid():
            phone = form.cleaned_data['phone']
            send_mail(
                'Новый номер телефона',
                f'Получен новый номер телефона: {phone}',
                'fittqboshenkiy@gmail.com',
                ['fittsqboshenkiy@gmail.com'],
                fail_silently=False,
            )
            messages.success(request, 'Номер телефона успешно отправлен!')
            return redirect('index')
        else:
            messages.error(request, 'Ошибка в отправке номера телефона. Попробуйте снова.')
    else:
        form = PhoneForm()

    main_news = mainNew.objects.all()
    professions = professionNew.objects.all()
    prices = tablePrice.objects.all()

    context = {
        'main_news': main_news,
        'professions': professions,
        'prices': prices,
        'form': form,
    }
    return render(request, 'main/news/index.html', context)
