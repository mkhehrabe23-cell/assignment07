!apt update
!apt install ffmpeg -y
!pip install yt-dlp pydub

# Commented out IPython magic to ensure Python compatibility.
# %%writefile 102303221.py
# import sys
# import os
# from yt_dlp import YoutubeDL
# from pydub import AudioSegment
# import warnings
# warnings.filterwarnings("ignore")
# 
# def download_videos(singer, number):
#     print(f"Downloading {number} songs of {singer}...")
# 
#     os.makedirs("downloads", exist_ok=True)
# 
#     ydl_opts = {
#         'format': 'bestaudio/best',
#         'outtmpl': 'downloads/%(title)s.%(ext)s',
#         'postprocessors': [{
#             'key': 'FFmpegExtractAudio',
#             'preferredcodec': 'mp3',
#             'preferredquality': '192',
#         }],
#         'noplaylist': True
#     }
# 
#     search_query = f"ytsearch{number}:{singer} songs"
# 
#     with YoutubeDL(ydl_opts) as ydl:
#         ydl.download([search_query])
# 
# def cut_and_merge(duration, output_file):
#     print("Cutting and merging audios...")
# 
#     combined = AudioSegment.empty()
# 
#     for file in os.listdir("downloads"):
#         if file.endswith(".mp3"):
#             path = os.path.join("downloads", file)
#             audio = AudioSegment.from_mp3(path)
#             trimmed = audio[:duration * 1000]
#             combined += trimmed
# 
#     combined.export(output_file, format="mp3")
#     print("Mashup created:", output_file)
# 
# def main():
#     if len(sys.argv) != 5:
#         print("Usage: python <program.py> <SingerName> <NumberOfVideos> <AudioDuration> <OutputFileName>")
#         sys.exit(1)
# 
#     singer = sys.argv[1]
#     number = int(sys.argv[2])
#     duration = int(sys.argv[3])
#     output_file = sys.argv[4]
# 
#     if number <= 10:
#         print("NumberOfVideos must be greater than 10")
#         sys.exit(1)
# 
#     if duration <= 20:
#         print("AudioDuration must be greater than 20")
#         sys.exit(1)
# 
#     download_videos(singer, number)
#     cut_and_merge(duration, output_file)
# 
# if __name__ == "__main__":
#     main()
#

!python 102303221.py "Sharry Maan" 15 25 mashup.mp3
