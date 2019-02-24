from skimage.io import imread, imsave, imshow, show
from skimage.color import label2rgb
from cluster import AgglomerativeClustering, distortion
from os.path import normpath

data_path = normpath("./sample/sample.jpg")
img = imread(data_path)
img2 = img.reshape(img.shape[0] * img.shape[1], img.shape[2])

batch_size = 100

cluster_count = 33
agg = AgglomerativeClustering(cluster_count=cluster_count)
V, cmap = [], []
start_index = 0
while start_index < img2.shape[0]:
    print(start_index, "/", img2.shape[0])
    end_index = start_index + batch_size - cluster_count
    V, cmap = agg.fit(img2[start_index:end_index])
    start_index = end_index

cmap2 = cmap.reshape(img.shape[0], img.shape[1])
clustered_image = label2rgb(label=cmap2, colors=V / 255)

# Cluster for K = 2,3,...,32 to calculate distortion
distortion_dict = {}
for cluster_count in range(32, 1, -1):
    agg.cluster_count = cluster_count
    V, cmap = agg.fit([])

    distortion_dict[cluster_count] = distortion(img2, cmap, V)
    print(distortion_dict)

    # For K = 2,4,6,8,16 show or save the image to see differences
    if cluster_count in [2, 4, 6, 8, 16]:
        cmap2 = cmap.reshape(img.shape[0], img.shape[1])
        clustered_image = label2rgb(label=cmap2, colors=V / 255)

        # imshow(clustered_image)
        # show()

        # To save as bitmap, use '.bmp' instead of '.png'
        result_path = normpath("result/agg_" + str(cluster_count) + "_clusters.png")
        imsave(result_path, clustered_image)