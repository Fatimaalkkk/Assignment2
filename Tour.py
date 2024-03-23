#!/usr/bin/env python
# coding: utf-8

# In[1]:


class Tour:
    # Here let’s make a constructor to initialize the Tour object with provided attributes
    def __init__(self, date, number_of_visitors, guide_name):
        # Here I will Initialize date
        self.date = date
        # Here I will Initialize number of visitors
        self.number_of_visitors = number_of_visitors
        # here I will Initialize guide name
        self.guide_name = guide_name

    # This function is to get the date
    def get_date(self):
        return self.date

    # This function is to set the date
    def set_date(self, date):
        self.date = date

    # This function is to get the number of visitors
    def get_number_of_visitors(self):
        return self.number_of_visitors

    # This function is to set the number of visitors
    def set_number_of_visitors(self, number_of_visitors):
        self.number_of_visitors = number_of_visitors

    # This function is to get the guide name
    def get_guide_name(self):
        return self.guide_name

        # This function is to set the guide name
    def set_guide_name(self, guide_name):
        self.guide_name = guide_name


# In[ ]:




