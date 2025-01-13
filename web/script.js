document.getElementById('searchForm').addEventListener('submit', function(event) {
    event.preventDefault();
    
    const query = document.getElementById('searchInput').value;
    
    // Clear previous results
    document.getElementById('instagram-links').innerHTML = '';
    document.getElementById('youtube-links').innerHTML = '';
    document.getElementById('tweets-links').innerHTML = '';
    document.getElementById('web-links').innerHTML = '';

    // Fetch results from your backend
    fetch('/search', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ query: query })
    })
    .then(response => response.json())
    .then(data => {
        // Assuming your backend returns data categorized by source
        data.instagram.forEach(link => {
            const anchor = document.createElement('a');
            anchor.href = link.url;
            anchor.textContent = link.title;
            document.getElementById('instagram-links').appendChild(anchor);
        });

        data.youtube.forEach(link => {
            const anchor = document.createElement('a');
            anchor.href = link.url;
            anchor.textContent = link.title;
            document.getElementById('youtube-links').appendChild(anchor);
        });

        data.tweets.forEach(link => {
            const anchor = document.createElement('a');
            anchor.href = link.url;
            anchor.textContent = link.title;
            document.getElementById('tweets-links').appendChild(anchor);
        });

        data.webpages.forEach(link => {
            const anchor = document.createElement('a');
            anchor.href = link.url;
            anchor.textContent = link.title;
            document.getElementById('web-links').appendChild(anchor);
        });
    })
    .catch(error => {
        console.error('Error fetching search results:', error);
    });
});
