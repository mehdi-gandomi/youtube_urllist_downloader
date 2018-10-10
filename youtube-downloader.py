
from youtube_functions import *
import pyperclip,os,subprocess

args=initialize_terminal_parser()
urls=pyperclip.paste()
valid_urls=get_youtube_urls(urls)
if valid_urls:
    if args.type.lower() in ['mp4','webm']:
        if args.ask_for_download:
            for url in valid_urls:
                clear_scr()
                qualityItag=str(qualitiesItags[args.type.lower()][args.quality.lower()])
                print("Fetching filename for url : {}".format(url[0]))
                fileName=get_file_name(url[0],qualityItag)
                print("\n The Video name is : {} ".format(fileName))
                choice=input("do you want to download this file ? (yes or no) : ")
                if choice.lower()=="yes":
                    download_video(url[0].strip(),args.type,args.quality,True,args.output)
        else:
            for url in valid_urls:
                download_video(url[0].strip(),args.type,args.quality,True,args.output)
        # convert_vtt_to_srt(path)
    elif args.type.lower() in ['m4a','ogg','mp3']:
        for url in valid_urls:
            download_audio(url[0].strip(),args.type,args.output)
    else:
        print("error")
    subprocess.Popen(r'explorer /open,"{}"'.format(args.output))