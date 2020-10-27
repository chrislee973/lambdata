
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

### NLP HELPER FUNCTIONS ###

def tokens(text, lower = True, remove_stopwords = False): 
    """
    Returns a list of all the unique lowercased tokens in a text. If lower = True, they will be lowercased. 
    If remove_stopwords = True, stopwords will be removed from the list.
    
    """

    #tokenized list of words
    tokens = set(re.findall(r'\w+', self.text.lower()))

    if remove_stopwords:
        #filter out stopwords
        tokens = [token for token in tokens if token not in stopwords.words('english')] 
        return tokens
        
    else: 
        return tokens






