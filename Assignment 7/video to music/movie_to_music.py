from moviepy import editor

video = editor.VideoFileClip("file.mp4")
video.audio.write_audiofile("file.mp3")