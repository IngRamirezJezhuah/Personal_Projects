from flask import Flask, request, jsonify
from pytube import YouTube
import threading
import os

app = Flask(__name__)

def download_video(link, folder):
    def update_progress(stream, chunk, bytes_remaining):
        total_size = stream.filesize
        bytes_downloaded = total_size - bytes_remaining
        percentage_completed = (bytes_downloaded / total_size) * 100
        # Aquí podrías añadir un mecanismo para reportar el progreso si lo deseas

    url = YouTube(link, on_progress_callback=update_progress)
    video = url.streams.get_highest_resolution()
    video.download(output_path=folder)
    return "Descarga completada"

@app.route('/download', methods=['POST'])
def download():
    data = request.json
    link = data.get('link')
    folder = data.get('folder', '.')

    if not link:
        return jsonify({'error': 'No se proporcionó un enlace'}), 400

    # Iniciar la descarga en un hilo separado
    threading.Thread(target=download_video, args=(link, folder)).start()

    return jsonify({'message': 'Descarga iniciada'})

if __name__ == '__main__':
    app.run(debug=True)
