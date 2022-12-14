# Plushies - Testing
# Manual Testing of the User Stories
User Story | Testing | Pass
--- | --- | :---:
As a user<br> I want to view a list of products to purchase. | As a user on the Home page I navigate to the Shop -> All Plushies to see all products or choose category that I'm interesed in. | :heavy_check_mark:
As a user<br> I want to view selected individual product details, the price, size, description and image. | As a user on the shop page or on the one of the plushies categories page I click individual product (either on the name or image). It takes me to the page with product details. I can easily notice product's name, available product's sizes, product's price, product's description and product's image. | :heavy_check_mark:
As a user<br> I want to view the total of my purchases at any time. | As a user I add items in the cart and I can see total of my purchases on every page on desktop and mobile | :heavy_check_mark:
As a user<br> I want to view a store contact information. | As a user I can navigate to the Contact Page. I can easily notice opening hours of the store and three ways of contact with store team - via message, email or phone. | :heavy_check_mark:
As a user<br> I want to contact easily with store owner via message form. | As a user on the Contact Page I can fill in message form to contact with the store. I have to fill all the fields. The email field has to be an email input to submit the form. After submiting the form I can see 'Thanks for your message!' notification, the form is empty, and ready to send another one. | :heavy_check_mark:
As a user<br> I want to register an account, so I can have a pesonal account to view my profile. | As a user I can navigate to the User Icon and from dropdown menu choose Register. To register account I need to provide E-mail address, Username, Password and click Register button. I can see notification that 'Confirmation email was sent to kewetop217@invodua.com' and I need to verify my email address. | :heavy_check_mark:
As a user<br> I want to receive an email confirmation after registering account to verify that my account registration was successful. | During registration process I received Email Verification link.  Once I confirm my email, I got redirect to Log In Page with notification 'You have confirmed kewetop217@invodua.com'.  | :heavy_check_mark:
As a user<br> I want to login and logout to access my personal account information | As registered user I can login provide username or email address and my password, I got redirect to Home Page with notification 'Successfully signed in as my username.' On the navbar I can navigate through user icon and dropdown menu to My Profile Page. On the Profile Page I can provide my delivery information, such as: Phone Number, Street Address, City, County, Post Code and Country. I can see my order history, which is empty for now. | :heavy_check_mark:
As a user<br> I want to easily enter my payment information so I can checkout quickly. | On the My Profile page I can add my details into Default Delivery Information form with Phone Number, Street Address, City, County, Post Code and Country, and click update information button. | :heavy_check_mark:
As a user<br> I want to be able recover my password so I have access to my account | On the Log In Page I can choose 'Forgot the password' option. I been redirect to the Password Reset Page where I can provide my email address and click Reset My Password button. I've been informed that Email with Password Reset was send. I check my mailbox and now I can change my Password to new one. I've set my new password and I've been notified that 'Password successfully changed.' | :heavy_check_mark:
As a user<br> I want to have a personalised user profile so I can view my order history, order confirmations, and save my payment information. | As a user I can navigate to the My Profile page and save my Default Delivery Information. I can easly check my Order History and navigate to the details of the specific order by clicking on the order number. It redirect me to the History Order Details where I can check information about order number, order date, what products I ordered with quantity and price, total payment charges, and delivery information that were used to send products to me. | :heavy_check_mark:
As a user<br> I want to sort the list of available products by price, by name or by category name. | As a user I can navigate to the Shop All Plushies to see all products. I can choose the way I want to sort products on the page. I can sort products by price (from the lowest to the highest, and from the highest to the lowest), by name (from A to Z, and from Z to A), by category (from A to Z and from Z to A). | :heavy_check_mark:
As a user<br> I want to sort a specific category of product by price or by name. | As a user I can navigate to the Animals Plushies, Food Plushies, or Gaming Plushies and sort products only in the chosen category by price or by name. | :heavy_check_mark:
As a user<br> I want to search for product by name or color to find specific product. | As a user I can search for product on the search box in the navbar. I can enter product's name or color that I am interested in, and it finds me products if exists. | :heavy_check_mark:
As a user<br> I want to see what I've searched for and how many products was found | As a user I want to search for red product, I can see on the page how many products found for resukt "red". If I type query that does not find products for I can see on the page that it found '0 results for "batman"'. If I enter empty search I got notification error with message 'Search criteria empty!' | :heavy_check_mark:
As a user<br> I want to select the size and quantity of a product. | As a user I can navigate to the selected product and choose beetween available sizes of the product. I can choose quantity of the product. | :heavy_check_mark:
As a user<br> I want to view products in my cart and identify total cost of my purchase. | As a user I can navigate to the shopping cart. I can easly see how many products I have in my cart for what price. I can identify total cost of my purchase on the bottom of the shopping cart. | :heavy_check_mark:
As a user<br> I want to modify the quantity of individual items in the cart, so I can make a change to my purchase before checkout. | As a user in the shopping cart with chosen products to purchase I can easily modify quantity of my products, by decreasing or increasing the amount by clicking on the button | :heavy_check_mark:
As a user<br> I want to view the order confirmation after checkout. | As a user I provided necesery information and purchased items. I can see order confirmation page with order details. | :heavy_check_mark:
As a user<br> I want to receive a confirmation email after checkout, to keep the confirmation for my records. | As a user after successful checkout I received a confirmation email. | :heavy_check_mark:
As a store owner<br> I want to add products to my store. | once logged onto my admin user, I can navigate through the user icon and from dropdown menu I can click on the Admin. I can add product via Add Product Form, where I can choose category and size, add name, description, price, color, country that product was made in, and image but it is not required. If I add a product without an image it render with image placeholder - bear. As it is more visually appealing then no graphic at all. | :heavy_check_mark:
As a store owner<br> I want to edit the product details. | As a store owner I can edit products on the shop page or in the product's details page by clicking the edit button. It redirects me to the edit page with notification of what Product I am editing. I can change any field and click button to update the chosen product. | :heavy_check_mark:
As a store owner<br> I want to delete the products that are no longer for sale. | As a store owner I can delete products on the shop page or in the product's details page by clicking the delete button. I can see pop up information if I am sure to delete the chosen product, where I need to confirm deleting while still having an option to cancel. It redirects me to the shop page with notification 'Product deleted!'. | :heavy_check_mark:

# Code Validation
## HTML5 Validation
I used [HTML5 Validator](https://validator.w3.org/) to validate my html code. I validate by URI and by Direct Input.
<details><summary>Home</summary>
<img src="documentation/html-validation-home.jpg">
</details>

<details><summary>Shop - All Categories</summary>
<img src="documentation/html-validation-shop.jpg">
</details>

<details><summary>Food Plushies</summary>
<img src="documentation/html-validation-food-plushies.jpg">
</details>

<details><summary>Gaming Plushies</summary>
<img src="documentation/html-validation-gaming-plushies.jpg">
</details>

<details><summary>Animales Plushing</summary>
<img src="documentation/html-validation-animales-plushing.jpg">
</details>

<details><summary>Contact</summary>
<img src="documentation/html-validation-contact.jpg">
</details>

<details><summary>Cart</summary>
<img src="documentation/html-validation-cart.jpg">
</details>

<details><summary>Checkout</summary>
<img src="documentation/html-validation-checkout.jpg">
</details>

<details><summary>Checkout Success</summary>
<img src="documentation/html-validation-checkout-success.jpg">
</details>

<details><summary>Register</summary>
<img src="documentation/html-validation-register.jpg">
</details>

<details><summary>Log In</summary>
<img src="documentation/html-validation-login.jpg">
</details>

<details><summary>Log Out</summary>
<img src="documentation/html-validation-logout.jpg">
</details>

<details><summary>Profile</summary>
<img src="documentation/html-validation-profile.jpg">
</details>

<details><summary>Order History</summary>
<img src="documentation/html-validation-order-history.jpg">
</details>

<details><summary>Add-product</summary>
<img src="documentation/html-validation-add-product.jpg">
</details>

## CSS3 Validation
I used [CSS3 Validator](https://jigsaw.w3.org/css-validator/) to validate my css code. I validate by file upload.

<details><summary>base.css</summary>
<img src="documentation/css-validation-base-css.jpg">
</details>

<details><summary>checkout.css</summary>
<img src="documentation/css-validation-checkout-css.jpg">
</details>

<details><summary>profile.css</summary>
<img src="documentation/css-validation-profile-css.jpg">
</details>

## JavaScript Validation
I used [JSHint Validator](https://jshint.com/) to validate my javascript code. I validate by direct input.

<details><summary>Base</summary>
<img src="documentation/js-validation-base.jpg">
</details>

<details><summary>Cart</summary>
<img src="documentation/js-validation-cart.jpg">
</details>

<details><summary>Checkout</summary>
<img src="documentation/js-validation-checkout.jpg">
</details>

<details><summary>Products</summary>
<img src="documentation/js-validation-products.jpg">
</details>

<details><summary>Products Quantity</summary>
<img src="documentation/js-validation-products-quantity.jpg">
</details>

<details><summary>Profiles</summary>
<img src="documentation/js-validation-profiles.jpg">
</details>

## Python Validation
I used [Code Institue pep8ish Validator](https://pep8ish.herokuapp.com/) to validate my python code. I validate by raw file from github and pasting into url.

### Cart App

<details><summary>Apps</summary>
<img src="documentation/python-validation-cart-apps.jpg">
</details>

<details><summary>Context</summary>
<img src="documentation/python-validation-cart-context.jpg">
</details>

<details><summary>Urls</summary>
<img src="documentation/python-validation-cart-urls.jpg">
</details>

<details><summary>Views</summary>
<img src="documentation/python-validation-cart-views.jpg">
</details>

### Checkout App

<details><summary>Admin</summary>
<img src="documentation/python-validation-checkout-admin.jpg">
</details>

<details><summary>Apps</summary>
<img src="documentation/python-validation-checkout-apps.jpg">
</details>

<details><summary>Forms</summary>
<img src="documentation/python-validation-checkout-forms.jpg">
</details>

<details><summary>Models</summary>
<img src="documentation/python-validation-checkout-models.jpg">
</details>

<details><summary>Signals</summary>
<img src="documentation/python-validation-checkout-signals.jpg">
</details>

<details><summary>Urls</summary>
<img src="documentation/python-validation-checkout-urls.jpg">
</details>

<details><summary>Views</summary>
<img src="documentation/python-validation-checkout-views.jpg">
</details>

<details><summary>Webhook Handler</summary>
<img src="documentation/python-validation-checkout-webhook-handler.jpg">
</details>

<details><summary>Webhooks</summary>
<img src="documentation/python-validation-checkout-webhooks.jpg">
</details>

### Home App

<details><summary>Apps</summary>
<img src="documentation/python-validation-home-apps.jpg">
</details>

<details><summary>Urls</summary>
<img src="documentation/python-validation-home-urls.jpg">
</details>

<details><summary>Views</summary>
<img src="documentation/python-validation-home-views.jpg">
</details>

### Plushies Main

<details><summary>Asgi</summary>
<img src="documentation/python-validation-home-asgi.jpg">
</details>

<details><summary>Settings</summary>
<img src="documentation/python-validation-home-settings.jpg">
</details>

<details><summary>Urls</summary>
<img src="documentation/python-validation-plushies-urls.jpg">
</details>

<details><summary>Wsgi</summary>
<img src="documentation/python-validation-plushies-wsgi.jpg">
</details>

### Products App

<details><summary>Admin</summary>
<img src="documentation/python-validation-products-admin.jpg">
</details>

<details><summary>Apps</summary>
<img src="documentation/python-validation-products-apps.jpg">
</details>

<details><summary>Forms</summary>
<img src="documentation/python-validation-products-forms.jpg">
</details>

<details><summary>Models</summary>
<img src="documentation/python-validation-products-models.jpg">
</details>

<details><summary>Urls</summary>
<img src="documentation/python-validation-products-urls.jpg">
</details>

<details><summary>Views</summary>
<img src="documentation/python-validation-products-views.jpg">
</details>

### Profiles App

<details><summary>Apps</summary>
<img src="documentation/python-validation-profiles-apps.jpg">
</details>

<details><summary>Forms</summary>
<img src="documentation/python-validation-profiles-forms.jpg">
</details>

<details><summary>Models</summary>
<img src="documentation/python-validation-profiles-models.jpg">
</details>

<details><summary>Urls</summary>
<img src="documentation/python-validation-profiles-urls.jpg">
</details>

<details><summary>Views</summary>
<img src="documentation/python-validation-profiles-views.jpg">
</details>

# Lighthouse Testing
<details><summary>Home</summary>
<img src="documentation/lighthouse-home.png">
</details>

<details><summary>Shop - All Categories</summary>
<img src="documentation/lighthouse-shop.png">
</details>

<details><summary>Food Plushies</summary>
<img src="documentation/lighthouse-food-plushies.png">
</details>

<details><summary>Gaming Plushies</summary>
<img src="documentation/lighthouse-gaming-plushies.png">
</details>

<details><summary>Animals Plushing</summary>
<img src="documentation/lighthouse-animals-plushies.png">
</details>

<details><summary>Contact</summary>
<img src="documentation/lighthouse-contact.png">
</details>

<details><summary>Cart</summary>
<img src="documentation/lighthouse-cart.png">
</details>

<details><summary>Checkout</summary>
<img src="documentation/lighthouse-checkout.png">
</details>

<details><summary>Checkout Success</summary>
<img src="documentation/lighthouse-checkout-success.png">
</details>

<details><summary>Register</summary>
<img src="documentation/lighthouse-register.png">
</details>

<details><summary>Log In</summary>
<img src="documentation/lighthouse-login.png">
</details>

<details><summary>Log Out</summary>
<img src="documentation/lighthouse-logout.png">
</details>

<details><summary>Profile</summary>
<img src="documentation/lighthouse-profile.png">
</details>

<details><summary>Order History</summary>
<img src="documentation/lighthouse-order-history.png">
</details>

<details><summary>Add-product</summary>
<img src="documentation/lighthouse-add.png">
</details>

# Bugs

1. Images not loading on the page
    <details><summary>Screenshot</summary>
    <img src="documentation/bug-1.jpg">
    </details>
    To fix this problem I needed to add:

    ```
    'django.template.context_processors.media'
    ```

    to the settings.py in the TEMPLATES

2. Layout issues with icons in the navbar on the mobile view
    <details><summary>Screenshot</summary>
    <img src="documentation/bug-2.jpg">
    </details>
    To fix it I needed to find elements that had extra paddings and marings, and change it.

3. Layout issues with icons in the navbar on the mobile view
    <details><summary>Screenshot</summary>
    <img src="documentation/bug-3.jpg">
    </details>
    The problem here was with icons elements being nested in the wrong parent element, so I needed to move out of div with classes: collapse, navbar-collapse.

4. Layout issues with dropdown menu in the navbar on the mobile view
    <details><summary>Screenshot</summary>
    <img src="documentation/bug-4.jpg">
    </details>
    I fixed the problem with adding class 'position-absolute' on the unorder list element with class 'dropdown-menu'.

5. Layout issues with extra space on the right of the screen.
    <details><summary>Screenshot</summary>
    <img src="documentation/bug-5.jpg">
    </details>
    I fixed the problem by wrapping a free delivery banner element with div with class 'container-fluid'.

6. Could not make migrations for the profiles app. ModuleNotFoundError: No module names 'progiles'
    <details><summary>Screenshot</summary>
    <img src="documentation/bug-6.jpg">
    </details>
    A quick fix of changing a typo made in the settings.py in the INSTALLED_APPS. I change 'progiles' for 'profiles'.

7. Could not load shop page. NameError at /shop/
    <details><summary>Screenshot</summary>
    <img src="documentation/bug-7.jpg">
    </details>
    I fixed the problem with importing Product Model in the begning of the views.py.

8. Could not sort products. ProgrammingError at /shop/
    <details><summary>Screenshot</summary>
    <img src="documentation/bug-8.jpg">
    </details>
    On this bug I spent a lot of time. I get products objects by distinct to not duplicate same products on the shop page but I could not sort on that. So I need to get all objects and sort and then filter and distinct them. I find the way to work out the syntax for that:

    ```
    products = products.filter(id__in=Product.objects.order_by('name', 'price').distinct('name')).order_by(sortkey)
    ```

9. User could submit empty message form on the contact page. That cause bug in the django admin panel, because admin could not delete message None. To fix that I added str() method in the return:

    ```
    def __str__(self):
        return str(self.name)
    ```
    To prevent in the future submiting empty forms I added requied attribute on all message form's fields. In the for loop in the forms.py I added:

    ```
    self.fields[field].widget.attrs['required'] = 'required'
    ```

10. After submiting the message form on the contact page, the form contained still last submited output. To fix that I added in the contact function in the views.py
    ```
    contact_form = ContactForm()
    ```

in the if statement with valid form so the form outout would be empty.

11. Every time user clicked refresh page after submiting the message form on the contact page, the form would send for every click. To fix that I added return in the views.py in the contact function:
    ```
    return redirect(reverse('contact'))
    ```

# Testing Devices
I tested website on the windows 11 pc with Google Chrome and Edge.

I tested mobile version on the iPhone 12 Pro and iPhone12 Pro Max.