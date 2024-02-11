# live Link:


( pip freeze | sed 's/==.*$//' > requirements.txt )



# IST Cloth Store

Welcome to IST Cloth Store, an online clothing store built using Django. This web application allows users to register, verify their email, login, logout, manage their wallet balance, and purchase clothing items with various features for a seamless shopping experience.

## Table of Contents

- [Features](#features)
- [Setup](#setup)
- [Usage](#usage)
- [Screenshots](#screenshots)
- [Support](#support)

## Features

1. **User Authentication:**
   - Register an account with email verification.
   - Login and Logout securely.

2. **Wallet Management:**
   - Users can add balance to their wallet for convenient and quick purchases.

3. **Product Purchase:**
   - Buy individual products or all items in the cart.
   - Seamless checkout process.

4. **Product Management:**
   - Sort products by price, popularity, and other criteria.
   - Search for products by name or keyword.
   - Filter products by category, size, and color.

## Setup

1. **Clone the Repository:**
   ``` 
   git clone https://github.com/your-username/IST-Cloth-Store.git
   cd IST-Cloth-Store
2. Create Virtual Environment:
   ```
   python -m venv venv
3. Activate Virtual Environment:

1. On Windows:
   ```
   .\venv\Scripts\activate
2. On macOS/Linux:
   ```
   source venv/bin/activate
4. Install Dependencies:
   ```
   pip install -r requirements.txt
5. Database Migration:
   ```
   python manage.py migrate
6. Create Superuser:
   ```
   python manage.py createsuperuser
7. Run the Development Server:
   ```
   python manage.py runserver


Now Visit http://localhost:8000/ in your browser.

## Usage
Register an Account:

Visit the registration page and follow the instructions to verify your email.
Login:

Use your credentials to log in.

Add Balance:

Navigate to the wallet section to add balance to your account.
Explore and Purchase:

Browse products, filter, and sort as needed.
Add items to your cart and proceed to checkout.
Logout:

Logout securely when done.


## Screenshots

<img src="./sss/ss1.png" width="350" alt="schnehowebking" />  <img  src="./sss/ss2.png" width="350" alt="schnehowebking" />  <img  src="./sss/ss3.png" width="350" alt="schnehowebking" />  <img  src="./sss/ss4.png" width="350" alt="schnehowebking" />  <img  src="./sss/ss5.png" width="350" alt="schnehowebking" />  <img  src="./sss/ss6.png" width="350" alt="schnehowebking" />  <img  src="./sss/ss7.png" width="350" alt="schnehowebking" />


## Support
<p><a href="https://www.buymeacoffee.com/schnehowebking"> 
  <img align="left" src="https://cdn.buymeacoffee.com/buttons/v2/default-yellow.png" height="50" width="210" alt="schnehowebking" /></a>
</p>