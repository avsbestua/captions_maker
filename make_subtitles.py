from moviepy import VideoFileClip, CompositeVideoClip, TextClip
import whisper

def format_time(seconds):
    hours = int(seconds // 3600)
    minutes = int((seconds % 3600) // 60)
    seconds_only = seconds % 60
    return f"{hours:02d}:{minutes:02d}:{seconds_only:06.3f}".replace('.', ',')

text_clips = [] #list for text clips

#model loading
video = VideoFileClip('video.mp4')

#extracting audio from video
audio = video.audio
audio.write_audiofile('audio.mp3')

model = whisper.load_model("medium")

#extracting text from audio
result = model.transcribe('audio.mp3', language='uk')
print("Transcribed")

srt_content = []
subtitle_number = 1

for seg in result["segments"]:
    start_time = format_time(seg["start"])
    end_time = format_time(seg["end"])
    text = seg["text"].strip()

    text = text[:-1] if text[-1] in ['.', ','] else text

    srt_content.append(str(subtitle_number))
    srt_content.append(f"{start_time} --> {end_time}")
    srt_content.append(text)
    srt_content.append("")

    subtitle_number += 1

with open('subs.srt', 'w', encoding='utf-8') as f:
    f.write('\n'.join(srt_content))

print("Subtitle file was created")
