import numpy as np

from sklearn.ensemble import HistGradientBoostingRegressor
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error

def train_model(X_train, X_test, y_train, y_test):

  model = HistGradientBoostingRegressor(l2_regularization=1.0, learning_rate=0.2, max_depth=30, max_iter=450, min_samples_leaf=5, random_state=42)

  model.fit(X_train, y_train)

  y_pred = model.predict(X_test)
  rmse = np.sqrt(mean_squared_error(y_test, y_pred))
  mae = mean_absolute_error(y_test, y_pred)
  r2 = r2_score(y_test, y_pred)

  print(f"RMSE: {rmse}")
  print(f"MAE: {mae}")
  print(f"R2: {r2}")

  return {
      "model_name": "HistGradientBoostingRegressor",
      "model": model,
      "rmse": rmse,
      "mae": mae,
      "r2": r2
  }

