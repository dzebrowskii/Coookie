function findRecipe() {

    var ingredients = document.getElementById('ingredients').value;

    fetch(`/find_recipe/?ingredients=${encodeURIComponent(ingredients)}`)
    .then(response => response.json())
    .then(data => {
        const resultDiv = document.getElementById('result');
        resultDiv.innerHTML = data.recipes.join('<br>');
    })
    .catch(error => {
        console.error('Error:', error);
        document.getElementById('result').textContent = 'An error occurred';
    });
}