#!/usr/bin/env python
# coding: utf-8

# In[11]:


from Artwork import Artwork
from Exhibition import Exhibition
from Location import Location

import datetime

# Define a list to store artworks
artworks = []

# Define a list to store exhibitions
exhibitions = []

# Add some initial artworks to the list
initial_artworks = [
    Artwork("Arabic-Galactic Wonder", "Khaled", datetime.datetime(23, 1, 1), "Iconic portrait", "Outdoor Spaces")
]

for artwork in initial_artworks:
    artworks.append(artwork)

# Define the new exhibition
exhibition = Exhibition("Flower Exhibition", "Hasan", datetime.datetime(23, 1, 1), "The Beauty of Nature", "The Flowers", "Outdoor Spaces", datetime.timedelta(days=1))
# Add the new exhibition to the list of exhibitions
exhibitions.append(exhibition)

# Print details of all exhibitions in the list
print("New Exhibition added in the List:")
for exhibition in exhibitions:
    print("\nTitle:", exhibition.exhibition_title)
    print("Location:", exhibition.location)
    print("Duration:", exhibition.duration)  
    


# In[ ]:




