from moviepy import ImageClip, AudioFileClip
import os
from .config import OUTPUT_DIR


def make_video_from_audio(
    image_path,
    audio_path,
    output_filename="mixtape_vid.mp4"
):
    # -------- VALIDATIONS --------
    if not os.path.exists(image_path):
        raise FileNotFoundError("Image not found: " + image_path)

    if not os.path.exists(audio_path):
        raise FileNotFoundError("Audio not found: " + audio_path)

    # -------- OUTPUT PATH --------
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    output_path = os.path.join(OUTPUT_DIR, output_filename)

    # -------- SAME AS NOTEBOOK --------
    audio = AudioFileClip(audio_path)

    video = (
        ImageClip(image_path)
        .with_duration(audio.duration)
        .with_audio(audio)
    )

    video.write_videofile(
        output_path,
        fps=1
    )

    # -------- CLEANUP --------
    video.close()
    audio.close()

    return output_path
