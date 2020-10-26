import argparse

from youtube_downloader import YoutubeDownloader

parser = argparse.ArgumentParser(description="Simple YouTube Downloader in python3",
                                 epilog="Happy hacking :)")
parser.add_argument("-l", "--link",
                    help="YouTube link to download",
                    type=str)
parser.add_argument("-v", "--voa",
                    help="'video' or 'audio' values required",
                    type=str)
parser.add_argument("-t", "--type",
                    help="'webm' or 'mp4' values required",
                    type=str)
parser.add_argument("-r", "--resolution",
                    help="resolution of video to be downloaded",
                    type=str)

parser.add_argument("-f", "--file_path",
                    help="download file path of video",
                    type=str)

parser.add_argument("-n", "--file_name",
                    help="download file name of video",
                    type=str)
args = parser.parse_args()

if __name__ == "__main__":
    downloader = YoutubeDownloader(link=args.link, video_or_audio=args.voa,
                                   _type=args.type, resolution=args.resolution,
                                   file_path=args.file_path, file_name=args.file_name)
