# Stock_price_predictor
Stock price predictor is a data science project that takes in the different parameters of stock prices such as open value , highest and lowest volume and the volume of the stock to predict its closing price . This project compares two different approaches for prediction of the closing price . 
The two methods we use for predictions are
i) Machine Learning method 
ii) Neural Network method . 
The first step i.e of data cleaning and processing remains the same for both the methods . In the first method we are going to use the Linear Regression model from scikit-learn library . 
# Using Linear Regression 
The below graph shows the difference of the price predicted by the model and actual price from the testing dataset . The blue plot indicates the true value of the closing price and the green plot indicates the value predicted by the model 
![alt text](https://github.com/GAURAV-SOMAN-PORTFOLIO/Stock_price_predictor/blob/main/prediction_comparison.png)
Above graph is plotted with Index on the X axis and price of the stock on Y axis . 
The accuracy of the model is calculated with the r2_score metrics from the scikit-learn library . The r2score of the model comes out to be 0.989 or 98.9%

# Using Neural Network 
