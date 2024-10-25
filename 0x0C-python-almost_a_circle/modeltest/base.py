import json
import os
import csv
import turtle
import tkinter as TK

class Base:
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
    
    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries is None:
            return "[]"
        else:
            return json.dumps(list_dictionaries)
    
    @classmethod
    def save_to_file(cls, list_objs):
        filename = f"{cls.__name__}.json"

        with open(filename, 'w') as f:
            list_dict = [obj.to_dictionary() for obj in list_objs]
            json_str = Base.to_json_string(list_dict)
            f.write(json_str)
    
    @staticmethod
    def from_json_string(json_string):
        if json_string is None or json_string == '':
            return []
        else:
            return json.loads(json_string)
    
    @classmethod
    def create(cls, **dictionary):
        if cls.__name__ == 'Rectangle':
            new_instance = cls(1, 1)
        elif cls.__name__ == "Square":
            new_instance = cls(1)
            
        new_instance.update(**dictionary)
        return new_instance
    
    @classmethod
    def load_from_file(cls):
        filename = cls.__name__ + ".json"
        if not os.path.exists(filename):
            return []
        with open(filename, 'r') as f:
            json_string = f.read()
        list_dict = Base.from_json_string(json_string)
        return [cls.create(**d) for d in list_dict]
    
    @classmethod
    def save_to_file_csv(cls, list_objs):
        filename = cls.__name__ + ".csv"

        input_list = [obj.to_dictionary() for obj in list_objs]

        with open(filename, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerows([list(d.values()) for d in input_list])

    @classmethod
    def load_from_file_csv(cls):
        filename = cls.__name__ + '.csv'
        obj_list = []
        try:
            with open(filename, 'r') as f:
                reader = csv.reader(f)
                for row in reader:
                    if cls.__name__ == "Rectangle":
                        obj_dict = {
                            "id": int(row[0]),
                            "width": int(row[1]),
                            "height": int(row[2]),
                            "x": int(row[3]),
                            "y": int(row[4])
                        }
                    elif cls.__name__ == "Square":
                        obj_dict = {
                            "id": int(row[0]),
                            "size": int(row[1]),
                            "x": int(row[2]),
                            "y": int(row[3])
                        }

                    # Use `create` to instantiate the object with the dictionary values
                    obj = cls.create(**obj_dict)
                    obj_list.append(obj)
        except FileNotFoundError as e:
            pass

        return obj_list
    
    @staticmethod
    def draw(list_rectangles, list_squares):
        """Draws rectangles and squares using the turtle graphics module."""

        # Set up the turtle screen
        screen = turtle.Screen()
        screen.title("Rectangle and Square Drawing")
        screen.bgcolor("white")
        
        # Function to draw a shape based on the dimensions and position
        def draw_shape(shape, color):
            t = turtle.Turtle()
            t.penup()
            t.goto(shape.x, shape.y)
            t.pendown()
            t.color(color)
            t.begin_fill()

            for _ in range(2):
                t.forward(shape.width if hasattr(shape, "width") else shape.size)
                t.left(90)
                t.forward(shape.height if hasattr(shape, "height") else shape.size)
                t.left(90)

            t.end_fill()
            t.hideturtle()

        # Draw all rectangles
        colors = ["red", "blue", "green", "purple"]
        for i, rect in enumerate(list_rectangles):
            draw_shape(rect, colors[i % len(colors)])

        # Draw all squares
        for i, square in enumerate(list_squares):
            draw_shape(square, colors[i % len(colors)])

        # Complete drawing
        turtle.done()


