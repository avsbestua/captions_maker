from moviepy import VideoFileClip, CompositeVideoClip, TextClip
import whisper
import tqdm

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

pbar = tqdm.tqdm(total=len(result["segments"]))

for seg in result["segments"]:
    text = seg["text"].strip()

    text = text[:-1] if text[-1] else text

    txt_clip = TextClip(
        text=text,
        font='font.ttf',
        font_size=32,
        color='white',
        stroke_color='black',
        stroke_width=2,
        method='caption',
        size=(video.w, 600)
    ).with_start(seg["start"]).with_end(seg["end"]).with_position('bottom')

    text_clips.append(txt_clip)

    pbar.update(1)

pbar.close()

final_vid = CompositeVideoClip([video, *text_clips])

final_vid.write_videofile('result.mp4', codec='h264_nvenc', threads=4)