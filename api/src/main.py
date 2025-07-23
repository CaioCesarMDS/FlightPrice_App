from .utils.preprocessing import preprocess_base, preprocess_train
from .training.train import train_model

import pandas as pd

from sklearn.model_selection import train_test_split

def main(test_data):
    train_data = pd.read_excel('data/train_set.xlsx')

    train_df = preprocess_train(train_data)
    test_df = preprocess_base(test_data)

    X = train_df.drop('Price', axis=1)
    y = train_df['Price']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    test_df = test_df.reindex(columns=X.columns, fill_value=0)

    model = train_model( X_train, X_test, y_train, y_test)
    predictions = model.predict(test_df)

    return predictions
