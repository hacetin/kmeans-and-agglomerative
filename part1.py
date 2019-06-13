from skimage.io import imread
from cluster import KMeans, distortion
from util import save_image


def run_kmeans(data_path):
    img = imread(data_path)
    img2 = img.reshape(img.shape[0] * img.shape[1], img.shape[2])

    # Cluster for K = 2,3,...,16 save the image to see differences
    for cluster_count in range(2, 17):
        km = KMeans(cluster_count)
        V, cmap = km.fit(img2)

        if cluster_count in [2, 4, 6, 8, 16]:
            save_image(
                V,
                cmap,
                img.shape,
                "result/kmeans_{0}_clusters.png".format(cluster_count),
            )
