import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

def decrypt_img() :
    try:
        img = Image.open('its.jpg')
    except IOError:
        print("Can not open")
        return
    
    imgs = np.array(img)
    avg = 0
    
    for i in imgs:
        for j in i:
            avg = (int(j[0]) + int(j[1]) + int(j[2]))//3
            j[0]=avg
            j[1]=avg
            j[2]=avg

    plt.imshow(imgs)
    plt.show()
    
    n_img = Image.fromarray(imgs)
    n_img.save('cypu.jpg')
    
decrypt_img()

#two = [[1, 2, 3], [2, 4, 5], [5, 4, 5]]
#for i in two:
#    for j in i:
#        print(j, end=" ")
#    print()
    
#print(5//3)
#print(6//3)
#print(round(6/3))