import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
import joblib

df=pd.read_csv("dataset.csv")

x=df[["Years_Experience","Education_Level","Certifications_Count","Performance_Score"]]
y=df["Salary_LPA"]

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=42)

model=RandomForestRegressor(n_estimators=100,random_state=42)
model.fit(x_train,y_train)

joblib.dump(model,"salary_model.pkl")
print("Salary Model trained and saved as 'salary_model.pkl'!")

