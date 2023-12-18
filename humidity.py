import pickle
import pandas as pd
from prophet import Prophet
from prophet.plot import plot_plotly
data = pd.read_csv("Data/data.csv")

data["date"] = pd.to_datetime(data["date"], format='%Y-%m-%d')
data['year'] = data['date'].dt.year
data["month"] = data["date"].dt.month
forecast_data = data.rename(columns={"date": "ds", "humidity": "y"})

model = Prophet()
model.fit(forecast_data)

with open('Model/prophet_model_humidity.pkl', 'wb') as f:
    pickle.dump(model, f)
    
future = model.make_future_dataframe(periods=365)
predictions = model.predict(future)

plot_plotly(model, predictions).show()
