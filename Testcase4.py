#!/usr/bin/env python
# coding: utf-8

# In[37]:


# Import the datetime module
import datetime

# Import the TicketPricing and Ticket classes
from TicketPricing import TicketPricing
from Ticket import Ticket

# Define the generate_receipt function
def generate_receipt(tickets, ticket_pricing):
    total_amount = sum(ticket.ticket_price for ticket in tickets)
    
    # Apply group discount if applicable
    if len(tickets) >= 10:
        total_amount *= (1 - ticket_pricing.group_discount)
    
    # Calculate VAT
    vat_amount = total_amount * ticket_pricing.vat
    
    # Display receipt
    print("***** Payment Receipt *****")
    print("Date:", datetime.datetime.now())
    print("Number of Tickets:", len(tickets))
    print("Total Amount (before VAT): $", total_amount)
    print("VAT (", int(ticket_pricing.vat * 100), "% ): $", vat_amount)
    print("Total Amount (including VAT): $", total_amount + vat_amount)
    print("\nTickets Purchased:")
    
    # Variable to store the sum of ticket_id 1 and ticket_id 2 prices
    total_ticket_1_and_2_price = 0
    
    for i, ticket in enumerate(tickets, start=1):
        print(f"\nTicket {i}:")
        print("ID:", ticket.ticket_id)
        print("Price: $", ticket.ticket_price)
        print("Date:", ticket.date)
        
        # Add the prices of ticket_id 1 and ticket_id 2
        if ticket.ticket_id in [1, 2]:
            total_ticket_1_and_2_price += ticket.ticket_price
    
    # Print the total price of ticket_id 1 and ticket_id 2
    print("\nTotal Price of Ticket ID 1 and 2:", total_ticket_1_and_2_price)
    
    print("\nThank you for your purchase!")
    
    # Return the total amount
    return total_amount + vat_amount

# Create an instance of TicketPricing
ticket_pricing = TicketPricing(adult_price=50, child_price=30, senior_price=40, group_discount=0.1, vat=0.1, free_categories=['Staff'], vat_exempt_categories=['Government'])

# Create a list of Ticket objects representing the purchased tickets
tickets = [
    Ticket(ticket_id=1, ticket_price=50, date=datetime.datetime.now()),
    Ticket(ticket_id=2, ticket_price=30, date=datetime.datetime.now()),
    Ticket(ticket_id=3, ticket_price=40, date=datetime.datetime.now())
]

# Call the generate_receipt function and get the total bill
total_bill = generate_receipt(tickets, ticket_pricing)

# Print the total bill
print("Total Bill: $", total_bill)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




