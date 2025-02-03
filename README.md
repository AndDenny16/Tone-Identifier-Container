# **Tone Buddy**  
## **Step 2: Dockerized ML Model**

---

<img src="/logolfinal2.png" alt="Project Logo" width="150">

## **Motivation**
As a Computer Science major with a minor in Chinese Studies, I wanted to combine these two fields into a meaningful project. Mandarin Chinese, a tonal language, has **4 tones**, and the meaning of each word depends on using the correct tone.

For example:  
- **媽 (mā)**: 1st tone = *mother*  
- **罵 (mà)**: 4th tone = *scold*  

Messing up a tone can completely change the meaning of a sentence. This is a common challenge for learners of Mandarin. To address this, I created **Tone Buddy**, an app designed to help learners practice their tones using machine learning (ML).

---

## **Project Breakdown**
This repository is **Step 2** of the overall project: containerizing the ML model for the app. Below is an overview of the full project workflow:

### **Step 1: Tone Classification Model**
- Trained a **Deep Convolutional Neural Network (CNN)** on spectrograms of native Mandarin speakers using:
  - **TensorFlow**
  - **Librosa** (for audio preprocessing)
  - **Python**
- The model predicts the tone of a given word based on its audio spectrogram.

### **Step 2: Dockerized ML Model (This Repository)**
- Deployed the pretrained ML model in a custom **Docker container**.
- The container performs the following:
  1. Accepts user audio input.
  2. Converts the audio into a spectrogram.
  3. Feeds the spectrogram into the ML model.
  4. Returns the predicted tone.

### **Step 3: Serverless Backend**
- Built a scalable backend using:
  - **AWS API Gateway** and **AWS Lambda** for serverless functions.
  - **Amazon S3** for storing user data and spectrogram files.
  - **AWS Fargate** for hosting the Docker container.

### **Step 4: Frontend**
- Developed a **React Native frontend** to provide an intuitive and engaging user experience for learners.

---

## **About This Repository**

## **Features**
- **ML Model Deployment:** A pretrained Convolutional Neural Network (CNN) for Mandarin tone classification.
- **Audio Processing Pipeline:** Converts user audio into spectrograms before feeding them to the model.
- **Dockerized Solution:** Simplifies deployment and ensures consistent runtime environments.
- **Flask API:** Accepts audio input, processes it, and returns tone predictions.

---

## **Workflow**
1. **Input:** User submits an audio recording of a monosyllabic mandarin word
2. **Preprocessing:** Audio is converted into a spectrogram using **Librosa**. Image is converted into (1, 225, 225, 3) format.
3. **Save to S3** Spectrogram Image is saved to S3 user
4. **Model Prediction:** The spectrogram is fed into the pretrained ML model, which outputs the predicted tone.
5. **Output:** The result is sent back as a response (e.g., "Tone 3").

---

## **Project Components**
### **1. ML Model** (Not Included > 2GB)
- **Framework:** TensorFlow (.keras) file
- **Input Format:** Spectrograms (1, 225, 225, 3)
- **Output:** Predicted tone (1st, 2nd, 3rd, or 4th) with probability

### **2. DockerFile** 
- **Base Image** Python 3.11
- **Install** Requirements.txt
- **Start** Gunicorn Server


### **3. requirements.txt** 
- requirements.txt - list of dependencies
- `` Pillow
librosa
numpy
matplotlib
tensorflow
boto3
Flask ``

### **3. utils.py**

- **Audio Processing** using Librosa to create a spectrogram with these settings:
    ```
      - (1,225, 225,3) tensor size
  
      - Sample Rate:16000
  
      - Audio Trimmed: top_db: 10
  
      - n_fft=2048, hop_length=16, n_mels=64, fmin=50, fmax=350

    ```
- **Saving to S3 Bucket for UserData***

### **3. app.py**
- **Basic Flask Server** to accept requests
    ```
    /predict - Get a tone/score for a given audio clip
    /health - Health Check
    /info - info on how to make a request

    ```

- **Post Processing** of ML Model output


### **To Test Locally** 
- The repo currently doesn't house the ML Model dude to size restrictions, email me @ anddenny16@gmail.com, if you want to run it
  
  


