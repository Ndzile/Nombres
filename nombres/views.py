from django.shortcuts import render, redirect

# Create your views here.

# Vue pour que le secrétaire national de JPC crée un membre du bureau régional
from nombres.form import MembreBureauRegionalForm, MembreCoordinationLocaleForm
from nombres.models import CoordinationLocale, Jeune, MembreBureauRegional
from django.contrib.auth import authenticate, login, logout


def connexion(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to successful login page (e.g., homepage)
            return redirect('dash')
        else:
            # Invalid login credentials
            error_message = 'Invalid username or password'
    else:
        error_message = None
    return render(request, 'login.html', {'error_message': error_message})


def creer_membre_bureau_regional(request):
    if request.method == 'POST':
        form = MembreBureauRegionalForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dash')
    else:
        form = MembreBureauRegionalForm()
    return render(request, 'bureau_regional/creer.html', {'form': form})


# Vue pour qu'un membre du bureau régional crée un membre d'une coordination locale

def creer_membre_coordination_locale(request):
    if request.method == 'POST':
        form = MembreCoordinationLocaleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dash')
    else:
        form = MembreCoordinationLocaleForm()
    return render(request, 'coordination_locale/creer.html', {'form': form})


# Vue pour qu'un membre du bureau régional affiche les membres des coordinations locales qu'il a créées

def membres_coordination_locale(request, id):
    coordination_locale = CoordinationLocale.objects.get(id=id)
    membres = Jeune.objects.filter(coordination_locale=coordination_locale)
    return render(request, 'coordination_locale/membres.html', {'membres': membres})


# Vue pour qu'un membre de la coordination locale affiche les membres de sa coordination locale

def membres_coordination_locale(request):
    if not request.user.is_authenticated:
        return redirect('connexion')

    coordination_locale = request.user.coordination_locale
    membres = Jeune.objects.filter(coordination_locale=coordination_locale)

    return render(request, 'coordination_locale/membres.html', {'membres': membres})


def membres_bureau_regional(request):
    membres = MembreBureauRegional.objects.all()
    # ... (optional processing or filtering)
    return render(request, 'bureau_regional/membres.html', {'membres': membres})


def dash(request):
    context = {}  # Create an empty context dictionary

      # You can optionally add logic here to populate the context with data
      # For example, to display recent news or announcements:
      # recent_news = News.objects.order_by('-created_at')[:3]  # Get 3 recent news items
      # context['recent_news'] = recent_news

    return render(request, 'index.html', context)


def signout(request):
    logout(request)
    # messages.success(request, 'Logout successfully!')
    return redirect('connexion')