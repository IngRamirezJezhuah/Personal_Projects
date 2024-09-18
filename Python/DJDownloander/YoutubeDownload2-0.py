from pytube import YouTube

def download_video_yt(url,path='Descargas'):
    try:
        yt = YouTube(url)
        yt.streams.get_highest_resolution().download(output_path=path)
        print("Descarga completa!")
    except Exception as e:
        print("ERROR:", e)

url_video= input("Dame el url de YT: ")
path = input("Dame el lugar de descarga: ")
print("descargando... ...")
download_video_yt(url_video, path)