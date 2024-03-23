#!/usr/bin/env python
# coding: utf-8

# In[1]:


class MembershipManagement:
    # let’s make a Constructor to initialize the MembershipManagement object with provided attributes
    def __init__(self, members, membership_start_date, membership_end_date, membership_type, membership_fee,
                 membership_renewal_date, membership_discounts, membership_events_access):
        # here I will Initialize list of members
        self.members = members
        # here I will membership start date
        self.membership_start_date = membership_start_date
        # here I will membership end date
        self.membership_end_date = membership_end_date
        # here I will membership type
        self.membership_type = membership_type
        # here I will membership fee
        self.membership_fee = membership_fee
        # here I will membership renewal date
        self.membership_renewal_date = membership_renewal_date
        # here I will membership discounts
        self.membership_discounts = membership_discounts
        # here I will membership events access
        self.membership_events_access = membership_events_access

    # This function is implemented to get the list of members
    def get_members(self):
        return self.members

    # This function is implemented to set the list of members
    def set_members(self, members):
        self.members = members

    # This function is implemented to get the membership start date
    def get_membership_start_date(self):
        return self.membership_start_date

    # This function is implemented to set the membership start date
    def set_membership_start_date(self, membership_start_date):
        self.membership_start_date = membership_start_date

    # This function is implemented to get the membership end date
    def get_membership_end_date(self):
        return self.membership_end_date

    # This function is implemented to set the membership end date
    def set_membership_end_date(self, membership_end_date):
        self.membership_end_date = membership_end_date

    # This function is implemented to get the membership type
    def get_membership_type(self):
        return self.membership_type

    # This function is implemented to set the membership type
    def set_membership_type(self, membership_type):
        self.membership_type = membership_type

    # This function is implemented to get the membership fee
    def get_membership_fee(self):
        return self.membership_fee

    # This function is implemented to set the membership fee
    def set_membership_fee(self, membership_fee):
        self.membership_fee = membership_fee

    # This function is implemented to get the membership renewal date
    def get_membership_renewal_date(self):
        return self.membership_renewal_date

    # This function is implemented to set the membership renewal date
    def set_membership_renewal_date(self, membership_renewal_date):
        self.membership_renewal_date = membership_renewal_date

    # This function is implemented to get the membership discounts
    def get_membership_discounts(self):
        return self.membership_discounts

    # This function is implemented to set the membership discounts
    def set_membership_discounts(self, membership_discounts):
        self.membership_discounts = membership_discounts

    # This function is implemented to get the membership events access
    def get_membership_events_access(self):
        return self.membership_events_access

    # This function is implemented to set the membership events access
    def set_membership_events_access(self, membership_events_access):
        self.membership_events_access = membership_events_access


# In[ ]:




