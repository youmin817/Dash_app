import pandas as pd
from sklearn.ensemble import RandomForestRegressor

# Use github to get data set
act = pd.read_csv("https://raw.githubusercontent.com/youmin817/Data_Analysis/master/dashboard_app/ACT_Test_Score.csv")


df_sd = act.loc[:,["Name","English", "Math", "Reading", "Science", "Composite"]]

# data construction
names = df_sd.Name

df = df_sd.drop("Name", axis=1).T
df.columns = names

# subjects
columns = df_sd.columns[1:5]

# prediction set tup train model
x_train = act[["English","Math","Reading"]]
y_train = act["Science"]

# Random Forest Regression for prediction
rfModel = RandomForestRegressor(n_estimators=100)
rfModel.fit(x_train, y_train)

