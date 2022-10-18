from django.shortcuts import render
from riotwatcher import LolWatcher, ApiError
 
lol_watcher = LolWatcher('RGAPI-a5e4a44e-5b80-40b4-815b-353384cd7e41')
my_region = 'na1'

# Getting the latest version of the game from Data Dragon
versions = lol_watcher.data_dragon.versions_for_region(my_region)
champions_version = versions['n']['champion']
# Let's get some champions now
champion_list = lol_watcher.data_dragon.champions(champions_version)
champions = champion_list.get('data')


# Create your views here.
def home(request):
    return render(request, 'home.html', {'champions': champions})

def about(request):
    return render(request, 'about.html')

def detail(request, name):
    champ = champions.get(name)
    print(champ)
    return render(request, 'detail.html', {'champ': champ})