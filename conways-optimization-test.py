import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from PIL import Image

path = ""
path = 'sp.png'

if path != "":
    im = Image.open(path)
    im_grey = im.convert('L') # convert the image to *greyscale*
    data = np.array(im_grey)

    for (x,y), value in np.ndenumerate(data):
        if data[x][y] == 255:
            data[x][y] = 0
        else:
            data[x][y] = 1

    data = np.zeros(data.shape) + np.floor(data)
else:
    data = np.floor(np.random.random(size=(28, 28)) + 0.5)

data2 = np.zeros(data.shape)
data3 = np.ones(data.shape)

plt.rcParams['toolbar'] = 'None'

cmap = "Greys"

plt.imshow(data, cmap=cmap, interpolation='nearest')
plt.axis("on")

def animate(t):
    global data
    global data2
    global data3
    global anim
    global i

    data2 = np.zeros(data.shape)
    skip = 0

    for (x,y), value in np.ndenumerate(data):
        i = 0
        if data3[x][y] > 0:
            try:
                if data[x][y-1] == 1:
                    i += 1
            except:
                None
            try:
                if data[x+1][y-1] == 1:
                    i += 1
            except:
                None
            try:
                if data[x+1][y] == 1:
                    i += 1
            except:
                None
            try:
                if data[x+1][y+1] == 1:
                    i += 1
            except:
                None
            try:
                if data[x][y+1] == 1:
                    i += 1
            except:
                None
            try:
                if data[x-1][y+1] == 1:
                    i += 1
            except:
                None
            try:
                if data[x-1][y] == 1:
                    i += 1
            except:
                None
            try:
                if data[x-1][y-1] == 1:
                    i += 1
            except:
                None

            if data[x][y] == 1:
                if i == 2 or i == 3:
                    data2[x][y] = 1
            else:
                if i == 3:
                    data2[x][y] = 1

            if data2[x][y] == 1 or i > 0:
                try:
                    data3[x][y] = 1
                except:
                    None
                try:
                    data3[x][y - 1] = 1
                except:
                    None
                try:
                    data3[x + 1][y - 1] = 1
                except:
                    None
                try:
                    data3[x + 1][y] = 1
                except:
                    None
                try:
                    data3[x + 1][y + 1] = 1
                except:
                    None
                try:
                    data3[x][y + 1] = 1
                except:
                    None
                try:
                    data3[x - 1][y + 1] = 1
                except:
                    None
                try:
                    data3[x - 1][y] = 1
                except:
                    None
                try:
                    data3[x - 1][y - 1] = 1
                except:
                    None
            else:
                data3[x][y] = 0
                try:
                    data3[x][y - 1] += 0
                except:
                    None
                try:
                    data3[x + 1][y - 1] += 0
                except:
                    None
                try:
                    data3[x + 1][y] += 0
                except:
                    None
                try:
                    data3[x + 1][y + 1] += 0
                except:
                    None
                try:
                    data3[x][y + 1] += 0
                except:
                    None
                try:
                    data3[x - 1][y + 1] += 0
                except:
                    None
                try:
                    data3[x - 1][y] += 0
                except:
                    None
                try:
                    data3[x - 1][y - 1] += 0
                except:
                    None

        else:
            skip += 1

    try:
        print("Skipped %s of %s total cells (so %s neighbor checks skipped)." %
              ("{0:.0%}".format(skip/(data.shape[0]*data.shape[1])), data.shape[0]*data.shape[1], skip*8))
    except:
        None
    data = data2 + data3
    plt.imshow(data, cmap=cmap, interpolation='nearest')
    data = data2
    #plt.savefig("C:/Users/scgry/Desktop/mat/" + str(t) + ".png")


ani = animation.FuncAnimation(plt.gcf(), animate, interval=250)

plt.show()
