from django.shortcuts import render, redirect, get_object_or_404
from .forms import LoginForm
from .models import Etudiant
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth.models import User



# Create your views here.

# @login_required
# def about(request):
#     if request.method == 'POST':
#         dataform = LoginForm(request.POST)
#         if dataform.is_valid():
#             dataform.save()

# #     # cne = request.POST.get('cne')
# #     # cin = request.POST.get('cin')
# #     # data = Login(cne=cne, cin=cin)
# #     # data.save()

#     return render(request, 'guichet/about.html')

# @login_required
# def about(request):
    
#     # Enregistrer le formulaire de connexion s'il a été soumis
#     if request.method == 'POST':
#         dataform = LoginForm(request.POST)
#         if dataform.is_valid():
#             dataform.save()
#     # Récupérer le nom d'utilisateur à partir de la session
#     cne = request.session.get('cne')

#     # Vérifier si l'utilisateur est connecté
#     if not cne:
#         return redirect('about')

#     # Rediriger vers la vue suivre
#     return redirect('suivre')



# @login_required
# def about(request):
#     if request.method == 'POST':
#         dataform = LoginForm(request.POST)
#         if dataform.is_valid():
#             dataform.save()
#             return redirect('suivre')
#     else:
#         dataform = LoginForm()
    
#     return render(request, 'guichet/about.html', {'form': dataform})

@login_required
def about(request):
    if request.method == 'POST':
        # récupérer les informations de connexion
        cne = request.POST.get('cne')
        cin = request.POST.get('cin')

        # authentifier l'utilisateur
        user = authenticate(request, cne=cne, cin=cin)

        if user is not None:
            # connecter l'utilisateur
            login(request, user)
            return redirect('suivre')
        else:
            # afficher un message d'erreur si l'authentification a échoué
            error_message = "Nom d'utilisateur ou mot de passe incorrect."
            context = {'error_message': error_message}
            return render(request, 'guichet/about.html', context)

    return render(request, 'guichet/about.html')

# créer un utilisateur
med = User.objects.create_user(username='1412814223', password='ZT203663')
etudiant = Etudiant.objects.create(cne='1412814223', cin='ZT203663')

@login_required
def suivre(request):
    # afficher les informations de l'étudiant connecté
    etudiant = Etudiant.objects.get(user=request.user)
    context = {'etudiant': etudiant}
    return render(request, 'suivre.html', context)


# @login_required
# def suivre(request):
#     # Récupérer le nom d'utilisateur à partir de la session
#     cne = request.session.get('cne')

#     # Vérifier si l'utilisateur est connecté
#     if not cne:
#         return redirect('about')

#     # Afficher les informations de l'utilisateur
#     context = {'cne': cne}
#     return render(request, 'suivre.html', context)





