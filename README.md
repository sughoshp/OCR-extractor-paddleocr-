# Stable Table OCR 🚀

A resilient, CPU-optimized Python tool to extract text and table data from images using PaddleOCR. This project is specifically engineered to bypass the common "Tensor dimension out of bound" memory errors encountered on Windows environments.



## 🌟 Why this exists
Standard PaddleOCR table extraction (`PPStructure`) often triggers a `RuntimeError` regarding Tensor dimensions on Windows CPUs. This repository provides a stable alternative by utilizing the base OCR engine combined with a vertical-alignment algorithm to reconstruct table rows without crashing the memory.

## 🛠️ Tech Stack
- **Engine:** [PaddleOCR](https://github.com/PaddlePaddle/PaddleOCR)
- **Deep Learning:** PaddlePaddle (CPU-only)
- **Data Analysis:** Pandas
- **Environment:** Python 3.9+ (Managed via `uv`)

## 📦 Installation

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/YOUR_USERNAME/stable-table-ocr.git](https://github.com/YOUR_USERNAME/stable-table-ocr.git)
   cd stable-table-ocr
2.Set up the environment:
We use uv for lightning-fast dependency management. If you don't have it, install it via pip install uv.
uv venv
# Activate the environment
# Windows:
.venv\Scripts\activate
# Mac/Linux:
source .venv/bin/activate

3.Install Dependencies:
uv pip install paddlepaddle paddleocr pandas lxml opencv-python

4.Usage
Place your target image in the downloads folder or project directory.

Update the IMG_PATH variable in main.py.

Run the script:
  uv run main.py



The "Tensor Dimension" Error
If you still see RuntimeError: (PreconditionNotMet) Tensor's dimension is out of bound, it means there is a corrupt model cache.
Fix: Delete the cache folder and restart the script:
rmdir /s /q %USERPROFILE%\.paddleocr

Python Version
This project is verified on Python 3.9. If you are using 3.12+, ensure you are using the latest paddlepaddle version to avoid compatibility shifts.
