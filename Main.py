#!/usr/bin/env python
# coding: utf-8

# In[7]:


from Artwork import Artwork
from Exhibition import Exhibition
from Location import Location
from SpecialEvent import SpecialEvent
from TicketPricing import TicketPricing
from Ticket import Ticket
from MembershipManagement import MembershipManagement
from Tour import Tour
from Visitor import Visitor


# In[21]:


import datetime

# Define the Exhibition object
exhibition = Exhibition("Arabic-Galactic Wonder", "Khaled", datetime.datetime(1503, 1, 1), "Iconic portrait", "Arab Art", "Exhibition Hall", datetime.timedelta(days=30))
# Define the Visitor object
visitor = Visitor("Fatima" , 20, "1234567890123456")

# Define the Artwork object
artwork = Artwork("Arabic-Galactic Wonder", "Khaled ", datetime.datetime(1503, 1, 1), "Iconic portrait", "Exhibition Hall")

# Print attributes of the Exhibition object
print("Exhibition Title:", exhibition.get_exhibition_title())
print("Location:", exhibition.get_location())
print("Duration:", exhibition.get_duration())

# Print attributes of the Visitor object
print("\nVisitor Name:", visitor.get_visitor_name())
print("Visitor Age:", visitor.get_visitor_age())
print("Emirates ID:", visitor.get_emirates_id())

# Print attributes of the Artwork object
print("\nArtwork Title:", artwork.title)
print("Artist:", artwork.artist)
print("Date of Creation:", artwork.date_of_creation)
print("Historical Significance:", artwork.historical_significance)


# In[ ]:




