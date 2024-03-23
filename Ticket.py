#!/usr/bin/env python
# coding: utf-8

# In[1]:


class Ticket:
    # let’s make a Constructor to initialize the Ticket object with provided attributes
    def __init__(self, ticket_id, ticket_price, date):
        # here I will Initialize ticket ID
        self.ticket_id = ticket_id
        # here I will ticket price
        self.ticket_price = ticket_price
        # here I will date
        self.date = date

    # This function is defined to get the ticket ID
    def get_ticket_id(self):
        return self.ticket_id

    # This function is defined to set the ticket ID
    def set_ticket_id(self, ticket_id):
        self.ticket_id = ticket_id

    # This function is defined to get the ticket price
    def get_ticket_price(self):
        return self.ticket_price

    # This function is defined to set the ticket price
    def set_ticket_price(self, ticket_price):
        self.ticket_price = ticket_price

    # This function is defined to get the date
    def get_date(self):
        return self.date

    # This function is defined to set the date
    def set_date(self, date):
        self.date = date



# In[ ]:




