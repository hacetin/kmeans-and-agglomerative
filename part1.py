from skimage.io import imread, imsave, imshow, show
from skimage.color import label2rgb
from cluster import KMeans, distortion
from os.path import normpath

data_path = normpath("./sample/sample.jpg")
img = imread(data_path)
img2 = img.reshape(img.shape[0] * img.shape[1], img.shape[2])

# Cluster for K = 2,3,...,20 to calculate distortion
distortion_dict = {}
for cluster_count in range(2, 21):
    km = KMeans(cluster_count)
    V, cmap = km.fit(img2)

    distortion_dict[cluster_count] = distortion(img2, cmap, V)
    print(distortion_dict)

    # For K = 2,4,6,8,16 show or save the image to see differences
    if cluster_count in [2, 4, 6, 8, 16]:
        cmap2 = cmap.reshape(img.shape[0], img.shape[1])
        clustered_image = label2rgb(label=cmap2, colors=V / 255)

        # imshow(clustered_image)
        # show()

        # To save as bitmap, use '.bmp' instead of '.png'
        result_path = normpath("result/kmeans_" + str(cluster_count) + "_clusters.png")
        imsave(result_path, clustered_image)
