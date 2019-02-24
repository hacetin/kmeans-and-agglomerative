This repo includes the codes that I used in Machine Learning course for K-Means and Agglomerative Clustering. To see results quickly, use sample2.jpg instead of sample.jpg

# K-Means Clustering (part1.py)

### Implementation

Here are the steps of the k-means algorithm that I implemented:

1. Find the mean and the standard deviations (std) of the given data (im2 in our case).
2. Generate K random points. For each random point r, choose a random initial centroid as: “r \* std + mean”
3. Find all distances between data points and centroids and label all points with the closest centroid.
4. With labeled points, find mean values for each label (cluster). Keep old centroids in a temp variable and assign these new mean values to real centroid list.
5. Calculate error as the norm of difference vector between new and old centroids. If error is zero, end the process, and return label array and centroid array. Else, go to 3rd step.

# Agglomerative Clustering (part2.py)

### Implementation

I used centroid-linked agglomerative clustering. I just kept the centroid and the item count of each cluster. Here are the steps of the agglomerative clustering algorithm that I implemented:

1. Define each data point as a different cluster, and the point itself as the centroid of the cluster. Also, assign 1 to item count, and initialize a label array showing centroid indexes in the centroid array.
2. Find the closest two centroids (minimum distance, maximum similarity).
3. Add the cluster with high index to the cluster with the low index combining centroids with average mean and summing item counts.
4. Replace all labels of the cluster with the higher index with labels of the cluster with the low index in the labels array.
5. If the length of the centroids array is equal to K, end the process, and return label array and centroid array. Else, go to 2nd step.

### Speeding Up the Algorithm

To speed up the algorithm, I didn’t give the whole data points at the beginning. I gave the points to the agglomerative clustering algorithm as the total number of clusters be 100 initially at every iteration. 100 is a number that I found experimentally. If I use 1000, it is too slow for agglomerative clustering algorithm, or if I use 30, it increases the iteration count. Also, batch size must be more than or equal 2K to avoid infinite loop inside the agglomerative algorithm. Here are the steps for speeding up part:

1. Run the agglomerative clustering algorithm with 100 data points initially. It will produce K clusters.
2. Keeping the cluster information from previous step, run the agglomerative clustering algorithm with new (100-K) data points.
3. If data points array comes to the end, finish the process. Else, go to 2nd step.

# Detailed Info

You can find the questions and the detailed report in docs folder.

| Document  | Link                         |
| --------- | ---------------------------- |
| Questions | [CS550_HW2.pdf][docq]        |
| Report    | [CS550_HW2_report.pdf][docr] |

[docq]: https://github.com/hacetin/clustering/docs/CS550_HW2.pdf
[docr]: https://github.com/hacetin/clustering/docs/CS550_HW2_report.pdf
