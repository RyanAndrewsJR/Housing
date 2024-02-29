import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import LabelEncoder

from sklearn.model_selection import train_test_split

from sklearn.tree import DecisionTreeClassifier
from sklearn.naive_bayes import MultinomialNB

from sklearn.metrics import confusion_matrix, classification_report
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, make_scorer
from sklearn.metrics import roc_curve

heart_data = pd.read_csv("/Users/ryanquinnandrews/Desktop/heart.csv")
print(heart_data.dtypes)

#label_encoder = LabelEncoder()
#heart_data['HeartDiseaseorAttack'] = label_encoder.fit_transform(heart_data['HeartDiseaseorAttack'])
#heart_data['Smoker'] = label_encoder.fit_transform(heart_data['Smoker'])

X = heart_data[['HeartDiseaseorAttack', 'BMI', 'Age', 'MentHlth',
               'Smoker', 'Education', 'Income']]
print(X.head)

y = heart_data['HeartDiseaseorAttack']


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4)
tree = DecisionTreeClassifier()
tree.fit(X_train, y_train)

y_pred = tree.predict(X_test)
print(y_pred)

y_pred_prob = tree.predict_proba(X_test)
print(y_pred_prob)

confmatrix = pd.DataFrame(confusion_matrix(y_test, y_pred),
                          index=['True[0]', 'True[1]'],
                          columns=['predict[0]', 'predict[1]'])
print(confmatrix)

print('Classification')
print(classification_report(y_test,y_pred))

print('accuracy: %.3f' % accuracy_score(y_test, y_pred))
print('precision: %.3f' % precision_score(y_true=y_test, y_pred=y_pred))
print('recall: %.3f' % recall_score(y_true=y_test, y_pred=y_pred))
print('F1: %.3f' % f1_score(y_true=y_test, y_pred=y_pred))