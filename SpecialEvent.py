#!/usr/bin/env python
# coding: utf-8

# In[3]:


# Define the parent class Artwork
class Artwork:
    def __init__(self, title, artist, date_of_creation, historical_significance):
        self.title = title
        self.artist = artist
        self.date_of_creation = date_of_creation
        self.historical_significance = historical_significance

# Define the child class SpecialEvent inheriting from Artwork
class SpecialEvent(Artwork):
    # Constructor to initialize the SpecialEvent object with provided attributes
    def __init__(self, title, artist, date_of_creation, historical_significance, special_event_title, location, duration):
        # Call the constructor of the parent class Artwork
        super().__init__(title, artist, date_of_creation, historical_significance)
        
        # Initialize special event title
        self.special_event_title = special_event_title
        # Initialize location
        self.location = location
        # Initialize duration
        self.duration = duration

    # Method to get the special event title
    def get_special_event_title(self):
        return self.special_event_title

    # Method to set the special event title
    def set_special_event_title(self, special_event_title):
        self.special_event_title = special_event_title

    # Method to get the location
    def get_location(self):
        return self.location

    # Method to set the location
    def set_location(self, location):
        self.location = location

    # Method to get the duration
    def get_duration(self):
        return self.duration

    # Method to set the duration
    def set_duration(self, duration):
        self.duration = duration


# In[ ]:




