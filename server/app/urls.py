from . import views
from django.urls import path,include
urlpatterns = [
    #views.index= the function
    #name= name of the template
    # '' mean the index the name that appear in the url website 
    path('',views.index ,name="index"),
    path('Candidat',views.espace_recruteur ,name='espace_recruteur'),
    path('template',views.applicant ,name='applicant'),
    path('profile',views.mon_espace ,name='mon_espace'), #temporaire
    
    
    
    
    
    ]