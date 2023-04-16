from PIL import Image
import glob

filenames = glob.glob("data_two/*")

count = 1
for filename in filenames:
    outfile = "data_two_resized/im_" + str(count) + ".jpg"
    count += 1
    im = Image.open(filename)
    im = im.resize((408, 307), Image.Resampling.LANCZOS)
    im.save(outfile)