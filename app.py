from flask import Flask, render_template, request, send_file, jsonify
import os
from main import download_youtube_video

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/download', methods=['POST'])
def download():
    try:
        url = request.form['url']
        if not url:
            return jsonify({'error': 'URL is required'}), 400
            
        downloaded_file = download_youtube_video(url)
        if downloaded_file:
            return jsonify({
                'success': True,
                'message': 'Video downloaded successfully!',
                'filename': os.path.basename(downloaded_file)
            })
        else:
            return jsonify({'error': 'Failed to download video'}), 500
            
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True) 