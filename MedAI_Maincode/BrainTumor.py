from PIL import Image
from transformers import pipeline
import datasets

from datasets import load_dataset

data = load_dataset("Francesco/brain-tumor-m2pbp")
pipe = pipeline("object-detection", model="DunnBC22/yolos-tiny-Brain_Tumor_Detection")

def Processing(Image, pipe) :
  Color_List = ["purple", "yellow", "blue"]

  data = pipe(Image)

  data = data

  for Num_of_Label in range(len(Result)) :

    box = data[Num_of_Label]['box']

    xmin, ymin, xmax, ymax = box['xmin'], box['ymin'], box['xmax'], box['ymax']

    draw = ImageDraw.Draw(Image)

    draw.rectangle([xmin, ymin, xmax, ymax], outline= Color_List[Num_of_Label], width=2)

  return Image
  
  def create_brain_tumor_detec() :
  with gr.Blocks() as Brain_Tumor_Detect:
      gr.Markdown("Cùng kiểm tra xem bạn có khối u não không nào =)))")
      with gr.Row():

          inp = gr.Image(type = 'pil')
          out = gr.Image(type = 'pil')

      btn = gr.Button("Run")
      btn.click(fn=Processing, inputs= inp, outputs=out)
  return Brain_Tumor_Detect
