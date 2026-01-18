from pytubefix import YouTube
from pytubefix.cli import on_progress
from pyfiglet import Figlet
import yt_dlp
from colorama import Fore, Style, init

init(autoreset=True)


while True :
    f = Figlet(font='slant')
    print(f.renderText('DOWNTOOL'))
    print(Fore.GREEN + "Made By Wass")
    print("-----------------------------------------------")
    choice = input("\n 1 | Youtube MP4 \n 2 | SoundCloud \n 3 | Youtube MP3 \n\n Choisir votre type de téléchargement : ")
    if choice == '1':
        link = input("Coller le lien de votre vidéo : ")
        yt = YouTube(link, on_progress_callback=on_progress)
        print(yt.title)

        ys = yt.streams.get_highest_resolution()
        ys.download()
    elif choice == '2':
        link = str(input("Coller le lien de votre son : "))
        def download_soundcloud(url, output_path="Téléchargements"):
            ydl_opts = {
                'format': 'bestaudio/best',
                'outtmpl': f'{output_path}/%(title)s.%(ext)s',
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': '192',
                }],
                'quiet': False,
            }

            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])
        download_soundcloud(link)
    elif choice == '3':
        link = input("Coller le lien de votre vidéo : ")
        yt = YouTube(link, on_progress_callback=on_progress)
        print(yt.title)

        ys = yt.streams.get_audio_only()
        ys.download()

