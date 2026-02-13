# Assignment07

#  YouTube Mashup Generator

##  Description
This is a command-line Python program that creates a mashup of songs from a given singer.  
It downloads multiple songs from YouTube, trims the first few seconds of each, and merges them into one final MP3 file.

##  Tools Used
- Python 3
- yt-dlp (YouTube downloading)
- pydub (Audio processing)
- ffmpeg (Audio conversion)


##  How It Works

1. Takes input from command line:
   - Singer Name
   - Number of Videos (>10)
   - Audio Duration (>20 seconds)
   - Output File Name

2. Downloads N songs using yt-dlp  
3. Converts them to MP3  
4. Cuts first Y seconds from each song  
5. Merges all clips into one mashup file  

##  Usage

python <RollNumber>.py <SingerName> <NumberOfVideos> <AudioDuration> <OutputFileName>
