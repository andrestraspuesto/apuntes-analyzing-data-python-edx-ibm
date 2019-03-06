
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score
import seaborn as sns
import numpy as np

def linear_regression(x, y):
    lm = LinearRegression()
    exp = lm.fit(x, y)
    prediction = lm.predict(x)
    #y = y0 + sum[ptei*xi]
    y0 = lm.intercept_
    pte = lm.coef_
    return prediction

def polynomial_1d_regression(x, y, n):
    f = np.polyfit(x, y, n)
    p = np.poly1d(f)
    print(p)

def pipeline_polynomial_nd_regression(x, y, n):
    steps =[
        ('scale', StandardScaler()), 
        ('polynomial', PolynomialFeatures(degree = n)),
        ('model', LinearRegression())
        ]
    pipe = Pipeline(steps)
    pipe.fit(x, y)
    prediction = pipe.predict(x)
    return prediction

def msqe(real_values, predicted_values):
    return mean_squared_error(real_values, predicted_values)
def r_square(real_values, predicted_values):
    return r2_score(real_values, predicted_values)
    
def dist_plot(real_data, calculated, plot_path):
    ax1 = sns.distplot(real_data, hist = False, color = 'r', label = "Actual value")
    ax = sns.distplot(calculated, hist = False, color = 'b', label = 'Fitted values', ax = ax1)
    plt = ax.get_figure()
    plt.savefig(plot_path)
    