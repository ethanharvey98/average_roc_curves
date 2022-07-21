# average_roc_curves
This function takes the average of different length ROC curves returned from sklearn.metrics.roc_curve (see scikit-learn.org). The function expects a list of fpr, tpr, and thresholds. The function subsamples from these lists and returns an average_fpr, average_tpr, and average_thresholds.
