from pytube import YouTube
from pathlib import Path
import os
from pywebio.input import *
from pywebio.output import *

def video_download():
    while True:
        video_link = input("informe a URL: ")
        type_download = input("Escolha o tipo de download que você quer (Dica, escreva musica ou video): ")
        type_download = str(type_download).lower()

        if type_download == 'musica':
            try: 
                # put_text('Fazendo download da música '.title()).style('color: black; font-size: 50px')
                if video_link.split('//')[0] == 'https:':
                    # url input from user
                    yt = YouTube(video_link)

                    ##@ Extract audio with 160kbps quality from video
                    video = yt.streams.filter(abr='160kbps').last()

                    ##@ Downloadthe file
                    out_file = video.download(output_path=Path.cwd())
                    base, ext = os.path.splitext(out_file)
                    new_file = Path(f'{base}.mp3')
                    os.rename(out_file, new_file)
                    ##@ Check success of download
                    if new_file.exists():
                        put_text('Download realizado '.title()).style('color: black; font-size: 50px')
                        print(f'{yt.title} has been successfully downloaded.')
                    else:
                        print(f'ERROR: {yt.title} could not be downloaded!')
                    
                    clear()

            except Exception as e:
                print(e)

        elif type_download == 'video':
            try: 
                if video_link.split('//')[0] == 'https:':
                    put_text('Fazendo download do vídeo '.title()).style('color: black; font-size: 50px')
                    video_url = YouTube(video_link)
                    video = video_url.streams.get_highest_resolution()
                    path_to_download = Path.cwd()
                    out_file = video.download(output_path=Path.cwd())
                    put_text(f'Download realizado {video_url.title}').style('color: black; font-size: 50px')
                    os.startfile(path_to_download)
                    clear()

            except Exception as e:
                print(e)

if __name__ == '__main__':
    video_download()
