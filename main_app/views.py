from django.shortcuts import redirect, render
from riotwatcher import LolWatcher
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from .models import Build
from django.views.generic import CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

 
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

@login_required
def detail(request, name):
    champ = champions.get(name)
    builds = Build.objects.filter(champion=name)
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

class BuildCreate(LoginRequiredMixin, CreateView):
    model = Build
    fields = ('build_name', 'mythic', 'boots', 'legendary_1', 'legendary_2', 'legendary_3', 'legendary_4')

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.champion = self.kwargs['name']
        return super().form_valid(form)

class BuildUpdate(LoginRequiredMixin, UpdateView):
    model = Build 
    fields = ('build_name', 'mythic', 'boots', 'legendary_1', 'legendary_2', 'legendary_3', 'legendary_4')

class BuildDelete(LoginRequiredMixin, DeleteView):
    model = Build
    success_url = '/'