#!/usr/bin/env python
# coding: utf-8

# In[1]:


class Artwork:
    def __init__(self, title, artist, date_of_creation, historical_significance):
        self.title = title
        self.artist = artist
        self.date_of_creation = date_of_creation
        self.historical_significance = historical_significance

    # Other methods of the Artwork class can be added here

# Define the child class Exhibition inheriting from Artwork
class Exhibition(Artwork):
    def __init__(self, title, artist, date_of_creation, historical_significance, exhibition_title, location, duration):
        # Call the constructor of the parent class Artwork
        super().__init__(title, artist, date_of_creation, historical_significance)       

 # here I will initialize exhibition title
        self.exhibition_title = exhibition_title
        # here I will  Initialize location
        self.location = location
        # here I will Initialize duration
        self.duration = duration

    # I have made this function to get the exhibition title
    def get_exhibition_title(self):
        return self.exhibition_title

# I have made this function to set the exhibition title
    def set_exhibition_title(self, exhibition_title):
        self.exhibition_title = exhibition_title

# I have made this function to get the location
    def get_location(self):
        return self.location

# I have made this function to set the location
    def set_location(self, location):
        self.location = location

# I have made this function to get the duration
    def get_duration(self):
        return self.duration

# I have made this function to set the duration
    def set_duration(self, duration):
        self.duration = duration        


# In[ ]:




