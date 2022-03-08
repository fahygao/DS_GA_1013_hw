import numpy as np
from sklearn.datasets import fetch_olivetti_faces
import plot_tools


def compute_nearest_neighbors(train_matrix, testImage):
    
    ## fill your code here. feel free to modify the signature of the function if required. 
    return idx_of_closest_point_in_train_matrix


def main() :
    test_idx = [1,  87,  94, 78] #use this

    data = fetch_olivetti_faces()
    targets = data.target
    data = data.images.reshape((len(data.images), -1))

    train_idx = np.array(list(set(list(range(data.shape[0]))) - set(test_idx) ) )

    train_set = data[train_idx ]
    y_train = targets[train_idx] 
    test_set = data[np.array(test_idx)]
    y_test = targets[ np.array(test_idx)]


    imgs = []
    estLabels = []
    for i in range(test_set.shape[0]):
        testImage = test_set[i, :]
        nnIdx = compute_nearest_neighbors(train_set, testImage)
        imgs.extend( [testImage, train_set[nnIdx,:]] )
        estLabels.append(y_train[nnIdx])


    row_titles = ['Test','Nearest']
    col_titles = ['%d vs. %d'%(i,j) for i,j in zip(y_test, estLabels)]
    plot_tools.plot_image_grid(imgs,
                    "Image-NearestNeighbor",
                    (64,64), len(test_set),2,True,row_titles=row_titles,col_titles=col_titles)
    
    
    
##### Support code for 4e
#     test_idx = [207, 209, 396,  10,  15, 334, 101, 286, 255, 305,  37,  38,  97,
#        331, 227, 347,  45, 105, 151,  65, 265, 217,  19, 238,  56, 378,
#          3, 316, 246,  69, 179, 303, 250, 103, 337, 145, 183, 236,  71,
#        354, 395, 281,  81, 350, 301, 381,  67, 297, 205, 358] #use this test indices
#     k_values = [1, 5, 10, 15, 20, 25, 30, 35, 40, 50, 100, 200, 300, 400]  #use atleast these many k values. can add to this
    
    
#     data = fetch_olivetti_faces()
#     targets = data.target
#     data = data.images.reshape((len(data.images), -1))

#     train_idx = np.array(list(set(list(range(data.shape[0]))) - set(test_idx) ) )

#     train_set = data[train_idx ]
#     y_train = targets[train_idx] 
#     test_set = data[np.array(test_idx)]
#     y_test = targets[ np.array(test_idx)]


# Support code for 4f - adding noise to data
# noisy_train_set = train_set + np.random.randn(*train_set.shape)*(150/255)
# noisy_test_set = test_set + np.random.randn(*test_set.shape)*(150/255)
    
    
    
if __name__ == "__main__" :
    main()