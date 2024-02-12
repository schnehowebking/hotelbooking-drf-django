# Hotel Booking API

## Description

This is a simple hotel booking website where users can explore hotels, leave reviews, and manage their accounts. The website offers the following features:

1. **User Registration and Authentication**: Users can register, log in, and log out. Upon registration, users receive an email verification link to activate their accounts.

2. **Hotel Detail Page**: Detailed information about each hotel is displayed on a dedicated page. This includes the hotel name, address, photos, and reviews.

3. **Hotel Booking and Confirmation**: Users can book hotels using their deposited money. Upon booking, users receive a confirmation email for their reservation.

4. **Hotel Reviews**: Authenticated users can leave reviews for hotels they have stayed at. Each review includes a rating and a text comment. Only the author of a review can modify or remove it.

## Features

### User Registration and Authentication 

- User registration with email verification
- User login and logout functionality

### Hotel Detail Page 

- Display detailed information about each hotel
- Show hotel name, address, photos, and reviews

### Hotel Booking and Confirmation

- Allow users to book hotels using deposited money
- Send confirmation email for booked hotels

### Hotel Reviews 

- Authenticated users can leave reviews for hotels
- Each review includes a rating and a text comment
- Users can only modify or remove their own reviews

## User Account Management

- Users can manage their accounts by updating profile information
- Users can reset passwords if forgotten
- Users can view their booking history

## Technologies Used

- **Frontend**: HTML, CSS, JavaScript, Bootstrap
- **Backend**: Django (Python)
- **Database**: SQLite (for development), PostgreSQL (for production)
- **Authentication**: Django Authentication System with Email Verification
- **Email**: SMTP (Simple Mail Transfer Protocol) for sending verification emails
- **Payment Gateway**: Integration with a payment gateway for hotel bookings

## How to Run

1. Clone the repository.
2. Set up the Django environment and install dependencies.
3. Run database migrations.
4. Start the Django development server.
5. Access the website through the provided URL.

## Future Improvements

- Implement OAuth for social media login.
- Enhance the user interface for a better user experience.
- Add more features such as hotel search and filtering options.
- Integrate with a real payment gateway for booking transactions.
