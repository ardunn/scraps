
# converting 5.0+ H264-encoded videos to 4.0+ H264-encoded videos, for PS4 playback
ffmpeg -i input.mp4 -c:v libx264 -profile:v high -level:v 4.0 -c:a copy output.mp4
