from sklearn.linear_model import LogisticRegression
import argparse
import os
import numpy as np
from sklearn.metrics import mean_squared_error
import joblib
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
import pandas as pd
from azureml.core.run import Run
from azureml.data.dataset_factory import TabularDatasetFactory

from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, roc_curve, auc
from sklearn.ensemble import RandomForestClassifier

from azureml.core import Workspace, Dataset

import joblib


def clean_data(data):
    # Dict for cleaning data
    x_df = data.drop(columns=['code'])
    x_df = pd.get_dummies(x_df, columns = ['site', 'province'])
    y_df = data['code']
    return x_df, y_df

def main():
    # Add arguments to script
    parser = argparse.ArgumentParser()

    parser.add_argument('--n', type=int, default=3)
    parser.add_argument('--l', type=int, default=5)
    parser.add_argument('--d', type=int, default=4)

    args = parser.parse_args()

    run = Run.get_context()

    run.log("Estimators:", np.int(args.n))
    run.log("Leaves:", np.int(args.l))
    run.log("Max Depth:", np.int(args.d))

    # TODO: Create TabularDataset using TabularDatasetFactory
    # Data is located at:
    datasource = "https://raw.githubusercontent.com/xrubio/ecologyStamps/master/data/stamps.csv"
    ds = pd.read_csv(datasource, sep=';')
    ds = ds.copy()[ds['type']=="Dressel 20"]
    ds.drop(labels=['X', 'Y','id','type'], axis=1, inplace=True)  #no longer need type, since all vessels same
    ds.rename(columns={"name":"province"}, inplace=True)
    
    x, y = clean_data(ds)

    # TODO: Split data into train and test sets.

    ### YOUR CODE HERE ###

    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state = 42)

    rfc = RandomForestClassifier(
        n_estimators = args.n,
        max_depth = args.d,
        min_samples_leaf = args.l,
        random_state=42,
        warm_start=True

    )
    rfc.fit(x_train, y_train)
    accuracy = rfc.score(x_test, y_test)
    run.log("Accuracy", np.float(accuracy))

    #save the model
    joblib.dump(rfc, './outputs/model.joblib')


if __name__ == '__main__':
    main()
