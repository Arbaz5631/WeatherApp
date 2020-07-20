from django.shortcuts import render
import requests
import pyodbc


conn = pyodbc.connect(

    'Driver={SQL Server Native Client 11.0};'
    'Server=(local);'
    'Database=login;'
    'Trusted_Connection=yes;'
)


def create(conn, name, email, number, desc):
    cursor = conn.cursor()
    cursor.execute('insert into Cloud_users values(?,?,?,?);',
                   (name, email, number, desc))
    conn.commit()
    conn.close()


# Create your views here.
def index(request):
    if request.method == 'POST':
        search = request.POST.get('search', '')
        url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=0e12ad84dbe4bcdf1f980898cfc713b6'
        city = search
        r= requests.get(url.format(city)).json()
        city_weather={'city': city,
            'temperature': (((r['main']['temp'])-32)//1.8),
            'temperature_min':(((r['main']['temp_min'])-32)//1.8),
            'temperature_max':(((r['main']['temp_max'])-32)//1.8),
            'wind_speed':(r['wind']['speed']),
            'description': r['weather'][0]['description'],
            'icon': r['weather'][0]['icon']
        }
        return render(request,'weatherApp/search.html',{'city_weather':city_weather})

    else:
        url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=0e12ad84dbe4bcdf1f980898cfc713b6'
        city1 = 'Farrukhabad'
        city2 = 'Kanpur'
        city3 = 'Jaipur'
        city4 = 'Noida'
        city5 = 'Delhi'
        city6 = 'Ghaziabad'
        r1 = requests.get(url.format(city1)).json()
        r2 = requests.get(url.format(city2)).json()
        r3 = requests.get(url.format(city3)).json()
        r4 = requests.get(url.format(city4)).json()
        r5 = requests.get(url.format(city5)).json()
        r6 = requests.get(url.format(city6)).json()
        city_weather = {'Farrukhabad': {
            'city': city1,
            'temperature': (((r1['main']['temp'])-32)//1.8),
            'description': r1['weather'][0]['description'],
            'icon': r1['weather'][0]['icon'],
        },
            'Kanpur': {
            'city': city2,
            'temperature': (((r2['main']['temp'])-32)//1.8),
            'description': r2['weather'][0]['description'],
            'icon': r2['weather'][0]['icon'],
        },
            'Jaipur': {
            'city': city3,
            'temperature': (((r3['main']['temp'])-32)//1.8),
            'description': r3['weather'][0]['description'],
            'icon': r3['weather'][0]['icon'],
        },
            'Noida': {
            'city': city4,
            'temperature': (((r4['main']['temp'])-32)//1.8),
            'description': r4['weather'][0]['description'],
            'icon': r4['weather'][0]['icon'],
        },
            'Delhi': {
            'city': city5,
            'temperature': (((r5['main']['temp'])-32)//1.8),
            'description': r5['weather'][0]['description'],
            'icon': r5['weather'][0]['icon'],
        },
            'Ghaziabad': {
            'city': city6,
            'temperature': (((r6['main']['temp'])-32)//1.8),
            'description': r6['weather'][0]['description'],
            'icon': r6['weather'][0]['icon'],
        }
        }
        param = {'city_weather': city_weather}

        return render(request, 'weatherApp/index.html', param)


def contact(request):
    if request.method == "POST":
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        number = request.POST.get('number', '')
        desc = request.POST.get('desc', '')
        create(conn, name, email, number, desc)

    return render(request, 'weatherApp/contact.html')


def about(request):

    return render(request, 'weatherApp/about.html')
