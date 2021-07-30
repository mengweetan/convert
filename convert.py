# on mac
# pip install -r requirements.txt
#brew install poppler

from pdf2image import convert_from_path
from PIL import Image
import os

source_directory = "source"
target_directory = "target"
source_path = "{}/{}".format(os.getcwd(),source_directory)

#p = os.listdir(spource_path)

#print (p)
#images = convert_from_path(file_name)

#print (images)


for filename in os.listdir(source_path):
   #with open(os.path.join(spource_path, filename), 'r') as f:
    #print (f)# open in readonly mode
    try:
        if "pdf" in filename:
            images = convert_from_path(os.path.join(source_path, filename))
            im = []
            for i in range(len(images)):

              # Save pages as images in the pdf
              images[i].save('temp'+ str(i) +'.jpg', 'JPEG')
              im.append(Image.open('temp'+ str(i) +'.jpg'))
              os.remove('temp'+ str(i) +'.jpg')
            pdf_filename = "{}_{}.pdf".format(filename,"new")
            im_list = im[1:]
            im[0].save(os.path.join(target_directory, pdf_filename), "PDF" ,resolution=100.0, save_all=True, append_images=im_list)
    except Exception as e:
        print (e)
        pass
