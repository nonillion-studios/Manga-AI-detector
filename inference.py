## this is an example code , feel free to edit it
from ultralytics import YOLO
import argparse

def main():
    parser = argparse.ArgumentParser(description="Manga YOLOv11 Inference")
    parser.add_argument("--source", type=str, required=True, help="Path to input manga image or directory")
    parser.add_argument("--conf", type=float, default=0.25, help="Confidence threshold")
    parser.add_argument("--save", action="store_true", help="Save the annotated image")
    args = parser.parse_args()

    # Load fine-tuned weights
    model = YOLO("best.pt")

    # Run detection
    results = model.predict(source=args.source, conf=args.conf, save=args.save)
    
    print(f"Inference completed! Check 'runs/detect/predict' for results.")

if __name__ == "__main__":
    main()
