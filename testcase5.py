#!/usr/bin/env python
# coding: utf-8

# In[3]:


# Import the MembershipManagement class
from MembershipManagement import MembershipManagement

# Sample data for testing
members = ["Fatima", "Mariam", "Aisha"]
membership_start_date = "2024-01-01"
membership_end_date = "2024-12-31"
membership_type = "Gold"
membership_fee = 1000
membership_renewal_date = "2025-01-01"
membership_discounts = {"Senior Discount": 0.1, "Student Discount": 0.2}
membership_events_access = ["Event A", "Event B", "Event C"]

# Create an instance of the MembershipManagement class
membership = MembershipManagement(
    members=members,
    membership_start_date=membership_start_date,
    membership_end_date=membership_end_date,
    membership_type=membership_type,
    membership_fee=membership_fee,
    membership_renewal_date=membership_renewal_date,
    membership_discounts=membership_discounts,
    membership_events_access=membership_events_access
)

# Print all provided information before update
print("Before Update:")
print("Members:", membership.get_members())
print("Membership Start Date:", membership.get_membership_start_date())
print("Membership End Date:", membership.get_membership_end_date())
print("Membership Type:", membership.get_membership_type())
print("Membership Fee:", membership.get_membership_fee())
print("Membership Renewal Date:", membership.get_membership_renewal_date())
print("Membership Discounts:", membership.get_membership_discounts())
print("Membership Events Access:", membership.get_membership_events_access())

# Test case: Update membership information
print("\nUpdating membership information...")

# Update membership type and fee
new_membership_type = "Platinum"
new_membership_fee = 1500
membership.set_membership_type(new_membership_type)
membership.set_membership_fee(new_membership_fee)

# Print all provided information after update
print("\nAfter Update:")
print("Members:", membership.get_members())
print("Membership Start Date:", membership.get_membership_start_date())
print("Membership End Date:", membership.get_membership_end_date())
print("Membership Type:", membership.get_membership_type())
print("Membership Fee:", membership.get_membership_fee())
print("Membership Renewal Date:", membership.get_membership_renewal_date())
print("Membership Discounts:", membership.get_membership_discounts())
print("Membership Events Access:", membership.get_membership_events_access())


# In[ ]:




