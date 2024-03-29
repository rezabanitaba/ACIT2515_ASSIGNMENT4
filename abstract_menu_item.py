from sqlalchemy import Column, String, Integer, Float, DateTime
from base import Base

import datetime

class AbstractMenuItem(Base):
    """ creates menu item """ 

    BOOLEAN_TRUE = 1

    __tablename__ = "menu"

    id = Column(Integer, primary_key=True)
    menu_item_name = Column(String(100))
    menu_item_no = Column(Integer)
    date_added = Column(DateTime)
    price = Column(Float)
    calories = Column(Integer)
    type = Column(String(6))

    def __init__(self, menu_item_name, menu_item_no, date_added, price, calories, type):

        self.menu_item_name = menu_item_name
        self.menu_item_no = menu_item_no
        self.date_added = date_added
        self.price = price
        self.calories = calories
        self.type = type


    
    def to_dict(self):
        raise NotImplementedError("This needs to be implemented in the child classes")


    def get_id(self):
        """ returns menu item id """
        return self.id


    def get_menu_item_name(self):
        """ returns menu item name """ 
        return self.menu_item_name

    def get_menu_item_no(self):
        """ returns menu  item no """
        return self.menu_item_no

    def get_date_added(self):
        """ returns date added """
        return self.date_added
    
    def menu_item_description(self):
        raise NotImplementedError("abstract method")

    def set_price(self, price):
        """ sets menu item price """
        self.price = price

    def get_price(self):
        """ returns menu item price """
        return self.price

    def get_type(self):
        raise NotImplementedError("abstract method")    


    @staticmethod
    def _validate_menu_item_type(item_type):
        if (item_type == "food") or (item_type == "drink"):
            return 
        else:
            raise ValueError("Menu item must be of type food or drink")


