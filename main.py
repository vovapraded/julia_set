import numpy as np
import matplotlib.pyplot as plt

# Параметры
width, height = 4000, 4000
dpi = 1200
re_min, re_max = -1.5, 1.5
im_min, im_max = -1.5, 1.5
escape_radius = 2


width_in_inches = width / dpi
height_in_inches = height / dpi

fig, ax = plt.subplots(figsize=(width_in_inches, height_in_inches), dpi=dpi)
plt.subplots_adjust(left=0, right=1, top=1, bottom=0)
ax.axis('off')

def make_and_show(c, max_iter):
    image = np.zeros((height, width))
    for y in range(height):
        for x in range(width):
            # Преобразование координат пикселя в комплексное число z
            re = re_min + (x / width) * (re_max - re_min)
            im = im_min + (y / height) * (im_max - im_min)
            z = complex(re, im)

            iteration = 0
            while abs(z) <= escape_radius and iteration < max_iter:
                z = z ** 2 + c
                iteration += 1

            if iteration < max_iter:
                image[y, x] = iteration
            else:
                image[y, x] = 0
    # Отображение изображения
    plt.imshow(image, cmap='inferno', extent=(re_min, re_max, im_min, im_max))
    fig.savefig(f"{c}{max_iter}.png", dpi=dpi)



make_and_show(complex(-0.7, 0.27015),256)
# make_and_show(complex(0.5251993, 0.5251993),256)
# make_and_show(complex(-0.8, 0.156), 300)
# make_and_show(complex(0.285, 0.01), 200)
# make_and_show(complex(0.45, -0.1428), 400)
# make_and_show(complex(-0.70176, -0.3842), 500)
# make_and_show(complex(-0.835, -0.2321), 300)
# make_and_show(complex(0.285, 0.013), 250)
make_and_show(complex(-0.4, 0.6), 600)
make_and_show(complex(-0.8, 0.156), 400)
make_and_show(complex(0.355, 0.355), 350)
make_and_show(complex(-0.75, 0.11), 700)
make_and_show(complex(-0.75, 0.15), 500)
make_and_show(complex(-0.72, 0.1), 550)
make_and_show(complex(0.37, 0.1), 300)
make_and_show(complex(0.355, 0.355), 400)
make_and_show(complex(-0.624, 0.435), 350)