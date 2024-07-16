# qcm_normand/views.py
from django.shortcuts import render
from .generation_voc import traiter_document, creer_question_vocabulaire

def index(request):
    tableau_langues = traiter_document('C:\\Users\\guill\\OneDrive\\Bureau\\nom commun.txt')
    quiz = creer_question_vocabulaire(tableau_langues)

    return render(request, 'qcm_normand/index.html', {
        'question': quiz.question.mot,
        'options': quiz.reponses,  # Conserver les objets complets
    })


