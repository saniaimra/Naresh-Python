def ROI(init_price,fin_price):
    roi = []
    for i in range(len(init_price)):
        a = ((fin_price[i]-init_price[i])/init_price[i])*100
        roi.append(a)

    total_roi = ((sum(fin_price) - sum(init_price))/sum(init_price))*100
    print('Initial_prices = ',init_price)
    print('Final_prices = ',fin_price)
    print(roi)
    print(total_roi)
ROI([100, 200, 300],[120, 180, 330])