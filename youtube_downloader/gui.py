import tkinter as tk
import argparse

from tkinter import messagebox, filedialog

from youtube_downloader import YoutubeDownloader

parser = argparse.ArgumentParser(description="Simple YouTube Downloader in python3 w/ GUI :)",
                                 usage="\ngit clone [link]\n"
                                       "mkvirtualenv youtube-downloader\n"
                                       "pip install -r requirements.txt\n"
                                       "python gui.py\n",
                                 epilog="Happy hacking :)")

args = parser.parse_args()


class YoutubeDownloaderWithGUI(object):
    def __init__(self, root):
        self.root = root
        self.root.geometry("1280x1920")
        self.root.resizable(True, True)
        self.root.title("YouTube Video Downloader")
        self.root.config(background="#ded3d3")
        self.link = tk.StringVar()
        self.file_path = tk.StringVar()
        self.video_or_audio = tk.StringVar()
        self._type = tk.StringVar()
        self.resolution = tk.StringVar()
        self.create_gui()
        self.root.mainloop()

    def _create_text_entries(self, text, bg, label_row,
                             label_column, entry_width,
                             entry_row, entry_column,
                             text_variable, column_span=None):
        label = tk.Label(self.root, text=text, bg=bg)
        label.grid(row=label_row, column=label_column, pady=5, padx=5)
        self.root.linkText = tk.Entry(self.root, width=entry_width, textvariable=text_variable)
        self.root.linkText.grid(row=entry_row, column=entry_column, pady=5, padx=5, columnspan=column_span)

    def _create_button(self, text, command, width, bg, row, column, padx, pady):
        button = tk.Button(self.root, text=text, command=command, width=width, bg=bg)
        button.grid(row=row, column=column, pady=pady, padx=padx)

    def create_gui(self):
        self._create_text_entries(text="YouTube link  :", bg="#eb4034", label_row=1, label_column=0,
                                  entry_width=55, text_variable=self.link, entry_row=1, entry_column=1,
                                  column_span=2)

        self._create_text_entries(text="Video/Audio  :", bg="#eb4034", label_row=2, label_column=0,
                                  entry_width=55, text_variable=self.video_or_audio, entry_row=2, entry_column=1,
                                  column_span=2)

        self._create_text_entries(text="Type  :", bg="#eb4034", label_row=3, label_column=0,
                                  entry_width=55, text_variable=self._type, entry_row=3, entry_column=1,
                                  column_span=2)

        self._create_text_entries(text="Resolution  :", bg="#eb4034", label_row=4, label_column=0,
                                  entry_width=55, text_variable=self.resolution, entry_row=4, entry_column=1,
                                  column_span=2)

        self._create_text_entries(text="Destination    :", bg="#eb4034", label_row=5, label_column=0,
                                  entry_width=55, text_variable=self.file_path, entry_row=5, entry_column=1)

        self._create_button(text="Browse", command=self.browse, width=10, bg="#05E8E0",
                            row=5, column=2, padx=1, pady=1)

        self._create_button(text="Download", command=self.download, width=20, bg="#05E8E0",
                            row=6, column=2, pady=3, padx=3)

    def browse(self):
        download_directory = filedialog.askdirectory(initialdir="YOUR DIRECTORY PATH")
        self.file_path.set(download_directory)

    def download(self):
        try:
            youtube_downloader = YoutubeDownloader(link=self.link.get(), video_or_audio=self.video_or_audio.get(),
                                                   _type=self._type.get(), resolution=self.resolution.get(),
                                                   file_path=self.file_path.get())
            downloaded_file_path = youtube_downloader.download()
            messagebox.showinfo("SUCCESS", "DOWNLOADED IN: " + downloaded_file_path)
        except:
            messagebox.showinfo("ERROR", "DOWNLOAD FAILED")


if __name__ == "__main__":
    gui = YoutubeDownloaderWithGUI(tk.Tk())
