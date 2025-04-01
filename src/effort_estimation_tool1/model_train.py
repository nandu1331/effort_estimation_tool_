# train_model.py
import joblib
from sklearn.ensemble import RandomForestRegressor
from database import get_db_connection, fetch_historical_data, close_db_connection

def train_effort_model():
    """
    Train a RandomForestRegressor model using historical effort data from the database.
    """
    # Fetch historical data
    conn = get_db_connection()
    historical_data = fetch_historical_data(conn)
    close_db_connection(conn)

    if not historical_data:
        raise ValueError("No historical data available to train the model.")

    # Prepare features (X) and targets (y)
    X = []  # Features: simplistic complexity score based on effort averages
    y = []  # Targets: actual efforts

    for data in historical_data:
        ui_ux, mobile, mobile_buffer, mobile_testing, backend, backend_buffer, backend_testing, buffer, management = data
        # Simplified complexity: average of core efforts
        complexity = (ui_ux + mobile + backend + mobile_testing + backend_testing) / 5
        X.append([complexity])
        y.append([ui_ux, mobile, mobile_buffer, mobile_testing, backend, backend_buffer, backend_testing, buffer, management])

    # Train the model
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X, y)
    
    # Save the model
    joblib.dump(model, "effort_model.pkl")
    print("Trained and saved effort_model.pkl")

if __name__ == "__main__":
    train_effort_model()