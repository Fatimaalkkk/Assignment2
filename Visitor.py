#!/usr/bin/env python
# coding: utf-8

# In[1]:


class Visitor:
    # let’s make a Constructor to initialize the Visitor object with provided attributes
    def __init__(self, visitor_name, visitor_age, emirates_id):
        # let’s Initialize visitor name
        self.visitor_name = visitor_name
        # let’s Initialize visitor age
        self.visitor_age = visitor_age
        #let’s  Initialize Emirates ID
        self.emirates_id = emirates_id

    # Here I made function to get the visitor name
    def get_visitor_name(self):
        return self.visitor_name

    # This function is made to set the visitor name
    def set_visitor_name(self, visitor_name):
        self.visitor_name = visitor_name

    # The use of this function is to get the visitor age
    def get_visitor_age(self):
        return self.visitor_age

    # This function is used to set the visitor age
    def set_visitor_age(self, visitor_age):
        self.visitor_age = visitor_age

    # Function to retrieve the Emirates ID
    def get_emirates_id(self):
        return self.emirates_id

    # the Emirates ID can be set using this function
    def set_emirates_id(self, emirates_id):
        self.emirates_id = emirates_id


# In[ ]:




