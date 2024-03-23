def generateBrainTumorAI():
  pipe = pipeline("object-detection", model="DunnBC22/yolos-tiny-Brain_Tumor_Detection")
def Processing(Image):
  Color_List = ["purple", "yellow", "blue"]

  data = pipe(Image)

  data = data

  for Num_of_Label in range(len(Result)) :

    box = data[Num_of_Label]['box']

    xmin, ymin, xmax, ymax = box['xmin'], box['ymin'], box['xmax'], box['ymax']

    draw = ImageDraw.Draw(Image)

    draw.rectangle([xmin, ymin, xmax, ymax], outline= Color_List[Num_of_Label], width=2)

  return Image
