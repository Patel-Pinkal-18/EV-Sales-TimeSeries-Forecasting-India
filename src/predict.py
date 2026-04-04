import joblib

def load_model(path="models/ev_sales_model.pkl"):
    return joblib.load(path)

def predict(model, X):
    return model.predict(X)