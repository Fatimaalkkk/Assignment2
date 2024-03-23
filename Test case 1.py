#!/usr/bin/env python
# coding: utf-8

# In[8]:


from Artwork import Artwork
from Exhibition import Exhibition
from Location import Location
from SpecialEvent import SpecialEvent
from TicketPricing import TicketPricing
from Ticket import Ticket
from MembershipManagement import MembershipManagement
from Tour import Tour
from Visitor import Visitor
import datetime

# Get the current date
current_date = datetime.datetime.now().date()

# Define a list to store artworks
artworks = []

# Add some initial artworks to the list
initial_artworks = [
    Artwork("Arabic-Galactic Wonder", "Khaled ", current_date, "Iconic portrait", "Outdoor Spaces")
]
for artwork in initial_artworks:
    artworks.append(artwork)

# Define the new artwork to be added
new_artwork = Artwork("The wonder women", "shaikha", current_date, "Beautiful Painting", "Exhibition Hall")

# Add the new artwork to the list
artworks.append(new_artwork)

# Print details of all artworks in the list
print("All Artworks in the List:")
for artwork in artworks:
    print("\nTitle:", artwork.title)
    print("Artist:", artwork.artist)
    print("Date of Creation:", artwork.date_of_creation)
    print("Historical Significance:", artwork.historical_significance)



# In[ ]:




