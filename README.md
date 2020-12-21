# E-Commerce-Website 
- E-commerce Website built with django
- Use Django, Bootstrap, PostgreSQL, Celery, Redis
- Deploy on Heroku with AWS S3 storage
- Live Deployment: https://dlin99-django-ecommerce.herokuapp.com/


# Tech & Tools:
1. Backend: Django 3.1.3
2. Frontend: Bootstrap 4.3.1 
3. Database: Postgresql
4. Storage: AWS S3
5. Asynchronous Tasks: Celery + Redis
6. Payment: Paypal API (Sandbox)

# Functions:
- Shopping:
  - Purchase products as a logged in or a guest user.
  ![image](readme_images/cart.png)
- Logged In User:
  - Login and Signup Pages
  ![image](readme_images/login_signup_pages.png)
  - Forget Password, Reset via Email
  ![image](readme_images/reset_password1.png)
  ![image](readme_images/reset_password2.png)
  ![image](readme_images/reset_password3.png)
  - Change Password
  ![image](readme_images/change_password.png)
  - Profile/Change Profile Pages
  ![image](readme_images/profile.png)
  - My Orders Page/Order Details
  ![image](readme_images/my_orders.png)
  ![image](readme_images/order_detail.png) 
- Homepage:
  - Show all the products with pagination (6 items per page)
  ![image](readme_images/homepage.png)
- Product Page:
  - Show the details of individual product
  ![image](readme_images/product.png)
- Cart Page:
  - Show all the items in your shopping cart
  ![image](readme_images/cart.png)
- Checkout:
  - Use Paypal API to handle the payment
  ![image](readme_images/checkout.png)
  ![image](readme_images/paypal.png)
  - Confirmation Email will be sent after payment
  ![image](readme_images/confirmation_email.png)
  - Use Celery + Redis to handle the process of sending confirmation emails
- Contact Us:
  - Send email to us
  ![image](readme_images/contact_us.png)  
- NavBar:
  - Search bar for finding certain products
  ![image](readme_images/search_bar.png)

# To use:
1. git clone this repository to your computer
2. `python3 -m venv venv`
3. `. venv/bin/activate`
4. `pip install -r requirements.txt`
5. `python manage.py migrate`
6. `python manage.py createsuperuser`
7. run http://localhost:8000/


# Reference:
1. Project for the Course taught by Dennis Ivy. (https://www.youtube.com/playlist?list=PL-51WBLyFTg0omnamUjL1TCVov7yDTRng)