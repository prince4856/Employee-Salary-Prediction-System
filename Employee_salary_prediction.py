## ------------------------------------
# Employee Salary Prediction System
# Developed by: Prince Kumar
# IIT Patna BS
# Day-1
# ------------------------------------



import pandas as pd
df=pd.read_csv("salary_dataset.csv")
# print(df)   # show data
# print(df.head())    # head show 1st 5 row
# print(df.tail())    # it show last 5 row
# print(df.shape)
# print(df.columns)
# print(df.info())

# Day-04
# print(df.describe())  # provide statistical summary for numerical column.
# print(df.isnull())     # Check whether value is missing or not.
# print(df.isnull().sum())  # using sum to count total no of missing value.


# day-05
# print(df["Salary"])                   # single column selection.
# print(df[["Salary","Experience"]])     # Multiple column selection

# print(df["Salary"].mean())            # Calculate Average mean of salary 
# print(df["Salary"].max())                # Highest salary
# print(df["Salary"].min())                   # Lowest salary



# Day-06
# Filter rows based on condition.

# print(df[df["Salary"]>500000])   # filter rows whose salary >500000
# print(df[df["Salary"]<500000])      # Filter rows whose salary<500000
# print(df[df["Salary"]==600000])       # Filter rows whose salary == 600000
# print(df[df["Experience"]>5])          # filter row whose Experience >5
# print(df[df["City"]=="Delhi"])


# day-07
# print(df.sort_values(by="Salary"))  # sort value by salary
# print(df.sort_values(by="Salary",ascending=False))     # sort value by salary in Descending order.

# print Top 5 highest salary.
# new_df=df.sort_values(by="Salary",ascending=False)
# print(new_df.head())    # Top 5 Highest salary
# print(new_df.tail())   # Lowest 5 salary

# Sort by Experience.
# print(df.sort_values(by="Experience"))


# Day-08
#1. Average salary by city
# df=df.groupby("City")["Salary"].mean()
# print(df)

#2.-Average salary by education.
# df=df.groupby("Education")["Salary"].mean()
# print(df)

#3-Count Employee by city.
# city_count=df.groupby("City").size()
# print(city_count)

# Count Employee by education
# count_education=df.groupby("Education").size()
# print(count_education)





# Day-09

# print(df.columns)
# print(df.describe)

# Calculate relationship b/w 2 numerical var
# print(df[["Experience","Salary"]].corr())


# Day-10  (work-EDA(Graph presentation))

# import matplotlib.pyplot as plt

# Experience=[1,2,3,4,5,6,7,8,9,10]
# Salary=[300000,400000,550000,600000,800000,1200000,700000,1000000,1500000,1800000]

# plt.plot(Experience,Salary)
# plt.title("Employee Salary vs Experience")
# plt.xlabel("Experience")
# plt.ylabel("Salary")
# plt.show()


# Day-11
# Create a bar chart.

# import matplotlib.pyplot as plt

# City=["Patna","Delhi","Mumbai","Pune","Bangalore","Hyderabad","Kolkata","Chennai","Delhi","Bangalore"]
# Salary=[300000,400000,550000,600000,800000,1200000,700000,1000000,1500000,1800000]
# df.groupby("City")  # group similar city
# result=df.groupby("City")["Salary"].mean()  # calculating mean according to mean
# print(result)
# plt.bar(result.index,result.values) # plotting bar graph
# plt.title("Average Salary vs City")
# plt.xlabel("City")
# plt.ylabel("Salary")
# plt.show()  # Display graph



# Day-12
# plotting Histogram

# import matplotlib.pyplot as plt

# Salary=[300000,400000,550000,600000,800000,1200000,700000,1000000,1500000,1800000]

# plt.hist(Salary)
# plt.title("Salary distribution")
# plt.xlabel("Salary")
# plt.ylabel("No of employee")
# plt.show()



# # Day-13---------Plotting scatter plot (it show relationship b/w two variable).

# import matplotlib.pyplot as plt

# Experience=[1,2,3,4,5,6,7,8,9,10]
# Salary=[300000,400000,550000,600000,800000,1200000,700000,1000000,1500000,1800000]

# plt.xlabel("Experience")
# plt.ylabel("Salary")
# plt.title("Experience vs Salary")
# plt.scatter(Experience,Salary, marker="*")
# plt.show()


# Day-14-------------- Topic (pie chart- pie chart represent data as a slice of circle.)

# import matplotlib.pyplot as plt

# # Count employees in each city
# df1 = df.groupby("City").size()

# # Create Pie Chart
# plt.pie(
#     df1.values,
#     labels=df1.index,
#     autopct="%1.1f%%"
# )

# plt.title("Employee Distribution by City")

# plt.show()




# Day-15     Topic-Box plot

# import matplotlib.pyplot as plt        # import matplotlib for creating graph

# Salary=[300000,400000,550000,600000,800000,1200000,700000,1000000,1500000,1800000] # Store salary value
# plt.boxplot(Salary)   # Create boxplot using salary data
# plt.title("Salary boxplot")
# plt.ylabel("salary")
# plt.show()



# Day-16          Topic:- Seaborn Heatmap (Correlation Heatmap)
# import matplotlib.pyplot as plt     # Importing matplotlib for plotting graph
# import seaborn as sns   # import Seaborn for Advance Statistical Visualisation

# Matrix=df[["Experience","Salary"]].corr()   # Select Experience and Salary Column to calculate corr matrix
# plt.title("Correlation Heatmap")   # Giving the title name of graph
# sns.heatmap(Matrix)   # Create a heatmap
# plt.show()




# Day-17
# Data preprocessing --> Handling Missing value.

# print(df.isnull())  # Checking missing value using pandas

# print(df.isnull().sum())   # Count missing value.

# print(df.isnull().sum().idxmax())  # Identifying which column has highest missing value.

# print(df.isnull().sum().sum())   # Total missing value

# # Numerical colmn --it can only fill with using mean and median
# df["Salary"]=df["Salary"].fillna(df["Salary"].mean())
# df["Experience"]=df["Experience"].fillna(df["Experience"].mean())

# # Category column--- use mode
# df["City"] = df["City"].fillna(df["City"].mode()[0])
# df["Education"] = df["Education"].fillna(df["Education"].mode()[0]) 

# # Missing value after filling 
# print(df.isnull().sum())

# # Save the clean dataset
# df.to_csv("Salary_dataset_clean.csv",index=False)



##------------------(Day-18, Topic -Handling Duplicate data(Data cleaning part-2))-----------------------

# # Check Duplicate row
# print(df.duplicated())

# # Count Duplicate rows
# print(df.duplicated().sum())

# # Display only Duplicate rows.
# print(df[df.duplicated()])


# # Dataset size before removing duplicate
# print(df.shape)   # Before removing duplicate

# # Remove  Duplicate rows
# df=df.drop_duplicates()
# print(df)

# #  Dataset size after removing duplicate.
# print(df.shape)  # After removing Duplicate

# # Save the clean dataset file.
# df.to_csv("Salary_dataset_clean.csv",index=False)



# ------------------(Day-19, Topic name :- Label Handling )------------------------

# Identify all text column.

# from sklearn.preprocessing import LabelEncoder

# # create a label encoder object
# le=LabelEncoder()

# # Encode the city column
# df["City"]=le.fit_transform(df["City"])

# # Encode education column
# df["Education"]=le.fit_transform(df["Education"])

# # Display the encoded dataset
# print(df.head())

# # Save encoded dataset
# # df.to_csv("Salary_dataset_encoded.csv", index=False)


#------------------------------------(Day-20 ,One-hot encoding)-------------------------------------

# Identify which column in your dataset is better suited for One-Hot Encoding.
# encoded_df=pd.get_dummies(df, columns=["City","Education"])

# # Display encoded dataset
# print(encoded_df.head())

# # Check new columns
# print(encoded_df.columns)

# # Dataset Shape
# print(encoded_df.shape)

# # Save Dataset
# encoded_df.to_csv("Salary_dataset_encoded.csv", index=False)


#========================(Day-21, Topic-Feature Scaling (Machine learning Data preprocessing))=====

# Identify the numerical column in the dataset.
# print(df.select_dtypes("number").columns) 

# from sklearn.preprocessing import StandardScaler   # import standardscaler from scikit-learn
# scaler=StandardScaler()   # Create an scaler obj
# df["scaled_Salary"]=scaler.fit_transform(df[["Salary"]])  # Apply  standard_scaler to numerical column
# print(df)



#============================(Day-22, Topic = Normalization using MinMaxScaler)====================
# from sklearn.preprocessing import MinMaxScaler

# # Create a  MinMaxScaler object 
# model=MinMaxScaler()

# df["Normalized_salary"]= model.fit_transform(df[["Salary"]])  # Salary normalization logic

# print("Normalized_salary=",df)

#=========================(Day-23, Topic Train test split)===============================

# from sklearn.model_selection import train_test_split

# # create data
# x=df[["Experience"]]   # input feature
# y=df["Salary"]         # target variable

# x_train ,x_test ,y_train ,y_test = train_test_split(x,y ,test_size=0.2,random_state=42)  # Train-test split


# print(x_train.shape)
# print(x_test.shape)
# print(y_train.shape)
# print(y_test.shape)

#==========================(Day-24 ,Linear Regression, Model Building )===========================

# from sklearn.linear_model  import LinearRegression

# # create obj for model
# model = LinearRegression() 

# # Train the model on training data
# model.fit(x_train,y_train)

# # Prediction
# y_pred = model.predict(x_test)

# print("Actual Salary=",y_test)
# print("Predicted Salary=",y_pred)



# ===============================(Day-25 ,Model Evaluation)=================================

# from sklearn.metrics import (mean_absolute_error,mean_squared_error,r2_score)
# import numpy as np

# mae=mean_absolute_error(y_test,y_pred)
# mse=mean_squared_error(y_test,y_pred)
# rmse=np.sqrt(mse)
# r_score=r2_score(y_test,y_pred)

# print("Mean absolute error=",mae)
# print("mean squared error=",mse)
# print("root mean square error=",rmse)
# print("r2 score=",r_score)



#================================(Day-26,Topic name-Actual vs Predicted Salary + Regression Line)===

# import matplotlib.pyplot as plt

# #  create data
# x=df[["Experience"]]   # input feature
# y=df["Salary"]         # target variable



# plt.scatter(y_test,y_pred ,label="Predicted value")
# plt.plot(x,model.predict(x),label="Regression line")
# plt.xlabel("Actual value")
# plt.ylabel("Predicted value")
# plt.title("Actual vs Predicted graph")
# plt.legend()    # show label on graph
# plt.show()

# # model parameter
# print("slope=",model.coef_)
# print("intercept=",model.intercept_)



#=========================(Day-27,Topic name-Residual ,predictions error and residual plot)========

# residual=y_test-y_pred

# print("Residual=",residual)

# import matplotlib.pyplot as plt

# plt.scatter(y_pred,residual, label="residual")

# # Zero reference line
# plt.axhline(0 ,label="Zero error")   # Draw zero horizontal line(y=o, means Actual=predicted)

# # label
# plt.xlabel("predicted")
# plt.ylabel("residual")

# # Title
# plt.title("predicted salary vs residual graph")
# plt.legend()
# plt.show()


#=============================Day-28 , Topic --> model improvement (Polynomial Regression))=======

# from sklearn.preprocessing import PolynomialFeatures
# from sklearn.linear_model import LinearRegression
# from sklearn.metrics import (mean_absolute_error,mean_squared_error,root_mean_squared_error,r2_score)

# x=df[["Experience"]]
# y=df["Salary"]

# poly=PolynomialFeatures(degree=2)

# # Transfer training data 
# x_train_poly=poly.fit_transform(x_train)


# # create a linear regression model
# model=LinearRegression()


# # train the model
# model.fit(x_train_poly,y_train)

# # Transform test data
# x_test_poly=poly.transform(x_test)


# y_pred = model.predict(x_test_poly)

# mae= mean_absolute_error(y_test,y_pred)
# mse=mean_squared_error(y_test,y_pred)
# rmse=root_mean_squared_error(y_test,y_pred)
# r=r2_score(y_test,y_pred)

# print("prediction=",y_pred)
# print("mean absolute error=",mae)
# print("mean squared error=",mse)
# print("Root mean squared error=",rmse)
# print("r2 score=",r)


#===============================(Day-29, Linear Regression vs Polynomial Regression)===============

# Linear Regression Metrics
# print("======= Linear Regression=======")

# from sklearn.preprocessing import PolynomialFeatures
# from sklearn.linear_model import LinearRegression
# from sklearn.metrics import (mean_absolute_error,mean_squared_error,r2_score)

# import numpy as np

# # Linear Regression
# Linear_model=LinearRegression()

# # train the model
# Linear_model.fit(x_train,y_train)

# # prediction
# y_pred=Linear_model.predict(x_test)

# # metrics
# mae=mean_absolute_error(y_test,y_pred)
# mse=mean_squared_error(y_test,y_pred)
# rmse=np.sqrt(mse)
# r_score=r2_score(y_test,y_pred)

# print("prediction=",y_pred)
# print("Mean absolute error=",mae)
# print("mean squared error=",mse)
# print("root mean square error=",rmse)
# print("r2 score=",r_score)


# # Polynomial Regression
# print("\n======= polynomial Regression======")


# poly = PolynomialFeatures(degree=2)

# x_train_poly=poly.fit_transform(x_train)  # Transform Training data
# x_test_poly = poly.transform(x_test)      # Training testing data


# # create model
# poly_model = LinearRegression()

# # model Training
# poly_model.fit(x_train_poly,y_train)

# # prediction
# y_pred = poly_model.predict(x_test_poly)


# # Metrics
# mae= mean_absolute_error(y_test,y_pred)
# mse=mean_squared_error(y_test,y_pred)
# rmse=np.sqrt(mse)
# r=r2_score(y_test,y_pred)

# print("prediction=",y_pred)
# print("mean absolute error=",mae)
# print("mean squared error=",mse)
# print("Root mean squared error=",rmse)
# print("r2 score=",r)


#==================================(Day-30, Topic name :-> Feature selection and Multiple linear regression)==
# Checking available columns 
print(df.columns)

# Check 1st few rows
print(df.head())

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import (mean_absolute_error,mean_squared_error,r2_score)

# I/p feature and targer variable
x=df[["Experience","Age"]]
y=df["Salary"]


# train test split
x_train ,x_test ,y_train,y_test =train_test_split(x,y,test_size=0.2 ,random_state=42)

# create model
model = LinearRegression()

# Train the model
model.fit(x_train,y_train)

# prediction on test data
y_pred = model.predict(x_test)

# model Evaluation
mae=mean_absolute_error(y_test,y_pred)
mse=mean_squared_error(y_test,y_pred)
rmse=np.sqrt(mse)
r2=r2_score(y_test,y_pred)



# print result
print("mean absolute error=",mae)
print("mean square error=",mse)
print("Root mean square error=",rmse)
print("r2 score=",r2)

print("Coefficients =", model.coef_)
print("Intercept =", model.intercept_)


#=================================(Day-31, Topic :-Model Evaluatiom for salary predictions)=========

import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import (mean_absolute_error,mean_squared_error, r2_score)


# split the datasets
x_train,x_test ,y_train,y_test = train_test_split(x,y, test_size=0.2 ,random_state=42)

# create model
model = LinearRegression()

# train the model
model.fit(x_train,y_train)

# predictions
y_pred=model.predict(x_test)

# Residual
Residuals = y_test-y_pred

mae = mean_absolute_error(y_test,y_pred)
mse=mean_squared_error(y_test,y_pred)
rmse=np.sqrt(mse)
r2 = r2_score(y_test,y_pred)


print("prediction=",y_pred)
print("Error=",Residuals)
print("mean absolute erro=",mae)
print("mean squared error=",mse)
print("Root mean square error=",rmse)
print("r2 score=",r2)


# Visualization of Residual Analysis 

# import matplotlib.pyplot as plt

# plt.scatter(y_pred,Residuals)
# plt.xlabel("Predicted salary")
# plt.ylabel("residual")
# plt.title("Predicted salary vs residual")

# ## Draw horizontal line at residual = 0
# plt.axhline(y=0)  # draws the zero-residual reference line.
# plt.show()


# # Visualization of  Actual vs predicted salary plot

# import matplotlib.pyplot as plt

# plt.scatter(y_test ,y_pred)
# plt.xlabel("Actual salary")
# plt.ylabel("predicted salary")
# plt.title("Actual vs predicted salary")
# plt.show()



#===============================( Day-32 , Model Comparision)=================================

# Today we will learn which model is better in diff regression model for employee salary predictions system.
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.metrics import (mean_absolute_error,mean_squared_error,r2_score)



# create model

models={
    "Linear Regression":LinearRegression(),
    "Decision Tree": DecisionTreeRegressor(),
    "Random Forest":RandomForestRegressor(random_state=42),
        "Gradient Boosting":GradientBoostingRegressor(random_state=42)}


# Create empty list to store model results
results = []


# Train each model
for name,model in models.items():
    model.fit(x_train,y_train)
    y_pred=model.predict(x_test)
    


    # model Evaluation
    mae=mean_absolute_error(y_test,y_pred)
    mse=mean_squared_error(y_test,y_pred)
    rmse=np.sqrt(mse)
    r2=r2_score(y_test,y_pred)

    # print the result
    results.append({
                   "model":name,
    "mean absolute error":mae,
    "Mean squared error":mse,
    "Root mean square error":rmse,
    "R2 score":r2
    })

# convert result into dataframe
result_df=pd.DataFrame(results)

# Display the model comparision
print(result_df)


#======================================(Day-33 ,Best Model Selection)===================================
# Find the best model based on mae
best_model_name = result_df.loc[result_df["mean absolute error"].idxmin(),"model"] 

# Select actual model
best_model=models[best_model_name]

# Display selected model

print("Best model=",best_model_name)
print("Selected Model object=",best_model)


# Get the performance of selected model
best_result = result_df[result_df["model"] == best_model_name]

print("\nSelected Model Performance")
print("MAE =", best_result["mean absolute error"].values[0])
print("MSE =", best_result["Mean squared error"].values[0])
print("RMSE =", best_result["Root mean square error"].values[0])
print("R2 Score =", best_result["R2 score"].values[0])


#===============================(Day-34 ,Hyperparameter tuning of selected  model)==================

from sklearn.ensemble  import RandomForestRegressor
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import (mean_squared_error , mean_absolute_error ,r2_score)

import numpy as np


# Create Random Forest model
model = RandomForestRegressor(random_state=42)


# Define hyperparameters
param_grid = {
    "n_estimators":[50, 100,200],
    "max_depth":[None ,10,20]
}

# Create GridSearchCV 
grid_search = GridSearchCV(estimator = model , param_grid=param_grid , cv=5 ,scoring = "neg_mean_absolute_error",n_jobs =1 )


# Train GridSearchCV 
grid_search.fit(x_train,y_train)


# Display best parameters
print("Best parameters=",grid_search.best_params_)


# Get the best model
best_rf =grid_search.best_estimator_


# prediction
y_pred_rf = best_rf.predict(x_test)


# Model Evaluation
mae_rf =mean_absolute_error(y_test,y_pred_rf)
mse_rf = mean_squared_error(y_test ,y_pred_rf)
rmse_rf =np.sqrt(mse_rf)
r2_rf=r2_score(y_test,y_pred_rf)


# Display performance
print("\n Tuned Random Forest performance")
print("MAE=",mae_rf)
print("MSE=",mse_rf)
print("RMSE=",rmse_rf)
print("R2 Score=",r2_rf)


#=========================================(Day-35 ,Model validation and overfitting check)============
# Today we will compare training performance and testing performance 

from sklearn.metrics import (mean_absolute_error,r2_score)

# train the selected model
best_model.fit(x_train,y_train)

# prediction on Training data
y_train_pred =best_model.predict(x_train)

# predictions on testing data
y_test_pred=best_model.predict(x_test)


# Training performance
mae_train=mean_absolute_error(y_train,y_train_pred)
r2_train= r2_score(y_train,y_train_pred)

# Testing performance
mae_test=mean_absolute_error(y_test, y_test_pred)
r2_test =r2_score(y_test,y_test_pred)


# Display result
print("Training mae=",mae_train)
print("r2 train=",r2_train)

print("Test mae=",mae_test)
print("r2 test=",r2_test)


#====================================(Day-36 , Topic-> Final model and new Employee salary predictions)=====
# Today you will learn how to use the selected linear regression model
#  to predict the salary of new Employee.

print(x.columns)

# Train the Final selected model
best_model.fit(x_train,y_train)

# Create a new Employee data
new_employee=[[5,30,]]

# predicted Salary 
predicted_salary =best_model.predict(new_employee)
print("Predicted salary=",predicted_salary[0])   # print the predicted salary


#===========================================(Day-37 , Topic:-used input based salary prediction)======

# Take input from the user
Experience=float(input("Enter experience:"))
Age=float(input("Enter age:"))

# create employee data
new_employee=[[Experience , Age]]

# predicted salary
predicted_salary=best_model.predict(new_employee) 

# Display salary
print("Predicted Salary=",round(predicted_salary[0],2))   # print the 1st predicted salary round up to 2 decimal place.


#==============================(Day-38, Topic:-prediction validation and input Handling)============

# taking user input
Experience=float(input("enter experience"))
Age=float(input("enter age"))

# input validation
if Experience<0:
    print("Invalid experience. experience cannot be negative")

elif Age<18 or Age>0:
    print("Invalid age. enter the age b/w 18 and 70.")

else:
    # create a new employee data
    new_employee=[[Experience,Age]]    

    # predict salary
    predicted_salary = best_model.predict(new_employee)

    # Display salary
    print("predicted_salary",round(predicted_salary[0],2))


#==========================(Day-39 ,Topic:-> Create a complete prediction function)===============

def predict_salary(experience,age):

    # Validate experience
    if experience<0:
        return "invalid experienxce, experience cannot be negative."

    # Validate age
    elif age<18 or age>70:
        return "invalid age,please enter age between 18 and 70"


    # create the employee data
    new_employee=[[experience,age]]

    # Predict salary
    predict_salary=best_model.predict(new_employee)

    # return predicted salary
    return round(predicted_salary[0],2)

# calling function
result = predict_salary(5,30)
print("Result=",result)


#================================(Day-40, Topic :-Save and Load the trained ML model)==========

import joblib   # import joblib library ,use to save and load Python objects such as trained machine-learning models.

# Train the Final model
best_model.fit(x_train,y_train)   # x_train → input/features ,y_train → target/output

# save the trained model
joblib.dump(best_model, "salary_model.pkl")    # joblib.dump(object, filename)
print("Saved model Successfully")

# Load the saved model
best_model=joblib.load("salary_model.pkl")
print("Model loaded successfully")

# Test prediction
new_employee=[[5,30]]

predicted_salary=best_model.predict(new_employee)
print("predicted_salary=",round(predicted_salary[0],2))   # Round the first predicted salary up to 2 decimal salary


#=============================(Day-41 ,Topic:-Separate model Training and Prediction)===============

import joblib

# train the final model
best_model.fit(x_train,y_train)

# Save the model
joblib.dump(best_model,"salary_model.pkl")
print("model train and saved successfully")

# Prediction script


# Load trained model
best_model=joblib.load("salary_model.pkl")

# Take input from user
experience=float(input("enter experience"))
age=float(input("enter age"))

# validate input
if experience<0:
    print("invalid experience,experience cannot be negative")
elif age<18 or age>70:
    print("invalid age,enter age b/w 18 and 70")

else:
    new_employee=[[experience,age]]

    # predict salary
    predicted_salary=best_model.predict(new_employee) 
    print("Predict salary=",round(predicted_salary[0],2))   


#================================(Day-42,Topic:-Create a user friendly prediction interface)================

import joblib

# Load model
best_model=joblib.load("salary_model.pkl")

# project heading
print("="*45)
print("EMPLOYEE SALARY PREDICTIONS SYSTEM")
print("="*45)

# Take input from user 
print("/n Enter Employee Details")
print("="*30)

experience=float(input("enter experience:"))
age=float(input("enter age:"))

# input validation
if experience<0:
    print("invalid experience and experience cannot be negative")
elif age>18 or age<70:
    print("invalid age or age should be b/w 18 and 70")
else:
    # create employee data
    new_employee=[[experience,age]]

    # predict salary
    predicted_salary=best_model.predict(new_employee)

    # Display salary
    print("\n" + "-" * 45)
    print("Predicted Salary = ₹", round(predicted_salary[0], 2))
    print("-" * 45)


#============================================(Day-43, Topic :-Final testing and error Handling)===

import joblib

# Load the trained model
best_model=joblib.load("salary_model.pkl")

# Project handling
print("EMPLOYEE SALARY PREDICTION SYSTEM")

try:
    # Take input from user
    experience=float(input("enter experience"))
    age=float(input("enter age"))

    # input validation
    if experience<0:
        print("invalid experience .it cannot be negative")

    elif age<18 or age>70:
        print("invalid age. enter age b/w 18 and 70")

    else:

        # create employee data
        new_employee=[[experience,age]]

        # predict salary
        predict_salary=best_model.predict(new_employee)

        # Display salary
        print("Predicted salary=",round(predict_salary[0],2))

except ValueError:
    print("invalid input,please enter numeric value ")

#=============================(DAY-44, Topic name :--> Project Documentation and final workflow)===

# Complete WorkFlow of my project (Employee salary prediction system) :-----

# Dataset
#    ↓
# Data Preprocessing
#    ↓
# Feature Selection
#    ↓
# Train-Test Split
#    ↓
# Model Training
#    ↓
# Model Comparison
#    ↓
# Model Evaluation
#    ↓
# Hyperparameter Tuning
#    ↓
# Best Model Selection
#    ↓
# Save Model
#    ↓
# Load Model
#    ↓
# User Input
#    ↓
# Input Validation
#    ↓
# Salary Prediction
#    ↓
# Display Result    

