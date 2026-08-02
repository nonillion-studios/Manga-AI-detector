from ultralytics import YOLO

def main():
    # Load your existing fine-tuned weights as the base
    model = YOLO("best.pt")

    # Start training / fine-tuning on a custom dataset defined in data.yaml
    results = model.train(
        data="data.yaml",  # Path to your dataset configuration file
        epochs=50,         # Number of training epochs
        imgsz=640,         # Image resolution
        batch=16,          # Batch size
        device=0           # GPU ID (or 'cpu' if no GPU available)
    )

if __name__ == "__main__":
    main()
