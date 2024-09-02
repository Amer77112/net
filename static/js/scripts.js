function performSearch() {
    const query = document.getElementById('query').value;
    fetch(`/search?query=${encodeURIComponent(query)}`)
        .then(response => response.json())
        .then(data => {
            const resultsContainer = document.getElementById('results').querySelector('ul');
            resultsContainer.innerHTML = '';
            data.results.forEach(result => {
                const li = document.createElement('li');
                const link = document.createElement('a');
                link.href = result.link;
                link.textContent = result.title;
                li.appendChild(link);
                resultsContainer.appendChild(li);
            });
        })
        .catch(error => {
            console.error('Error fetching search results:', error);
        });
}
