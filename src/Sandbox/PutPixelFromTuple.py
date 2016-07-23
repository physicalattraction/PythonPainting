from PIL import Image

W = 200
H = 200
img = Image.new("RGB", (W, H))

pixel_list = [(i%256,i%256,i%256) for i in range(W*H)]
i_pixel = 0
for x in range(W):
    for y in range(H):
        img.putpixel((x, y), pixel_list[i_pixel])
        # img[x,y] = pixel_list[i_pixel]
        i_pixel += 1

img.save('../../img/Sandbox/result.png')