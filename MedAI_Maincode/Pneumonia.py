def update(image_processed):

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

def create_Pneumonia_tab() :
  with gr.Blocks() as demo:
      gr.Markdown("Bạn có viêm phổi không ?")
      with gr.Row():
          inp = gr.Image(label= "Nhập ảnh",type="pil",scale=2)
          out = gr.Label(label="Kết quả dự đoán")
      btn = gr.Button("Go nào")
      btn.click(fn=update, inputs=inp, outputs=out)
  return demo
