import pickle
import pandas as pd
from prophet import Prophet
from prophet.plot import plot_plotly

data = pd.read_csv("Data/data.csv")

data["date"] = pd.to_datetime(data["date"], format='%Y-%m-%d')
data['year'] = data['date'].dt.year
data["month"] = data["date"].dt.month
forecast_data = data.rename(columns={"date": "ds", "meanpressure": "y"})

model = Prophet()
model.fit(forecast_data)

future = model.make_future_dataframe(periods=365)
predictions = model.predict(future)

with open('Model/prophet_model_meanpressure.pkl', 'wb') as f:
    pickle.dump(model, f)

plot_plotly(model, predictions).show()

