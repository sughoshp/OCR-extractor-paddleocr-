import os
import pandas as pd
from paddleocr import PaddleOCR

# We use the standard OCR engine. 
# It's robust and avoids the Table-Structure memory bug.
engine = PaddleOCR(
    use_angle_cls=True, 
    lang='en', 
    use_gpu=False, 
    show_log=False
)

IMG_PATH = r"C:\Users\sanke\Downloads\Gemini_Generated_Image_fibi51fibi51fibi.png"

def run_stable_extraction():
    # ... (keep your existing check for path)
    
    result = engine.ocr(IMG_PATH, cls=True)
    
    # Store everything in a list
    extracted_lines = []
    for line in result[0]:
        coords = line[0]
        text = line[1][0]
        # Use the top-left Y-coordinate to identify the "row"
        y_center = coords[0][1] 
        extracted_lines.append((y_center, text))

    # Sort by Y-coordinate (top to bottom)
    extracted_lines.sort(key=lambda x: x[0])

    print("\n📊 --- FORMATTED TABLE PREVIEW ---")
    
    # Simple grouping: if Y-coordinates are within 10 pixels, 
    # treat them as the same row
    current_y = -100
    row_text = ""
    
    for y, text in extracted_lines:
        if abs(y - current_y) > 10:  # New row detected
            if row_text:
                print(row_text)
            row_text = text
            current_y = y
        else:
            row_text += f" | {text}" # Append to same row
            
    print(row_text) # Print the last line
    if not os.path.exists(IMG_PATH):
        print(f"❌ File not found: {IMG_PATH}")
        return

    print("🚀 Running Stable OCR (Bypassing Table-Structure Bug)...")
    
    try:
        # Get raw OCR results
        result = engine.ocr(IMG_PATH, cls=True)

        if not result or result[0] is None:
            print("🧐 No content found in image.")
            return

        # result[0] contains list of [[coordinates], (text, confidence)]
        data = []
        for line in result[0]:
            text = line[1][0]
            confidence = line[1][1]
            # Get the top-left Y coordinate to help sort rows
            y_coord = line[0][0][1] 
            data.append({"y": y_coord, "text": text})

        # Basic logic to group text by their vertical (Y) position
        # This roughly reconstructs the table rows
        df_raw = pd.DataFrame(data)
        
        # Sort by vertical position
        df_raw = df_raw.sort_values(by="y")

        print("\n--- EXTRACTED CONTENT ---")
        for index, row in df_raw.iterrows():
            print(row['text'])
            
        print("\n✅ Successfully extracted text line-by-line.")

    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    run_stable_extraction()