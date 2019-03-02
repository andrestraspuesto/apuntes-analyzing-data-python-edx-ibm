import mod1.read_data as rd
import mod2.exploratory_data_analysis as ea

df = rd.get_cars_df()
clean_df = rd.get_clean_cars_df(df)

print(clean_df)