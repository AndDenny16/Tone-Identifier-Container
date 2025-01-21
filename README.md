# **Tone Buddy**  
## **Step 2: Dockerized ML Model**

---

## **Overview**
This step involves containerizing the Tone Buddy ML model to make it portable, scalable, and easy to deploy. The ML model predicts Mandarin tones by processing spectrograms of audio input. Docker ensures that the model and its dependencies are packaged together for consistent performance across environments.

---

## **Features**
- **ML Model Deployment:** A pretrained Convolutional Neural Network (CNN) for Mandarin tone classification.
- **Audio Processing Pipeline:** Converts user audio into spectrograms before feeding them to the model.
- **Dockerized Solution:** Simplifies deployment and ensures consistent runtime environments.
- **RESTful API Integration:** Accepts audio input, processes it, and returns tone predictions.

---

## **Workflow**
1. **Input:** User submits an audio recording of a monosyllabic mandarin word
2. **Preprocessing:** Audio is converted into a spectrogram using **Librosa**. Image is converted into (1, 225, 225, 3) format.
3. **Model Prediction:** The spectrogram is fed into the pretrained ML model, which outputs the predicted tone.
4. **Output:** The result is sent back as a response (e.g., "Tone 3").

---

## **Project Components**
### **1. ML Model**
- **Framework:** TensorFlow (.keras) file
- **Input Format:** Spectrograms (1, 225, 225, 3)
- **Output:** Predicted tone (1st, 2nd, 3rd, or 4th)


### **2. DockerFile** 
- **Base Image** Python 3.11


### **3. Requirements** 
- requirements.txt - list of dependencies


##**To Run the Container**

- To Run on your locally

`` docker build -t <your_desired_name> ``

`` docker run -it -p <desired_port>:5000 <your_desired_name> ``
  


