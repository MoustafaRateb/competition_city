# Add python code in this file
import csv
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
    cities = []
    with open('cities.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            c = City(row)
            cities.append(c)
    return cities

def read_points():
    points= []
    with open('points.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:  
            p= Point(row)
            points.append(p)
    return points




def main():
    cities = read_cities()
    points = read_points()
    for p in points:
        p.get_city(cities)



if __name__ == '__main__':
    main()