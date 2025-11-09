# FaceRecognition  
*A lightweight real-time face detection & recognition app built with OpenCV / Node.js*

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE) [![Build Status](https://img.shields.io/badge/build-passing-brightgreen.svg)](https://github.com/Raziel206/FaceRecognition)  

---

## 🚀 Project Overview  
This project provides a straightforward solution for detecting and recognising faces in real time, using a webcam or camera feed.  
It’s built with Node.js and `opencv4nodejs` (OpenCV bindings for Node), making it easy to extend, integrate and deploy.

---

## ✨ Features  
- Real-time face detection using your camera  
- Face recognition against a set of known faces  
- Lightweight and modular — easy to integrate into other systems  
- Works across Windows / macOS / Linux (given OpenCV dependencies are satisfied)  
- Can be extended for access control, attendance systems, automation projects, creative installations  

---

## 🧩 Tech Stack  
- **Language**: Python 
- **Library**: `opencv-python` `mediapipe`  
- **Platform**: Desktop / Laptop (with webcam or external camera)  
- **License**: MIT – free to use, modify, distribute  

---

## 🛠️ Installation & Setup  
### Run these commands in order 
```bash
git clone https://github.com/Raziel206/FaceRecognition.git
cd FaceRecognition
pip install virtualenv
py -3.10 -m venv env
.\env\Scripts\activate
pip install -r requirements.txt
python -m src.main
```
---
## 📁 Project Structure
```bash
FaceRecognition/
│
├── src/                  
│   ├── untils/
│   │      ├── __init__.py
│   │      ├── face_detect.py
│   │      ├── hand_detect.py
│   │      └── resizing.py
│   ├── __init__.py
│   ├── extension.py      
│   └── main.py    
├── .gitignore
├── LICENSE
├── README.md
└── requirements.txt
```
---
## 🎯 Use-Cases & Ideas

- Use for door-access system: recognise authorised faces and trigger unlock

- Use in classrooms / events: automatic attendance marking based on face recognition

- Use for creative installations: trigger lights/sounds when certain faces appear

- Use as a base for more advanced CV/AI work: add expression recognition, mask-detection, emotion tracking
---
## 🔍 Tips & Best Practices

- Use clear, well-lit face images for each person in the known_faces/ folder — good data = better recognition

- Maintain consistent lighting and camera position for best accuracy

- Tune recognition thresholds (in recognizer logic) to avoid false positives or mis-matches

- If performance is slow, reduce camera resolution or adjust detection/recognition parameters

- Always test with multiple poses (frontal, slight angles) and different lighting conditions
---
## 🤝 Contributing

Contributions are welcome and appreciated!  
Whether it's a bug fix, feature improvement, documentation enhancement, or optimization — every contribution helps.

### ✅ How to contribute

1. **Fork** the repository  
2. Create a **new branch** for your feature or bug fix  
   ```bash
   git checkout -b feature-name
   ```
3. Make a pull request, or if it is a big change/major feature, create an issue.   
---
## 🙏 Acknowledgements

[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://www.python.org/)
[![OpenCV](https://img.shields.io/badge/OpenCV-Powered-orange.svg)](https://opencv.org/)
[![MediaPipe](https://img.shields.io/badge/MediaPipe-Used%20for%20Face%20Recognition-brightgreen.svg)](https://mediapipe.dev/)
[![Made With ❤️](https://img.shields.io/badge/Made%20With-%E2%9D%A4-red.svg)](#)

This project wouldn't be possible without the amazing work of the open-source community.  
Special thanks to:

- [**Python**](https://www.python.org) — for being simple, fast to prototype, and developer-friendly  
- [**OpenCV**](https://opencv.org) — the core of real-time computer vision in this project  
- [**MediaPipe**](https://chuoling.github.io/mediapipe) — for efficient, production-ready face detection & landmark tracking  
- All contributors of these libraries for keeping them free, powerful, and evolving

> **Huge respect to open-source.** This project stands on the shoulders of giants.
---
## 📜 License

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

This project is licensed under the [**MIT License**](https://opensource.org/license/mit).

___
