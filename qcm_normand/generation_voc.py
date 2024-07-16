# qcm_normand/quiz_generator.py
import random

class Langue:
    def __init__(self, francais="inconnu", normand="inconnu", genre=None):
        self.francais = francais
        self.normand = normand
        self.genre = genre

    def afficher_informations(self):
        print(f"Français: {self.francais}")
        print(f"Normand: {self.normand}")
        print(f"Genre: {self.genre}")

class Mot:
    def __init__(self, mot="inconnu", genre="inconnu", validite=None):
        self.mot = mot
        self.genre = genre
        self.validite = str(validite) if validite is not None else "False"  # Conversion en chaîne

    def afficher_informations_mot(self):
        print(f"Mot: {self.mot}, Genre: {self.genre}, Validité: {self.validite}")

class VocabulaireTest:
    def __init__(self, question=None, reponses=None):
        self.question = question
        self.reponses = reponses

    def afficher_informations_voc(self):
        print("Question:")
        self.question.afficher_informations_mot()
        print("Réponses:")
        for i, reponse in enumerate(self.reponses):
            print(f"Réponse {i + 1}:")
            reponse.afficher_informations_mot()

def traiter_document(chemin_document):
    tableau = []
    with open(chemin_document, 'r', encoding='utf-8') as fichier:
        lignes = fichier.readlines()
        for ligne in lignes:
            mots = ligne.strip().split()
            if len(mots) >= 3:
                normand = mots[0]
                francais = mots[1]
                genre = mots[2]
                langue_objet = Langue(francais, normand, genre)
                tableau.append(langue_objet)
    return tableau

def creer_question_vocabulaire(tableau):
    choix = random.choice(tableau)
    question = Mot(choix.normand, choix.genre)
    reponse_correcte = Mot(choix.francais, choix.genre, "True")
    reponses_incorrectes = []

    while len(reponses_incorrectes) < 2:
        remplissage = random.choice(tableau)
        if remplissage.francais != choix.francais:
            if not any(r.mot == remplissage.francais for r in [reponse_correcte] + reponses_incorrectes):
                reponses_incorrectes.append(Mot(remplissage.francais, remplissage.genre, "False"))

    reponses = [reponse_correcte] + reponses_incorrectes
    random.shuffle(reponses)
    quizz = VocabulaireTest(question, reponses)
    return quizz

