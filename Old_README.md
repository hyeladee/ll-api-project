# LL API Project (old readme)

This is an API project written in Python using Django Framework. Please note the following for a quick setup.

* Python v3.12 is recommeneded (install or update if need be)
* In your terminal, run ```pip install pipenv``` if ```pipenv``` is not already installed. Then use ```pipenv install --dev && pipenv shell``` to install all project dependencies in a virtual environment. 
* Run ```python manage.py runserver``` to run the code locally
* Access the code at ```http://127.0.0.1:8000/api``` or ```http://localhost:8000/api```

<br>

## Project Overview

The project is an online food shop that comprises the following features:
1. Menu-items with categories 
2. Sorting, filtering, searching and throttling
3. A cart to hold menu selection which is later processed into an order
4. Three levels of user authorization:
    * Mangers
    * Customers and
    * Delivery Crew
5. Something I can't remember right now.

<br>


## Endpoints

### 1. User Registration and Login

| Endpoint | Role Required for Access | HTTP Method | Purpose of Endpoint|
|---|---|---|---|
|```/api/users``` | No role required | ```POST``` | Creates a new user with name, email and password |
| ```/api/users/me``` | Anyone with a valid user token | ```GET``` | Displays only the current user |
| ```/api/token/login``` | Anyone with a valid username and password | ```POST``` | Generates access tokens that will be used in other API calls (token based authentication) |

<br><br>

### 2. User Management

| Endpoint | Role Required for Access | HTTP Method | Purpose of Endpoint|
|---|---|---|---|
| ```/api/groups/manager/users``` | Manager | ```GET``` | Returns all managers
| ```/api/groups/manager/users``` | Manager | ```POST``` | Assigns the user in the payload to the manager group and returns ```201 - Created```
| ```/api/groups/manager/users/{userId}``` | Manager | ```DELETE``` | Removes this particular user from the manager group and returns ```200 - Success``` if everything is okay. If the user is not found, returns ```404 - Not found```
| ```/api/groups/delivery-crew/users``` | Manager | ```GET``` | Returns all delivery crew
| ```/api/groups/delivery-crew/users``` | Manager | ```POST``` | Assigns the user in the payload to delivery crew group and returns ```201 - Created```
| ```/api/groups/delivery-crew/users/{userId}``` | Manager | ```DELETE``` | Removes this user from the delivery crew group and returns ```200 - Success``` if everything is okay. If the user is not found, returns ```404 - Not found```

<br>

> Please note that all registered users are by default customers. Managers and delivery crew roles have to be assigned explicitly.

<br>

### 3. Menu-Items

| Endpoint | Role Required for Access | HTTP Method | Purpose of Endpoint|
|---|---|---|---|
| ```/api/menu-items``` | Customer, delivery crew | ```GET``` | Lists all menu items. Return a 200 - Ok HTTP status code
| ```/api/menu-items``` | Customer, delivery crew | ```POST```, ```PUT```, ```PATCH```, ```DELETE``` | Denies access and returns 403 - Unauthorized HTTP status code
| ```/api/menu-items/{menuItem}``` | Customer, delivery crew | ```GET``` | Lists single menu item
| ```/api/menu-items/{menuItem}``` | Customer, delivery crew | ```POST```, ```PUT```, ```PATCH```, ```DELETE``` | Returns 403 - Unauthorized
| ```/api/menu-items``` | Manager | ```GET``` | Lists all menu items
| ```/api/menu-items``` | Manager | ```POST``` | Creates a new menu item and returns 201 - Created
| ```/api/menu-items/{menuItem}``` | Manager | ```GET``` | Lists single menu item
| ```/api/menu-items/{menuItem}``` | Manager | ```PUT```, ```PATCH``` | Updates single menu item
| ```/api/menu-items/{menuItem}``` | Manager | ```DELETE``` | Deletes menu item

<br>

### 4. Cart Management

| Endpoint | Role Required for Access | HTTP Method | Purpose of Endpoint|
|---|---|---|---|
| ```/api/cart/menu-items``` | Customer | ```GET``` | Returns current items in the cart for the current user token
| ```/api/cart/menu-items``` | Customer | ```POST``` | Adds the menu item to the cart. Sets the authenticated user as the user id for these cart items
| ```/api/cart/menu-items``` | Customer | ```DELETE``` | Deletes all menu items created by the current user token

<br>

### 5. Order Management

| Endpoint | Role Required for Access | HTTP Method | Purpose of Endpoint|
|---|---|---|---|
| ```/api/orders``` | Customer | ```GET``` | Returns all orders with order items created by this user
| ```/api/orders``` | Customer | ```POST``` | Creates a new order item for the current user. Gets current cart items from the cart endpoints and adds those items to the order items table. Then deletes all items from the cart for this user.
| ```/api/orders/{orderId}``` | Customer | ```GET``` | Returns all items for this order id. If the order ID doesn't belong to the current user, it displays an appropriate HTTP error status code.
| ```/api/orders``` | Manager | ```GET``` | Returns all orders with order items by all users
| ```/api/orders/{orderId}``` | Customer | ```PUT``` , ```PATCH``` | Updates the order. A manager can use this endpoint to set a delivery crew to this order, and also update the order status to 0 or 1. If a delivery crew is assigned to this order and the status = 0, it means the order is out for delivery. If a delivery crew is assigned to this order and the status = 1, it means the order has been delivered.
| ```/api/orders/{orderId}``` | Manager | ```DELETE``` | Deletes this order
| ```/api/orders``` | Delivery crew | ```GET``` | Returns all orders with order items assigned to the delivery crew
| ```/api/orders/{orderId}``` | Delivery crew | ```PATCH``` | A delivery crew can use this endpoint to update the order status to 0 or 1. The delivery crew will not be able to update anything else in this order.

<br><br>

## Predefined users

This is an API project, and all enpoints can be tested with any API testing software e.g Postman or Insomnia. However, the project was built using Django Rest Framework, which comes with a browsable API viewer, which is basic, but more convenient and can quickly check endpoints without any setup.

In order to view protected endpoints via this browsable API viewer, you need to login using the endpoint ```http://localhost:8000/api/alt-login``` and logout using the ```http://localhost:8000/api/logout```

Some users are already created to get you quickly set up. You can login with any of their credentials for a quick test.

<br>

> ### For browser testing (session authentication)
 
Login with any of the username and password combination below at ```http://localhost:8000/api/alt-login```, and logout using the ```http://localhost:8000/api/logout```:

| Username |  | Password |
|----------| - |----------|
|admin | - | blahblahblah
|manager | - | blahblahblah
|delivery_crew | - | blahblahblah
|customer | - | blahblahblah
|ustomer_1 | - | blahblahblah

<br>

> ### For other API client testing (insomnia, postman etc)

You can access any of the protected endpoints by using the appropriate ```bearer token``` for any of the user below:

| Username |  | Tokens |
|----------| - |----------|
|admin | - | b6d3a920d156727bfd8f3927a66a0951b17e26bf
|manager | - | 417cff6e4980e78296ba3280e053aca84b288161
|delivery_crew | - | 176b9f21a2abbb2cb3b34c7d1ec045382b909afa
|customer | - | 093d20624456da44bb1d6d4de516218d651464ca
|customer_1 | - | 8b905e13144efbb3a3a11c510480638ceeef3d37

<br>

> Note that you can create your own user, login to obtain a bearer token for protected endpoint visits or change authorization privillage of any user using previously defined endpoints (1 & 2 abve).


<br>

## Additional Featuers

**Pagination:**
all list queries and broken to 5 items per page

**Throttling:**
without login - 5 visit per minute
with login - 10 visits per minute

**Ordering:**
You can order how items are sorted using any of their attributes.
1. You can use ```?``` for parameter and ```=``` for value. Example ```/api/menu-items?ordering=category```
2. Also you can use ```-``` for descending order sorting. Example ```/api/menu-items?ordering=-category```