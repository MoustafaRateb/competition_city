# Add python code in this file
import pandas as pd
class City:
    def __init__(self,city_dict):
        self.City_name = city_dict['Name'] 
        self.left_x = int(city_dict['TopLeft_X'])
        self.top_y =int(city_dict['TopLeft_Y'])
        self.right_x=int(city_dict['BottomRight_X'])
        self.bottom_y=int(city_dict['BottomRight_Y'])

class Point:
    def __init__(self,point_dict):
        self.point_id = point_dict['ID']
        self.x= int(point_dict['X'])
        self.y= int(point_dict['Y'])
        self.city = None
    def get_city(self,cities):
        for c in cities:
            if (c.left_x <= self.x <=c.right_x and c.top_y <= self.y <= c.bottom_y):
                self.city = c.City_name
                break
        
        print(self.point_id,self.city)


def read_cities():
    cities_df = pd.read_csv('cities.csv')
    return cities_df

def read_points():
    points_df = pd.read_csv('points.csv')
    return points_df




def main():
    cities_df = read_cities()
    points_df = read_points()
    points_df['City'] = None
    for index, row in points_df.iterrows():
        cities_df_fitered = cities_df.query('TopLeft_X <= {} <= BottomRight_X and TopLeft_Y <= {}<=BottomRight_Y'.format(row['X'],row['Y']))
        if cities_df_fitered.shape[0]:
            #points_df['City'][index] = 
            points_df.set_value(index,'City' ,cities_df_fitered.iloc[0]['Name'])
            print(points_df.iloc[index]['City'])
    print(points_df)



if __name__ == '__main__':
    main()