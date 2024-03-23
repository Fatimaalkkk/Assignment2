#!/usr/bin/env python
# coding: utf-8

# In[1]:


class Artwork:
    def __init__(self, title, artist, date_of_creation, historical_significance, exhibition_location):
        """
        Here I have made Constructor method to initialize the Artwork object with provided attributes.
        """
        self.title = title  # Title of the artwork
        self.artist = artist  # Artist of the artwork
        self.date_of_creation = date_of_creation  # Date of creation of the artwork
        self.historical_significance = historical_significance  # Historical significance of the artwork
        self.exhibition_location = exhibition_location  # Exhibition location of the artwork

    def get_title(self):
        """
        Here I defined function to get the title of the artwork.
        """
        return self.title

    def set_title(self, title):
        """
       Here I defined another function to set the title of the artwork.
        """
        self.title = title

    def get_artist(self):
        """
        Here I defined another function to get the artist of the artwork.
        """
        return self.artist

    def set_artist(self, artist):
        """
        Here I defined function to set the artist of the artwork.
        """
        self.artist = artist

    def get_date_of_creation(self):
        """
This function is to get the date of creation of the artwork.
        """
        return self.date_of_creation

    def set_date_of_creation(self, date_of_creation):
        """
The use of this function is to set the date of creation of the artwork.
        """
        self.date_of_creation = date_of_creation

    def get_historical_significance(self):
        """
        This function is to get the historical significance of the artwork.
        """
        return self.historical_significance

    def set_historical_significance(self, historical_significance):
        """
        This function sets the historical significance of the artwork.
        """
        self.historical_significance = historical_significance

    def get_exhibition_location(self):
        """
        Function to get the exhibition location of the artwork.
        """
        return self.exhibition_location

    def set_exhibition_location(self, exhibition_location):
        """
        This function is used to set the exhibition location of the artwork.
        """
        self.exhibition_location = exhibition_location


# In[ ]:




