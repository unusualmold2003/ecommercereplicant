# Amazon Shopping Simulation

This project simulates an Amazon-like online shopping experience using Python and Tkinter. Users can browse through different categories such as **Electronics**, **Furniture**, and **Grocery**, add items to their cart, apply coupons, and place orders.

## Features

- **Categories**: 
  - **Electronics**: Browse and purchase items such as mobiles, AirPods, and chargers.
  - **Furniture**: Buy home essentials like tables, chairs, and desks.
  - **Grocery**: Shop for daily necessities such as milk, potatoes, and tomatoes.
  
- **Cart Functionality**: 
  - Add items to the cart from different categories.
  - View and calculate the total price along with GST.
  - Apply discount coupons for additional savings.

- **Order Placement**: 
  - After viewing the final bill, users can place an order and receive confirmation.

## Project Structure

- **Frontend**: Tkinter is used to create the GUI for a seamless shopping experience.
- **Categories**: The shopping experience is divided into the following sections:
  - **Electronics**
  - **Furniture**
  - **Grocery**
- **Cart System**: Items can be added to the cart with prices calculated dynamically.

## Screens

1. **Home Screen**: 
   - Welcome message and options to explore different product categories.

2. **Category Screens**: 
   - Displays available products and prices with a "Buy Now" option for each item.

3. **Cart and Billing**: 
   - Users can review the cart, see the applied GST, and input a discount coupon if available. The total is displayed, and users can proceed with placing their order.

## Usage

1. **Shopping**: 
   - Run the program and choose a category. 
   - Select the items you want to add to your cart.
   - After adding items, click on the "Cart" button to proceed with billing.

2. **Applying Coupons**: 
   - You can apply a discount coupon during checkout to receive a flat discount on the total bill.

3. **Order Placement**: 
   - Once you’re satisfied with your selections and the discount applied, place the order to complete your shopping.

## Installation

1. Clone the repository or download the code files.
2. Install the required libraries:
   ```bash
   pip install tkinter
