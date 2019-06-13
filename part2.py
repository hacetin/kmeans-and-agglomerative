from skimage.io import imread
from cluster import AgglomerativeClustering, distortion
from util import save_image


def run_agg(image_path):
    img = imread(image_path)
    img_array = img.reshape(img.shape[0] * img.shape[1], img.shape[2])

    batch_size = 100
    cluster_count = 17
    step = batch_size - cluster_count

    agg = AgglomerativeClustering(cluster_count=cluster_count)

    # Cluster until 17 clusters
    for start_index in range(0, img_array.shape[0], step):
        print(start_index, "/", img_array.shape[0], end="\r")
        V, cmap = agg.fit(img_array[start_index : start_index + step])

    # Cluster for 2,3,...,16 save the image to see differences
    for cluster_count in range(16, 1, -1):
        agg.cluster_count = cluster_count
        V, cmap = agg.fit([])

        if cluster_count in [2, 4, 6, 8, 16]:
            save_image(
                V, cmap, img.shape, "result/agg_{0}_clusters.png".format(cluster_count)
            )
