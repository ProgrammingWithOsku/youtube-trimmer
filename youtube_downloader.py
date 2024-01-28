from pytube import YouTube
from moviepy.editor import VideoFileClip
import os


class YouTubeVideoDownloader:
    def __init__(self, url, start_time, end_time, output_filename):
        self.url = url
        self.start_time = start_time
        self.end_time = end_time
        self.output_filename = output_filename

    def download_and_trim_video(self):
        yt = YouTube(self.url)
        stream = yt.streams.filter(file_extension='mp4').first()
        video_path = stream.download()

        with VideoFileClip(video_path) as video:
            trimmed_video = video.subclip(self.start_time, self.end_time)
            trimmed_video.write_videofile(
                self.output_filename, codec="libx264")

        os.remove(video_path)
