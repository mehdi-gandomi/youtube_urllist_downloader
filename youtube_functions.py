# from merge_functions import merge_subtitle
# from vtt_to_srt import convert_all_vtts
import re,os,argparse,glob
#https://www.youtube.com/watch?v=IWXfwv00M-g

clear_scr=lambda : os.system("cls") if os.name=="nt" else os.system("clear")
qualitiesItags={
  "mp4":{
    "360p":18,
    "hd720":22,
    "720p":136,
    "480p":135,
    "240p":133
  },
  "webm":{
      "medium":43,

  }
}

def initialize_terminal_parser():
    parser = argparse.ArgumentParser(description='Download Movie And Tv Show Subtitle. Note : you have to type show name in quotes!!')
    parser.add_argument("-t","--type",help="Type of the file to download (mp4 or webm or 3gp)",default="mp4")
    parser.add_argument("-q","--quality",help="file quality to download",default=None)
    parser.add_argument("-o","--output",help="file path to dowloadfile into it ",default="./")
    return parser.parse_args()


def get_youtube_urls(urls):
    youtubeRegex=re.compile("((http(s)?:\/\/)?((w){3}.)?youtu(be|.be)?(\.com)?\/.+)+")
    if youtubeRegex.search(urls):
        return youtubeRegex.findall(urls)
def get_file_name(url,basePath,quality):
    fileName=os.popen("youtube-dl "+url+" -f "+quality+" --get-filename --skip-download --restrict-filename -o %(title)s.%(ext)s").read()
    return os.path.join(basePath,fileName)
def get_subtitle_filename(filename,basePath):
    return os.path.join(basePath,os.path.splitext(filename)[0]+".en.srt")
def generate_new_filename(fileName,basePath):
    return os.path.join(basePath,os.path.splitext(fileName)[0]+"-with-subtitle"+os.path.splitext(fileName)[1])

def download_video(url,type,quality,subtitle=False,path=False):
    create_path_if_not_exists(path)
    command="youtube-dl {} --restrict-filename".format(url)
    qualityItag=None
    if type.lower() in ['mp4','webm']:
        qualityItag=str(qualitiesItags[type.lower()][quality.lower()])
        command+=" -f "+qualityItag
    if subtitle:
        command+=" --write-sub --sub-format srt --sub-lang en --convert-subs srt"
    if path:
        command+=r" -o "+path+"\\%(title)s.%(ext)s"
    clear_scr()
    os.system(command)
    fileName=get_file_name(url,path,qualityItag)
    # merge_subtitle(fileName,get_subtitle_filename(fileName,path),generate_new_filename(fileName,path))
# def download_audio(url,type,quality,path):

def create_path_if_not_exists(path):
    if not os.path.exists(path):
        os.makedirs(path)
def convert_vtt_to_srt(path):
    vttFiles=glob.glob(path+"\\*.vtt")
    for vtt in vttFiles:
        os.rename(vtt,vtt.replace(".vtt",".srt"))