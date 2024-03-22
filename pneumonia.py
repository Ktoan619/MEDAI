def update(image_processed):
  #image = Image.open(image_url)
  #image_processed = image.convert("RGB")
  processor = AutoImageProcessor.from_pretrained("nickmuchi/vit-finetuned-chest-xray-pneumonia")
  model = AutoModelForImageClassification.from_pretrained("nickmuchi/vit-finetuned-chest-xray-pneumonia")
  inputs = processor(images=image_processed, return_tensors="pt")
  outputs = model(**inputs)
  logits = outputs.logits
  predicted_class_idx = logits.argmax(-1).item()

  for class_name, score in zip(model.config.id2label.values(), logits.softmax(dim=-1).squeeze().tolist()):
    ket_qua = "Viêm phổi"
    if (class_name == "NORMAL") :
      ket_qua = "Bình thường"
    if (model.config.id2label[predicted_class_idx] == class_name) :
      return (f"{ket_qua}: {score:.0%}")
  return ""
