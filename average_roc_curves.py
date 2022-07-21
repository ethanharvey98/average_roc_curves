def average_roc_curves(roc_curves_list,):
    """
    This function takes the average of different length ROC curves returned from 
    sklearn.metrics.roc_curve (see scikit-learn.org). The function expects a list 
    of fpr, tpr, and thresholds. The function subsamples from these lists and 
    returns an average_fpr, average_tpr, and average_thresholds.

    Parameters
    ----------
    roc_curves_list : list
        A list of fpr, tpr, and thresholds

    Returns
    -------
    average_fpr : list
        A list of averaged false positive rates
    average_tpr : list
        A list of averaged true positive rates
    average_thresholds : list
        A list of averaged thresholds
    """
    kfolds = len(roc_curves_list)
    min_length = np.min(list(len(roc_curves_list[k][2]) for k in range(kfolds)))
    shortened_roc_curves_list = list()
    for k in range(kfolds):
        fpr, tpr, thresholds = roc_curves_list[k]
        indicies = list(i for i in range(len(thresholds)))
        selected_indicies = np.sort(np.random.choice(indicies, min_length, replace=False))
        shortened_roc_curves_list.append([fpr[selected_indicies], tpr[selected_indicies], thresholds[selected_indicies]])
    average_fpr, average_tpr, average_thresholds = np.mean(shortened_roc_curves_list, axis=0)
    return average_fpr, average_tpr, average_thresholds
