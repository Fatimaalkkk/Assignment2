#!/usr/bin/env python
# coding: utf-8

# In[9]:


class TicketPricing:
    # Let’s make a constructor to initialize the TicketPricing object with provided attributes
    def __init__(self, adult_price, child_price, senior_price, group_discount, vat, free_categories, vat_exempt_categories):
        # Initialize adult price
        self.adult_price = adult_price
        # Initialize child price
        self.child_price = child_price
        # Initialize senior price
        self.senior_price = senior_price
        # Initialize group discount
        self.group_discount = group_discount
        # Initialize VAT
        self.vat = vat
        # Initialize free categories
        self.free_categories = free_categories
        # Initialize VAT exempt categories
        self.vat_exempt_categories = vat_exempt_categories

    
   
    # This function is used to get the adult price
    def get_adult_price(self):
        return self.adult_price

# This function is used to set the adult price
    def set_adult_price(self, adult_price):
        self.adult_price = adult_price

    # This function is used to get the child price
    def get_child_price(self):
        return self.child_price

# This function is used to set the child price
    def set_child_price(self, child_price):
        self.child_price = child_price

# This function is used to get the senior price
    def get_senior_price(self):
        return self.senior_price

# This function is used to set the senior price
    def set_senior_price(self, senior_price):
        self.senior_price = senior_price

# This function is used to get the group discount
    def get_group_discount(self):
        return self.group_discount

# This function is used to set the group discount
    def set_group_discount(self, group_discount):
        self.group_discount = group_discount

# This function is used to get the VAT
    def get_vat(self):
        return self.vat

# This function is used to set the VAT
    def set_vat(self, vat):
        self.vat = vat

# This function is used to get the list of free categories
    def get_free_categories(self):
        return self.free_categories

# This function is used to set the list of free categories
    def set_free_categories(self, free_categories):
        self.free_categories = free_categories

# This function is used to get the list of VAT exempt categories
    def get_vat_exempt_categories(self):
        return self.vat_exempt_categories

# This function is used to set the list of VAT exempt categories
    def set_vat_exempt_categories(self, vat_exempt_categories):
        self.vat_exempt_categories = vat_exempt_categories
        


# In[ ]:





# In[ ]:




