function findRecipe() {
    // Pobierz składniki z pola textarea o id "ingredients"
    const ingredients = document.getElementById('ingredients').value;

    // Zakoduj składniki do formatu URL i wyślij zapytanie do serwera
    fetch(`/find_recipe/?ingredients=${encodeURIComponent(ingredients)}`)
    .then(response => response.json())
    .then(data => {
        // Wyświetl wyniki w elemencie o id "result"
        const resultDiv = document.getElementById('result');
        resultDiv.innerHTML = data.recipes.join('<br>');
    })
    .catch(error => {
        console.error('Error:', error);
        document.getElementById('result').textContent = 'An error occurred';
    });
}