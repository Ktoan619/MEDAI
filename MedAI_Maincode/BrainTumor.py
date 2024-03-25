from PIL import Image, ImageDraw
from transformers import pipeline
import datasets
import gradio as gr

from datasets import load_dataset

data = load_dataset("Francesco/brain-tumor-m2pbp")
pipe = pipeline("object-detection", model="DunnBC22/yolos-tiny-Brain_Tumor_Detection")

def Processing(Image):
  
  data = pipe(Image)

  for Num_of_Label in range(len(data)) :

    Color_List = ["purple", "yellow", "blue"]

    box = data[Num_of_Label]['box']

    xmin, ymin, xmax, ymax = box['xmin'], box['ymin'], box['xmax'], box['ymax']

    draw = ImageDraw.Draw(Image)

    draw.rectangle([xmin, ymin, xmax, ymax], outline= Color_List[Num_of_Label], width=2)

  return Image
def create_brain_tumor_detect() :
  with gr.Blocks() as Brain_Tumor_Detect:
      gr.Markdown("Kiểm Tra Khối U Não")
      with gr.Row():

          inp = gr.Image(label = "Xin Nhập Ảnh Vào", type = 'pil')
          out = gr.Image(label = "Kết Quả", type = 'pil')

      btn = gr.Button("Xử Lý")
      btn.click(fn=Processing, inputs= inp, outputs=out)
  return Brain_Tumor_Detect

