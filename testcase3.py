#!/usr/bin/env python
# coding: utf-8

# In[6]:


import datetime
from SpecialEvent import SpecialEvent

# Define a function to simulate the purchase of tickets by a tour group for a special event
def purchase_tickets_for_event(tour_group, special_event, num_tickets):
    # Simulate the purchase process
    print(f"Tour group '{tour_group}' purchased {num_tickets} tickets for the special event '{special_event.title}'")
    print(f"Location: {special_event.location}")
    print(f"Event Duration: {special_event.duration}")

# Example usage

# Define the SpecialEvent object
special_event = SpecialEvent("Musical Concert", "Hussain Al Jassmi", datetime.datetime(1503, 1, 1), "Music Night", "Concert", "Louvre Museum", datetime.timedelta(hours=2))

# Define the tour group
tour_group = "ABC Tours"

# Simulate the purchase of tickets for the special event by the tour group
purchase_tickets_for_event(tour_group, special_event, 20)


# In[ ]:




