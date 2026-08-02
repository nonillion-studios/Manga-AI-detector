<div align="center">

# 🦾 Manga AI Detector (YOLOv11)

<img src="https://img.shields.io/badge/YOLO-v11-00FFFF?style=for-the-badge&logo=ultralytics&logoColor=white" />
<img src="https://img.shields.io/badge/PyTorch-EE4C2C?style=for-the-badge&logo=pytorch&logoColor=white" />
<img src="https://img.shields.io/badge/Python-3.8%2B-3776AB?style=for-the-badge&logo=python&logoColor=white" />
<img src="https://img.shields.io/badge/License-MIT-green.svg?style=for-the-badge" />

A custom fine-tuned **YOLOv11** object detection model engineered for manga, manhwa, and comic book document analysis.

</div>

---

## 🔍 Model Information & Classes

This model is fine-tuned to detect **4 structural elements** across manga page layouts:
* 🖼️ **Panels:** Individual story frames and borders.
* 💬 **Speech Bubbles:** Speech, thought, and text containers.
* 📝 **Text:** In-panel and out-of-panel dialog text.
* 💥 **SFX:** Stylized onomatopoeia, sound effects, and stylized lettering.

---

## 💻 Hardware Requirements

### Minimum (Inference Only)
* **CPU:** Quad-Core Intel / AMD Processor
* **RAM:** 8 GB DDR4
* **GPU:** Optional (NVIDIA GTX 1050 / 1650 or higher with 4 GB VRAM recommended for fast real-time batch processing)
* **Storage:** 2 GB available space

### Recommended (Training & Fine-Tuning)
* **CPU:** 8-Core Intel / AMD Processor
* **RAM:** 16 GB+ DDR4 / DDR5
* **GPU:** NVIDIA RTX 3060 / 4060 or higher (8 GB+ VRAM with CUDA support)
* **CUDA Support:** CUDA 11.8 or CUDA 12.x

---

## ⚙️ Installation

### 1. Clone the Repository
```bash
git clone [https://github.com/nonillion-studios/Manga-AI-detector.git](https://github.com/nonillion-studios/Manga-AI-detector.git)
cd Manga-AI-detector
2. Install Dependencies
Ensure you have Python 3.8+ installed, then run:

Bash


pip install -r requirements.txt
📂 Repository Layout
To maintain a clean working directory, organize your local setup as follows:

Plaintext


Manga-AI-detector/
├── best.pt            # Pre-trained fine-tuned weights
├── inference.py       # Helper python script for batch predictions
├── train.py           # Script to fine-tune the model on your own dataset
├── requirements.txt   # Dependencies
├── .gitignore         # Git ignore file
└── README.md          # Documentation
🚀 Usage & Inference
Option A: Via Python Script (inference.py)
Run inference directly on any image or folder using the included python script:

Bash


python inference.py --source "path/to/manga_page.jpg" --conf 0.25 --save
Option B: Via Ultralytics CLI
Bash


yolo detect predict model=best.pt source="path/to/manga_page.jpg" conf=0.25 save=True
Option C: Python In-Code Usage
Python


from ultralytics import YOLO

# Load fine-tuned weights
model = YOLO("best.pt")

# Predict on an image
results = model.predict(source="manga_page.png", conf=0.25)

# Show results
for result in results:
    result.show()
🎯 How to Fine-Tune (Train on Custom Dataset)
If you wish to continue training or adapt best.pt to your own manga dataset, follow these steps:

1. Prepare your dataset configuration (data.yaml)
Create a file named data.yaml defining your paths and classes:

YAML


path: ./dataset # root dataset directory
train: images/train
val: images/val

names:
  0: panel
  1: bubble
  2: text
  3: sfx
2. Fine-tune using best.pt
Create a train.py script or run the code below to fine-tune using transfer learning:

Python


from ultralytics import YOLO

# Load your fine-tuned model as the base
model = YOLO("best.pt")

# Fine-tune on your new dataset
results = model.train(
    data="data.yaml",
    epochs=50,
    imgsz=640,
    batch=16,
    device=0  # Use GPU 0 (or 'cpu' if no GPU is available)
)
Alternatively, run via the CLI:

Bash


yolo detect train model=best.pt data=data.yaml epochs=50 imgsz=640 batch=16
📄 License
This project is licensed under the MIT License. You are free to use, modify, and distribute this software for personal and commercial projects. See the LICENSE file for full terms.

👤 Author & Support
Maintained by Nonillion Studios.

For bug reports, questions, or feature requests, feel free to open an issue or pull request on the repository.
