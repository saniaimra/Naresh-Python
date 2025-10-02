def predict_sales(x):
    average_sales = sum(x)/len(x)
    print('Predicted sales for next month = ', average_sales)

predict_sales([10,20,30,40])