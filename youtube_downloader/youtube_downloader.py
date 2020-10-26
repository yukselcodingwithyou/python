import json

from pytube import YouTube


class YoutubeDownloader(object):

    def __init__(self, link=None, video_or_audio=None,
                 _type=None, resolution=None,
                 file_path=None, file_name=None):
        self.video = YouTube(link)
        self.mime_type = "{0}/{1}".format(video_or_audio, _type)
        self.res = resolution
        self.file_size = 0
        self.file_path = file_path
        self.file_name = file_name

    def detail(self):
        return {
            "title": self.video.title,
            "rating": self.video.rating,
            "length": self.video.length,
            "views": self.video.views,
            "streams": self.all_streams()
        }

    def get_stream(self):
        return self.video.streams.filter(mime_type=self.mime_type, res=self.res)

    def all_streams(self):
        streams = []
        for stream in self.video.streams:
            streams.append({
                "mime_type": stream.mime_type,
                "filesize": stream.filesize,
                "res": stream.resolution,
                "abr": stream.abr,
                "fps": stream.fps
            })
        return streams

    def download(self):
        to_be_downloaded_file = self.get_stream().first()
        self.file_size = to_be_downloaded_file.filesize
        return self.get_stream().first().download(output_path=self.file_path, filename=self.file_name)

    def __str__(self):
        return json.dumps(self.detail())
