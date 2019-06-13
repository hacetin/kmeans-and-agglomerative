from skimage.io import imsave
from skimage.color import label2rgb
import timeit


def save_image(V, cmap, shape, name):
    cmap2 = cmap.reshape(shape[0], shape[1])
    clustered_image = label2rgb(label=cmap2, colors=V / 255)

    imsave(name, clustered_image)


class CodeTimer:
    def __init__(self, message=""):
        self.message = message

    def __enter__(self):
        print(self.message)
        self.start = timeit.default_timer()

    def __exit__(self, exc_type, exc_value, traceback):
        self.took = timeit.default_timer() - self.start
        print("Finished in {0:0.5f} secs.".format(self.took))
