from django.shortcuts import redirect, render
from riotwatcher import LolWatcher
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from .models import Build

 
lol_watcher = LolWatcher('RGAPI-a5e4a44e-5b80-40b4-815b-353384cd7e41')
my_region = 'na1'

# Getting the latest version of the game from Data Dragon
versions = lol_watcher.data_dragon.versions_for_region(my_region)
champions_version = versions['n']['champion']
# Let's get some champions now
champion_list = lol_watcher.data_dragon.champions(champions_version, True)
champions = champion_list.get('data')
item_list = lol_watcher.data_dragon.items(champions_version)
items = item_list.get('data')


# Create your views here.
def home(request):
    return render(request, 'home.html', {'champions': champions})

def about(request):
    return render(request, 'about.html')

def detail(request, name):
    champ = champions.get(name)
    builds = Build.objects.filter(champion=name)
    print(builds)
    return render(request, 'detail.html', {'champ': champ, 'builds': builds})

def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
        else:
            error_message = 'Signup input invalid - Please try again!'
    form = UserCreationForm()
    context = {'form': form, 'error': error_message}
    return render(request, 'registration/signup.html', context)