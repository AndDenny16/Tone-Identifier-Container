
import boto3
from PIL import Image, ImageFilter
import io 
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use("Agg")
import librosa
import numpy as np 
import os

BUCKET_NAME = os.getenv("BUCKET_NAME")

def save_to_s3(image, username):
    print(username)
    print(image)
    s3 = boto3.client('s3')
    image_buffer = io.BytesIO()
    image.save(image_buffer, format="PNG")
    image_buffer.seek(0) 
    response = s3.put_object(
        Bucket=BUCKET_NAME,
        Key=f"userdata/{username}/latest.png",
        Body=image_buffer,
        ContentType="image/png"  # Set the correct content type
    )

def create_image(audio_data, img_size):
    """
    Take in a audio file and create a Image of size (225, 225,3) for input into CNN
    Input: 
        audio_data: base64 encoded audio file
        img_size: (225, 225)

    Output:
        Image of size (225, 225,3)
    """
    audio_file = io.BytesIO(audio_data)
    audio, sr = librosa.load(audio_file, sr=16000)
    print("Librosa load complete")

    trimmed_audio, _ = librosa.effects.trim(audio, top_db=10)
    mel_spectrogram = librosa.feature.melspectrogram(y=trimmed_audio, sr=sr, n_fft=2048, hop_length=16, n_mels=64, fmin=50, fmax=350)
    mel_spectrogram_db = librosa.power_to_db(mel_spectrogram, ref=np.max)
    print("Librosa Spectrogram Complete")

    fig = plt.figure(figsize=(2.5, 2.5)) 
    plt.axis('off')  
    librosa.display.specshow(mel_spectrogram_db, sr=sr, hop_length=16, x_axis=None, y_axis=None)
    plt.tight_layout(pad=0)
    fig.canvas.draw() 
    w, h = fig.canvas.get_width_height()
    img_array = np.frombuffer(fig.canvas.buffer_rgba(), dtype=np.uint8)
    img_array = img_array.reshape((h,w,4)) 
    image = Image.fromarray(img_array).resize(img_size).convert('RGB')
    image = image.filter(ImageFilter.GaussianBlur(radius=1))
    print("Image Spectrogram Complete")

    img_array = np.array(image).astype(np.float32)/255.0
    print(img_array)
    plt.close(fig)
    return image, img_array