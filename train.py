from ultralytics import YOLO

# Model yükleme
model = YOLO("yolov8n.pt")

# Eğitim
model.train(
    data="data.yaml",
    epochs=50,
    imgsz=640
)
