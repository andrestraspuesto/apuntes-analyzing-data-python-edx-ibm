
from sklearn.linear_model import LinearRegression

def simple_linear_regression(x, y):
    lm = LinearRegression()
    exp = lm.fit(x, y)
    prediction = lm.predict(x)
    #y = y0 + pte*x
    y0 = lm.intercept_
    pte = lm.coef_
    
    