# LL API Project

An online food ordering API built with Python and Django. This project implements a robust backend for menu management, cart operations, and role-based order management. Below is a guide for quick setup, feature highlights, and endpoint documentation.

---

## Quick Setup

1. **Install Python**: Use Python v3.12 or later (install or update if needed).
2. **Install Pipenv**: Run `pip install pipenv` if it's not already installed.
3. **Install Dependencies**: Use `pipenv install --dev && pipenv shell` to install project dependencies in a virtual environment.
4. **Run the Server**: Start the development server with `python manage.py runserver`.
5. **Access the API**:
   - Browsable API: [http://127.0.0.1:8000/api](http://127.0.0.1:8000/api) or [http://localhost:8000/api](http://localhost:8000/api)

---

## Project Overview

The LL API project simulates an online food shop with the following features:

1. **Menu Management**: Menu items with categories, filters, and search capabilities.
2. **Role-based Access**:
   - **Managers**: Handle menu and order management.
   - **Customers**: Place and view orders.
   - **Delivery Crew**: Manage order deliveries.
3. **Cart System**: Add, view, and manage items in a shopping cart.
4. **Order Processing**: Transition cart items to orders with delivery status updates.
5. **Enhanced Usability**:
   - Pagination, throttling, sorting, and searching for improved API interaction.

---

## Endpoints

### 1. **User Registration and Login**

| Endpoint                  | Access Level                  | HTTP Method | Description                                   |
|---------------------------|-------------------------------|-------------|-----------------------------------------------|
| `/api/users`              | Public                       | `POST`      | Register a new user.                         |
| `/api/users/me`           | Authenticated User           | `GET`       | View details of the logged-in user.          |
| `/api/token/login`        | Authenticated User           | `POST`      | Obtain access tokens for authentication.     |

---

### 2. **User Management**

| Endpoint                          | Access Level    | HTTP Method | Description                                           |
|-----------------------------------|-----------------|-------------|-------------------------------------------------------|
| `/api/groups/manager/users`       | Manager         | `GET`       | List all managers.                                   |
| `/api/groups/manager/users`       | Manager         | `POST`      | Add a user to the manager group.                    |
| `/api/groups/manager/users/{id}`  | Manager         | `DELETE`    | Remove a user from the manager group.               |
| `/api/groups/delivery-crew/users` | Manager         | `GET`       | List all delivery crew members.                     |
| `/api/groups/delivery-crew/users` | Manager         | `POST`      | Add a user to the delivery crew group.              |
| `/api/groups/delivery-crew/users/{id}` | Manager   | `DELETE`    | Remove a user from the delivery crew group.         |

**Note**: All users are customers by default. Roles (manager, delivery crew) must be assigned explicitly.

---

### 3. **Menu Management**

| Endpoint                        | Access Level       | HTTP Method | Description                                   |
|---------------------------------|--------------------|-------------|-----------------------------------------------|
| `/api/menu-items`               | Customer, Delivery Crew | `GET` | List all menu items.                          |
| `/api/menu-items/{id}`          | Customer, Delivery Crew | `GET` | View a single menu item.                     |
| `/api/menu-items`               | Manager           | `POST`      | Create a new menu item.                      |
| `/api/menu-items/{id}`          | Manager           | `PUT/PATCH` | Update an existing menu item.                |
| `/api/menu-items/{id}`          | Manager           | `DELETE`    | Remove a menu item.                          |

---

### 4. **Cart Management**

| Endpoint                  | Access Level    | HTTP Method | Description                                   |
|---------------------------|-----------------|-------------|-----------------------------------------------|
| `/api/cart/menu-items`    | Customer        | `GET`       | View items in the user's cart.               |
| `/api/cart/menu-items`    | Customer        | `POST`      | Add an item to the cart.                     |
| `/api/cart/menu-items`    | Customer        | `DELETE`    | Clear the user's cart.                       |

---

### 5. **Order Management**

| Endpoint                  | Access Level    | HTTP Method | Description                                   |
|---------------------------|-----------------|-------------|-----------------------------------------------|
| `/api/orders`             | Customer        | `GET`       | List all orders created by the user.         |
| `/api/orders`             | Customer        | `POST`      | Create a new order from cart items.          |
| `/api/orders/{id}`        | Customer        | `GET`       | View order details for the given ID.         |
| `/api/orders/{id}`        | Manager, Crew   | `PATCH`     | Update order delivery status.                |

---

## Predefined Users

### Session Authentication
Use the following credentials at `/api/alt-login`:

| Username        | Password        |
|------------------|-----------------|
| `admin`         | `blahblahblah`  |
| `manager`       | `blahblahblah`  |
| `delivery_crew` | `blahblahblah`  |
| `customer`      | `blahblahblah`  |

### Token Authentication
For API testing tools like Postman or Insomnia, use the Bearer Tokens below:

| Username        | Token                                   |
|------------------|-----------------------------------------|
| `admin`         | `b6d3a920d156727bfd8f3927a66a0951b17e26bf` |
| `manager`       | `417cff6e4980e78296ba3280e053aca84b288161` |

---

## Additional Features

- **Pagination**: Lists are paginated with 5 items per page.
- **Throttling**: 
  - Unauthenticated users: 5 requests/minute.
  - Authenticated users: 10 requests/minute.
- **Sorting**:
  - Use `?ordering=attribute` (e.g., `?ordering=category`).
  - Add `-` for descending order (e.g., `?ordering=-price`).

---