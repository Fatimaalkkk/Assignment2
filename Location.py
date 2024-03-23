#!/usr/bin/env python
# coding: utf-8

# In[1]:


class Location:
    # Here I have made constructor to initialize the Location object with provided attributes
    def __init__(self, location_id, location_name):
        # let’s Initialize location ID
        self.location_id = location_id
        # let’s Initialize location name
        self.location_name = location_name

    # Function to get the location ID
    def get_location_id(self):
        return self.location_id

    # Function to set the location ID
    def set_location_id(self, location_id):
        self.location_id = location_id

    # Function to get the location name
    def get_location_name(self):
        return self.location_name

    # Function to set the location name
    def set_location_name(self, location_name):
        self.location_name = location_name


# In[ ]:




