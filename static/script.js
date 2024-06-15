document.getElementById('instagramForm').addEventListener('submit', function(event) {
    event.preventDefault(); // Prevent form submission
    var instagramUrl = document.getElementById('instagramUrl').value;
    fetch('/download', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ url: instagramUrl })
    })
    .then(response => response.json())
    .then(data => {
        if (data.media_url) {
            var link = document.createElement('a');
            link.href = data.media_url;
            link.innerText = 'Click here to download the video';
            link.download = true;
            document.getElementById('downloadedContent').innerHTML = '';
            document.getElementById('downloadedContent').appendChild(link);
        } else {
            document.getElementById('downloadedContent').innerText = data.error;
        }
    })
    .catch(error => {
        console.error('Error:', error);
        document.getElementById('downloadedContent').innerText = 'An error occurred while processing your request.';
    });
});
