import joblib
from xgboost import XGBRegressor
from sklearn.model_selection import TimeSeriesSplit, GridSearchCV

def train_model(X, y):
    model = XGBRegressor(random_state=42)

    param_grid = {
        'n_estimators': [100, 200],
        'max_depth': [3, 5],
        'learning_rate': [0.05, 0.1]
    }

    tscv = TimeSeriesSplit(n_splits=5)

    grid = GridSearchCV(
        model,
        param_grid,
        cv=tscv,
        scoring='neg_mean_squared_error',
        n_jobs=-1
    )

    grid.fit(X, y)

    joblib.dump(grid.best_estimator_, "models/ev_sales_model.pkl")

    return grid.best_estimator_