from django.shortcuts import render
import json

# Create your views here.


def index(request):
    context = {
        'title': 'Geekshop'
    }
    return render(request, 'mainapp/index.html', context)


def products(request):
    context = {
        'title': 'Geekshop - Каталог',
        'products': [
            {
                'img': 'Adidas-hoodie.png',
                'name': 'Худи черного цвета с монограммами adidas Originals',
                'price': 6090,
                'card_text': 'Мягкая ткань для свитшотов. Стиль и комфорт – это образ жизни.',
                'button': 1
            },
            {
                'img': 'Blue-jacket-The-North-Face.png',
                'name': 'Синяя куртка The North Face',
                'price': 23725,
                'card_text': 'Гладкая ткань. Водонепроницаемое покрытие. Легкий и теплый пуховый наполнитель. ткань для свитшотов. Стиль и комфорт – это образ жизни.',
                'button': 1
            },
            {
                'img': 'Brown-sports-oversized-top-ASOS-DESIGN.png',
                'name': 'Коричневый спортивный oversized-топ ASOS DESIGN',
                'price': 3390,
                'card_text': 'Материал с плюшевой текстурой. Удобный и мягкий.',
                'button': 0
            },
            {
                'img': 'Black-Nike-Heritage-backpack.png',
                'name': 'Черный рюкзак Nike Heritage',
                'price': 2340,
                'card_text': 'Плотная ткань. Легкий материал.',
                'button': 0
            },
            {
                'img': 'Black-Dr-Martens-shoes.png',
                'name': 'Черные туфли на платформе с 3 парами люверсов Dr Martens 1461 Bex',
                'price': 13590,
                'card_text': 'Гладкий кожаный верх. Натуральный материал.',
                'button': 0
            },
            {
                'img': 'Dark-blue-wide-leg-ASOs-DESIGN-trousers.png',
                'name': 'Темно-синие широкие строгие брюки ASOS DESIGN',
                'price': 2890,
                'card_text': 'Легкая эластичная ткань сирсакер Фактурная ткань.',
                'button': 0
            }
        ]
    }

    with open("mainapp/fixtures/products.json", "w") as write_file:
        json.dump(context, write_file)

    return render(request, 'mainapp/products.html', context)
