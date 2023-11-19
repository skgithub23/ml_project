from classification2f import classification
#from classification3f import classification

import warnings
warnings.filterwarnings("ignore")
selected_features_list = [3,4,5,6,10,20,26]
classifier_list=['lr','dt','nb','rf','knn','ad','svm']
for classifier_type in classifier_list:
    for selected_features in selected_features_list:
        clf = classification('C:/Users/mailf/Downloads/drive-download-20231109T161859Z-001/', clf_opt=classifier_type,
                            no_of_selected_features=selected_features)
        print(f"Classifier: {classifier_type}, Selected Features: {selected_features}")
        clf.classification()
