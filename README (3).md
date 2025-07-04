# 🤟 Real-Time Sign Language Recognition

A real-time Sign Language Recognition system built using Python, OpenCV, and machine learning that detects and classifies hand gestures from live webcam input. This project aims to bridge communication gaps for individuals with hearing or speech impairments by translating sign language into readable text.

## 🔍 Project Overview

This project captures hand gestures using a webcam, processes them through a trained machine learning model, and outputs the corresponding letter or word in real-time. The application provides a user-friendly interface and supports real-time text and audio output, enhancing accessibility and user experience.

## 💡 Features

- 📷 **Real-Time Detection** using OpenCV
- 🧠 **Custom Trained Model** for gesture classification
- 💬 **Text & Audio Output** for interpreted gestures
- 🖐️ **Alphabet Gesture Recognition (A-Z)**
- 🗣️ **Text-to-Speech Integration** for verbalizing output
- ✅ Simple, responsive GUI for user interaction

## 🛠️ Tech Stack

- **Programming Language**: Python
- **Libraries Used**:
  - OpenCV
  - TensorFlow / Keras
  - NumPy
  - Tkinter
  - pyttsx3 (Text-to-Speech)
- **Model Training**:
  - Custom CNN model trained on sign language datasets
  - Data preprocessing and augmentation handled in Python

## 🚀 How to Run

1. **Clone the Repository**

```bash
git clone https://github.com/NaiduBalakrishna/Real-Time-Sign-Language-Recognition.git
cd Real-Time-Sign-Language-Recognition
```

2. **Install Dependencies**

```bash
pip install -r requirements.txt
```

3. **Run the Application**

```bash
python main.py
```

> Make sure your webcam is connected and functioning properly.

## 📁 Project Structure

```
Real-Time-Sign-Language-Recognition/
│
├── dataset/                 # Hand gesture image dataset
├── model/                   # Trained CNN model files
├── static/                  # UI assets (icons, images)
├── utils/                   # Helper functions and utilities
├── main.py                  # Entry point of the application
├── train_model.py           # Script to train the CNN model
├── requirements.txt         # Python dependencies
└── README.md                # Project documentation
```

## 📊 Dataset

- The dataset includes images for sign language alphabets (A–Z).
- Images are preprocessed for model training and stored in the `dataset/` folder.

## 🔉 Output

- The application detects hand gestures and displays the recognized letter on-screen.
- Additionally, it uses a text-to-speech engine to read the letter aloud.

## 🎯 Future Improvements

- Extend gesture recognition to support words and phrases
- Improve accuracy with a larger, more diverse dataset
- Implement multilingual audio output
- Deploy as a web or mobile app

## 🙋‍♂️ Author

**Bala Krishna**  
Developer & AI Enthusiast  
[GitHub](https://github.com/NaiduBalakrishna) | [LinkedIn](https://www.linkedin.com/in/NaiduBalakrishna/) 

## 🤝 Contributing

Contributions are welcome! If you have ideas or improvements, feel free to open an issue or submit a pull request.

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

> Empowering communication through the power of AI and accessibility.
