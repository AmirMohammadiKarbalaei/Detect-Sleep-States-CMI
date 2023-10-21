from sklearn.metrics import  confusion_matrix, classification_report, roc_curve, roc_auc_score
import matplotlib.pyplot as plt
import numpy as np



def evaluate_model(set_name, y_set, predictions, probabilities):
    # Plot the confusion matrix
    cm = confusion_matrix(y_set, predictions)
    plt.figure(figsize=(6, 4))
    plt.imshow(cm, interpolation='nearest', cmap=plt.cm.Blues)
    plt.title(f"Confusion Matrix for {set_name} set")
    plt.colorbar()
    classes = [0, 1]
    tick_marks = np.arange(len(classes))
    plt.xticks(tick_marks, classes)
    plt.yticks(tick_marks, classes)
    plt.xlabel("Predicted")
    plt.ylabel("True")
    for i in range(len(classes)):
        for j in range(len(classes)):
            plt.text(j, i, format(cm[i, j], 'd'), horizontalalignment="center", color="white" if cm[i, j] > cm.max() / 2 else "black")
    plt.show()

    # Print the classification report
    print(f"Classification Report for {set_name} set:\n", classification_report(y_set, predictions))

    # Plot the ROC curve
    fpr, tpr, thresholds = roc_curve(y_set, probabilities)
    roc_auc = roc_auc_score(y_set, probabilities)
    plt.figure(figsize=(8, 6))
    plt.plot(fpr, tpr, label=f'{set_name} set ROC curve (AUC = {roc_auc:.2f})')
    plt.plot([0, 1], [0, 1], 'k--')
    plt.xlim([0.0, 1.0])
    plt.ylim([0.0, 1.05])
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.title(f'Receiver Operating Characteristic (ROC) Curve for {set_name} set')
    plt.legend(loc="lower right")
    plt.show()