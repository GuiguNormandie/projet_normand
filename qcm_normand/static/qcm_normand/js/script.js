document.querySelectorAll('.option input').forEach(input => {
    input.addEventListener('change', function() {
        // Retire la classe 'selected' de toutes les options
        document.querySelectorAll('.option').forEach(option => {
            option.classList.remove('selected');
        });
        // Ajoute la classe 'selected' à l'option choisie
        this.parentElement.classList.add('selected');
    });
});

document.querySelector('.submit-button').addEventListener('click', function() {
    const selectedOption = document.querySelector('input[name="question1"]:checked');
    
    if (!selectedOption) {
        alert("Veuillez sélectionner une réponse.");
        return;
    }

    const isValid = selectedOption.getAttribute('data-valid') === "True";

    // Appliquer les couleurs aux réponses
    document.querySelectorAll('.option').forEach(option => {
        const optionInput = option.querySelector('input');
        if (optionInput.getAttribute('data-valid') === "True") {
            option.classList.add('correct'); // Classe pour la bonne réponse
        }
    });

    // Colore en rouge si une mauvaise réponse est sélectionnée
    if (!isValid) {
        selectedOption.parentElement.classList.add('incorrect');
    } else {
        selectedOption.parentElement.classList.add('correct');
    }

    // Régénérer une autre question après 2 secondes
    setTimeout(() => {
        // Logique pour régénérer la question ici (ex: rafraîchir la page ou appeler une fonction)
        window.location.reload(); // Exemple de rechargement de la page
    }, 2000);
});
