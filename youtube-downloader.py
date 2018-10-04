from youtube_functions import *
import pyperclip,os,subprocess

args=initialize_terminal_parser()
urls=pyperclip.paste()
valid_urls=get_youtube_urls(urls)
if valid_urls:
    if args.type.lower() in ['mp4','webm']:
        for url in valid_urls:
            download_video(url[0].strip(),args.type,args.quality,True,args.output)
        convert_vtt_to_srt(path)
    elif args.type.lower() in ['mp3','ogg']:
        for url in valid_urls:
            download_audio(url[0].strip(),args.type,args.quality,args.output)
    subprocess.Popen(r"explorer /select,'"+args.output+"'")