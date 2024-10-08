# Currency Exchange App

## Overview

This repository contains a **Currency Exchange Web Application** built using **Django**. The application allows users to convert an amount from one currency to another using real-time exchange rates. The project demonstrates both backend development using Django and frontend design with Bootstrap, highlighting my skills in full-stack web development.

## Technologies Used

- **Django**: Backend framework used for handling the server-side logic and routing.
- **HTML/CSS (Bootstrap)**: Used for designing a clean, responsive user interface.
- **OpenExchangeRates API**: Used to fetch real-time currency exchange rates.

## Objectives

The primary objectives of this project were to:

- Build a functional web application that integrates an external API for currency exchange rates.
- Demonstrate proficiency in backend development with Django.
- Apply Bootstrap for a responsive and modern user interface.
- Ensure the app provides real-time currency conversion with proper input validation and error handling.

## Project Features

- **Currency Conversion**: Users can input an amount and select two different currencies for conversion.
- **Real-time Exchange Rates**: The app uses real-time data from the OpenExchangeRates API (or similar) to fetch the most current exchange rates.
- **User-Friendly Interface**: The frontend design is responsive and clean, providing a simple interface for users to enter currency codes and amounts.

## Project Requirements

The project meets the following criteria:

- Integration of a third-party API to fetch live exchange rates.
- Use of Django for the backend, handling server-side logic and routing.
- Application of Bootstrap for responsive design and styling.
- Input validation and error handling for a smooth user experience.

## Final Product

The final product is a fully functional web application that allows users to convert currency values between different currencies. The app demonstrates a balance of backend logic (Django and API integration) and frontend design (Bootstrap). 

##Usage

Follow the steps below to set up and run the project on your local machine:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/currency-exchange-app.git
   cd currency-exchange-app
   ```
2. **Set up a virtual envirement**:
3. **Install packages**:
    ```bash
   pip install -r requirements.txt
   ```
4. **Apply migartions**:
```bash
   py manage.py migrate
   ```
5. **Run sever**:
```bash
   py manage.py runserver
   ```
6. **Use the application**
   On port http://127.0.0.1:8000/
