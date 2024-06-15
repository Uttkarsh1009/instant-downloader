# api/index.py
from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

# Instagram Graph API base URL
INSTAGRAM_API_BASE_URL = 'https://graph.instagram.com'

# Your Instagram access token (replace with your actual access token)
ACCESS_TOKEN = 'YOUR_INSTAGRAM_ACCESS_TOKEN'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/download', methods=['POST'])
def download_instagram_video():
    try:
        instagram_url = request.json.get('url')

        # Extract Instagram post ID from the URL
        post_id = instagram_url.split('/')[-2]

        # Construct URL to fetch post details from Instagram API
        api_url = f'{INSTAGRAM_API_BASE_URL}/{post_id}?fields=id,media_type,media_url&access_token={ACCESS_TOKEN}'

        # Fetch post details from Instagram API
        response = requests.get(api_url)
        data = response.json()

        # Check if the media is a video
        if data['media_type'] == 'VIDEO':
            media_url = data['media_url']
            return jsonify({'media_url': media_url})
        else:
            return jsonify({'error': 'The provided URL does not contain a video.'})

    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
