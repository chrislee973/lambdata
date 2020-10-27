
""" Class examples """

import pandas as pd
import re

class BareMinimumClass: 
    pass


class Complex: 
    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart 

    def add(self, other_complex): 
        self.r += other_complex.r
        self.i += other_complex.i 

    def __repr__(self): 
        return f"{self.r}, {self.i}"


class SocialMediaUser: 
    def __init__(self, name, location, upvotes=1): 
        self.name = str(name)
        self.location = location
        self.upvotes = upvotes
    
    def receive_upvotes(self, num_upvotes=1): 
        self.upvotes += num_upvotes

    def is_popular(self): 
        return self.upvotes > 100


class Animal: 
    def __init__(self, name, weight, diet_type): 
        self.name = str(name)
        self.weight = float(weight)
        self.diet_type = diet_type

    def run(self): 
        return "Vroom, vroom"

    def eat(self, food): 
        return "Huge fan of that " +str(food)


class Sloth(Animal): 
    def __init__(self, name, weight, diet_type, num_naps): 
        super().__init__(name, weight, diet_type)
        self.num_naps = int(num_naps)
    
    def say_something(self): 
        return "This is a sloth of typing"


class MyDataFrame(pd.DataFrame): 
    def num_cells(self): 
        return self.shape[0] * self.shape[1]









