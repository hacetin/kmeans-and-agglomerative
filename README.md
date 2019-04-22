This repo includes the codes that I used in Machine Learning course for K-Means and Agglomerative Clustering. To see results quickly, use **sample2.jpg** instead of **sample.jpg**.

# Results

| K   | K-Means Clustering                | Agglomerative Clustering       |
| --- | --------------------------------- | ------------------------------ |
| 2   | ![kmeans_2_clusters.png][k2res]   | ![agg_2_clusters.png][a2res]   |
| 4   | ![kmeans_4_clusters.png][k4res]   | ![agg_4_clusters.png][a4res]   |
| 8   | ![kmeans_8_clusters.png][k8res]   | ![agg_8_clusters.png][a8res]   |
| 16  | ![kmeans_16_clusters.png][k16res] | ![agg_16_clusters.png][a16res] |

Original Image(sample.jpg):
![sample.jpg][samplejpg]

# K-Means Clustering (part1.py)

### Implementation

Here are the steps of the k-means algorithm that I implemented:

1. Find the mean and the standard deviation (std) of the given data (im2 in our case).
2. Generate K random points. For each random point r, choose a random initial centroid as: “r \* std + mean”
3. Find all distances between data points and centroids and label all points with the closest centroid.
4. With labeled points, find mean values for each label (cluster). Keep old centroids in a temp variable and assign these new mean values to the real centroid list.
5. Calculate error as the norm of difference vector between new and old centroids. If error is zero, end the process, and return label array and centroid array. Else, go to 3rd step.

# Agglomerative Clustering (part2.py)

### Implementation

This is a centroid-linked agglomerative clustering. It just stores the centroid data point and the number of items for each cluster. Here are the steps of the agglomerative clustering algorithm:

1. Define each data point as a different cluster, and the point itself as the centroid of the cluster. Also, assign 1 to item count, and initialize a label array showing centroid indexes in the centroid array.
2. Find the closest two centroids (minimum distance, maximum similarity).
3. Add the higher indexed cluster to the lower indexed cluster by combining centroids with average mean and summing item counts.
4. Replace all labels of the higher indexed cluster with labels of the lower indexed cluster in the labels array.
5. If the length of the centroids array is equal to K, end the process, and return label array and centroid array. Else, go to 2nd step.

### Speeding Up the Algorithm

To speed up the algorithm, it doesn't use all data points at the beginning. It starts with a number of clusters initially at every iteration, and ran the agglomerative algorithm until some point. I use 100 for this project. It is like mini-batch size. Large batch size slows down agglomerative clustering algorithm, small btach size increases the number of iterations. Here are the steps for speeding up part:

1. Run the agglomerative clustering algorithm with 100 data points initially until it produces K clusters.
2. Keeping the cluster information from previous step, run the agglomerative clustering algorithm with new (100-K) data points and existing K points.
3. If data points array comes to the end, finish the process. Else, go to 2nd step.

# Detailed Info

You can find the questions and the detailed report in docs folder.

| Document  | Link                         |
| --------- | ---------------------------- |
| Questions | [CS550_HW2.pdf][docq]        |
| Report    | [CS550_HW2_report.pdf][docr] |

[samplejpg]: https://github.com/hacetin/cluster/blob/master/sample/sample.jpg?raw=true
[k2res]: https://github.com/hacetin/cluster/blob/master/result/kmeans_2_clusters.png?raw=true
[k4res]: https://github.com/hacetin/cluster/blob/master/result/kmeans_4_clusters.png?raw=true
[k8res]: https://github.com/hacetin/cluster/blob/master/result/kmeans_8_clusters.png?raw=true
[k16res]: https://github.com/hacetin/cluster/blob/master/result/kmeans_16_clusters.png?raw=true
[a2res]: https://github.com/hacetin/cluster/blob/master/result/agg_2_clusters.png?raw=true
[a4res]: https://github.com/hacetin/cluster/blob/master/result/agg_4_clusters.png?raw=true
[a8res]: https://github.com/hacetin/cluster/blob/master/result/agg_8_clusters.png?raw=true
[a16res]: https://github.com/hacetin/cluster/blob/master/result/agg_16_clusters.png?raw=true
[docq]: https://github.com/hacetin/cluster/blob/master/docs/CS550_HW2.pdf
[docr]: https://github.com/hacetin/cluster/blob/master/docs/CS550_HW2_report.pdf
