# average_roc_curves

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
