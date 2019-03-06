import mod1.read_data as rd
import mod2.exploratory_data_analysis as ea


resources_folder = "/tmp/resources/" 

df = rd.get_cars_df()
clean_df = rd.get_clean_cars_df(df)
print(rd.view_data_info(clean_df))
#Regresion lineal simple
#prediction1 = ea.linear_regression(clean_df[['highway-mpg']], clean_df['price'])
#ea.dist_plot(clean_df['price'], prediction1, resources_folder + "single_recursion_dist.png")

#regresion lineal multiple
#'curb-weight', 'engine-size', 'horsepower'
#prediction2 = ea.linear_regression(clean_df[['engine-size', 'curb-weight', 'highway-mpg']], clean_df['price'])
#ea.dist_plot(clean_df['price'], prediction2, resources_folder + "multiple_recursion_dist.png")

#regresion polinomial simple
#ea.polynomial_1d_regression(clean_df['highway-mpg'], clean_df['price'], 3)

#regresion polinomial multiple de 3er grado
prediction = ea.pipeline_polynomial_nd_regression(clean_df[['engine-size', 'curb-weight', 'highway-mpg', 'wheel-base']], clean_df['price'], 3)
ea.dist_plot(clean_df['price'], prediction, resources_folder + "multiple_3_polinomial_dist.png")

print(ea.msqe(clean_df['price'], prediction))
print(ea.r_square(clean_df['price'], prediction))