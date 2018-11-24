# Add python code in this file
from pandas import read_csv

def read_cities(cities_csv= 'cities.csv'):
    cities_df = read_csv(cities_csv)
    return cities_df

def read_points(points_csv = 'points.csv'):
    points_df = read_csv(points_csv)
    return points_df


def main():
    cities_df = read_cities() #cities dataframe
    points_df = read_points() #points dataframe
    points_df['City'] = 'None'
    for index, row in points_df.iterrows():
        cities_df_fitered = cities_df.query('TopLeft_X <= {} <= BottomRight_X and TopLeft_Y <= {} <=BottomRight_Y'.format(row['X'],row['Y']))
        if cities_df_fitered.shape[0]:
            points_df.set_value(index,'City' ,cities_df_fitered.iloc[0]['Name'])
    points_df.to_csv('output_points.csv',index =False)



if __name__ == '__main__':
    main()