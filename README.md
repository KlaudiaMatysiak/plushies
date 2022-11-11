# Plushies
## Table of Contents
* [Introduction](#introduction)
* [UX](#ux)
    * [User Stories](#users-tories)
    * [Design](#design)
    * [Wireframes](#wireframes)
        * [Mobile Wireframes](#mobile-wireframes)
        * [Desktop Wireframes](#desktop-wireframes)
* [Database](#database)
* [Features](#features)
    * [Navbar](#navbar)
    * [Home Page](#home-page)
    * [Footer](#footer)
    * [Shop Page](#shop-page)
    * [Contact](#contact)
    * [Shopping Cart](#shopping-cart)
    * [Checkout](#checkout)
    * [Successful checkout](#successful-checkout)
    * [Register](#register)
    * [Verify Email](#verify-email)
    * [Login](#login)
    * [User Profile](#user-profile)
    * [History order details](#history-order-details)
    * [Admin Page](#admin-page)
    * [Messages](#messages)
* [Technologies Used](#technologies-used)
    * [Languages](#languages)
    * [Libraries and Programs](#libraries-and-programs)
* [Testing](#testing)
* [Deployment](#deployment)
* [Credits](#credits)

# Introduction
It is the final project for the 'Full Stack Frameworks with Django' module at Code Institute. The Plushies project is an eCommerce shop that is offering to sell plushies.
Please note that this website is for eductional purposes. Do not enter any personal credit/debit card details.
## Testing Payment with Stripe
As a way of exemplifying how the payment functionality works, Stripe provides three types of payment events and their respective card numbers: successful payment, requires authentication and failed payment.

| Payment event | Card Number
|:---:|:---:|
|Successful payment|4242 4242 4242 4242
|Requires authentication|4000 0025 0000 3155
|Failed payment|4000 0000 0000 9995

Additional information:
* Use a valid future date.
* Use any three-digit CVC.


# UX

## User Stories
### User
* As a user, I want to view a list of products to purchase.
* As a user, I want to view selected individual product details, the price, size,description and image.
* As a user, I want to view the total of my purchases at any time.
* As a user, I want to view a store contant information.
* As a user, I want to register an account, so I can have a pesonal account to view my profile.
* As a user, I want to login and logout to access my personal account information.
* As a user, I want to be able recover my password so I have access to my account.
* As a user, I want to receive an email confirmation after registering account to verify that my account registration was successful.
* As a user, I want to have a poersonalised user profile so I can view my order history and order confirmations, and save my payment information.
* As a user, I want to sort the list of available products by price, by name or by category name.
* As a user, I want to sort a specific category of product by price or by name.
* As a user, I want to search for product by name or description to find specific product.
* As a user, I want to see what I've searched for and how many products was found.
* As a user, I want to select the size and quantity of a product.
* As a user, I want to view products in my cart and identify total cost of my purchase.
* As a user, I want to modify the quantity of individual items in the cart, so I can make a change to my purchase before checkout.
* As a user, I want to view items in the cart to be purchased and its total cost.
* As a user, I want to modify the quantity of individual item in the cart, so I can easily change it before checkout.
* As a user, I want to easily enter my payment information so I can checkout quickly.
* As a user, I want to view on order confirmation after checkout.
* As a user, I want to receive an email confirmation after checkout, to keep the confirmation for my records.
### Store Owner
* As a store owner, I want to add product to my store.
* As a store owner, I want to edit details product.
* As a store owner, I want to delete a products that are no longer for sale.

## Design
![palette](documentation/palette.jpg)
The colors palettes for website layout are Cultured, White, and Dark Slate Grey. For the links in the Register and Login page is used Ming color.

## Wireframes
I created wireframes in the Balsamiq program as first visual concept of the website.

### Mobile Wireframes
PDF file here

![Mobile Wireframes](documentation/mobile-wireframe.jpg)
### Desktop Wireframes
PDF file here

![Desktop Wireframes](documentation/desktop-wireframes.jpg)

## Database
To create database schema I used [dbdiagram.io](https://dbdiagram.io/)

![Database](documentation/database.jpg)

## Features
### Navbar
### Home Page
### Footer
### Shop Page
### Contact
### Shopping Cart
### Checkout
### Successful checkout
### Register
### Verify Email
### Login
### User Profile
### History order details
### Admin Page
### Messages

# Technologies Used
##  Languages
* HTML5
* CSS3
* Python
* Javascript
## Libraries and Programs
* [Git](https://git-scm.com/) - Git was used for version control.
* [GitHub](https://github.com/) - GitHub was used for storing code and deploying the site.
* [Gitpod](https://www.gitpod.io/) - GitPod was used for building and editing my code.
* [Heroku](https://www.heroku.com/) - Heroku was used to deploy the project.
* [Django](https://www.djangoproject.com/) - Django was used for creating store website.
* [PostgreSQL](https://www.postgresql.org/) - PostgreSQL was used to store products, products sizes and categories, users, user's profiles, orders colections in the database
* [AWS S3](https://aws.amazon.com/s3/) - AWS S3 was used for storing media and static files.
* [Stripe](https://stripe.com/en-gb) - Stripe was used for payment gateway.
* [Bootstrap 5](https://getbootstrap.com/docs/5.2/getting-started/introduction/) - Bootstrap 5 was used to desgin responsive website.
* [jQuery](https://jquery.com/) - jQuery was used to implement JavaScript.
* [Chrome Developer Tools](https://developers.google.com/web/tools/chrome-devtools) - Chrome Developer Tools was used to help fix problem areas and identify bugs.
* [Font Awesome](https://fontawesome.com/) - The icons for cookie logo, social media and buttons were taken from Font Awesome.
* [Google Fonts](https://fonts.google.com/) - The font 'Raleway' was imported from Google Fonts.
* [Balsamiq](https://balsamiq.com/) - Balsamiq was used to make Desktop and Mobile Wireframes.
* [Am I Responsive?](http://ami.responsivedesign.is/#) - Website used to create mockup image for this README file.

# Testing
* The testing section is in a separate file, [here](TESTING.md).

# Deployment
## Forking
1. Sign in to Github and go to my [repository](https://github.com/KlaudiaMatysiak/plushies)
2. Select the Fork button at the top right of the page.
3. The fork is now in your repositories.

## Local Deployment

* In order to make a local copy of this project, you can clone it. In your IDE Terminal, type the following command to clone my repository:

    - `git clone https://github.com/KlaudiaMatysiak/plushies.git`

    Alternatively, if using Gitpod, you can click below to create your own workspace using this repository.

    [![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io/#https://github.com/KlaudiaMatysiak/plushies)

* Create Python Environment Variables
    * Django secret key
    * To test checkout payments create stripe account
        * Stripe public key
        * Stripe secret key
* Install the Python dependencies from requirements.txt
    ```bash
    pip3 freeze --local > requirements.txt
    ```
* Create Procfile
    ```bash
    echo web: python app.py > Procfile
    ```
* Make migrations to prepare database.
    ```bash
    python3 manage.py makemigrations --dry-run
    python3 manage.py migrate --plan
    ```
* Create super user
    ```bash
    python3 manage.py createsuperuser
    ```
* Run the site locally
    ```bash
    python3 manage.py runserver
    ```

## Deployment on Heroku
### Pre set up
* Project running on gitpod
* [Heroku account](https://signup.heroku.com/)
* [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli#install-the-heroku-cli)
* [AWS account](https://aws.amazon.com/)
* [Stripe account](https://stripe.com/en-gb) for payments
* [Gmail account](https://www.google.com/intl/en-GB/gmail/about/) for email SMTP
### On Heroku
* On the website create new app
* On the heroku website, in the deploy folder connect your github account, find repositorium and enable automatic deployment
* On the heroku website set enviroment variables:
    * AWS_ACCESS_KEY_ID #AWS S3
    * AWS_SECRET_ACCESS_KEY # AWS S3
    * DATABASE_URL # postgresql database from heroku
    * EMAIL_HOST_PASS # gmail smtp
    * EMAIL_HOST_USER # gmail smtp
    * SECRET_KEY  # the Django secret key
    * STRIPE_PUBLIC_KEY # stripe
    * STRIPE_SECRET_KEY # stripe
    * STRIPE_WH_SECRET # stripe
    * USE_AWS: True

# Credits
## Images and descriptions
| Link to the image | Image and/or Description |
|:---:|:---:|
|[Click here](https://www.pngmart.com/image/203020)| Hero Plushie |
|[Click here](https://www.google.com/search?q=image+placeholder+plushie&tbm=isch&ved=2ahUKEwij_Mnr8Jf7AhULrycCHQDkBJ8Q2-cCegQIABAA&oq=image+placeholder+plushie&gs_lcp=CgNpbWcQAzoECCMQJzoECAAQQzoFCAAQgAQ6BggAEAUQHjoGCAAQCBAeUJsGWPwOYMkQaABwAHgAgAFFiAH4A5IBATmYAQCgAQGqAQtnd3Mtd2l6LWltZ8ABAQ&sclient=img&ei=wMdmY6OcBIvensEPgMiT-Ak&bih=961&biw=1920&rlz=1C1ONGR_en-GBGB992GB992#imgrc=noVQp1JLBjCbWM)| Image Placeholder |
|[Click here](https://www.etsy.com/uk/listing/627921279/kawaii-plush-waffle-plush-food-plushies)| Waffle Plushie |
|[Click here](https://www.amazon.co.uk/Living-Nature-Highland-Soft-Sound/dp/B00OLN1KSI/ref=asc_df_B00OLN1KSI/?tag=googshopuk-21&linkCode=df0&hvadid=310869151196&hvpos=&hvnetw=g&hvrand=2146499008631646336&hvpone=&hvptwo=&hvqmt=&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=1007416&hvtargid=pla-403233033491&psc=1)| Highland Cow Plushie |
|[Click here](https://www.plushieland.co.uk/products/fries-fast-food-plushie-oversize-plush-toy?variant=42531862184148) [Click here](https://www.1001hobbies.co.uk/plushes/439144-kidrobot-kidtcymp338-yummy-world-fernando-the-fries-2-0-large-plush-883975159306.html) | Fries Plushie |
|[Click here](https://www.bigbountyshop.com/products/pizza-slice-plushie-oversize-food-plush-toy-plushieland?currency=GBP&utm_medium=cpc&utm_source=google&utm_campaign=Google%20Shopping)| Pizza Slice Plushie |
|[Click here](https://www.bigbountyshop.com/collections/plushies/products/black-cat-plush-toy-black-cat-pillow-soft-plush-doll-cat-plushie-cat-pillow-stuffed-animal-soft-plush-pillow-baby-plush-toys-cat-shape-design-sofa-pillow-decoration-doll)| Cat Plushie |
|[Click here](https://www.smythstoys.com/uk/en-gb/brand/pok%c3%a9mon/pokemon-toys/bulbasaur-20cm-pok%c3%a9mon-plush/p/171511022)| Pokémon Bulbasaur Plushie |
|[Click here](https://www.campusgifts.co.uk/product/jellycat-vivacious-vegetable-broccoli?gclid=CjwKCAiAvK2bBhB8EiwAZUbP1KmhML4afi62a4kMRWsZDHpYx_UNc5zFWvr4pzeDPE2pJzX8cirkXxoCrNkQAvD_BwE)| Broccoli Plushie |
|[Click here](https://www.campusgifts.co.uk/product/jellycat-amuseable-avocado-small?gclid=CjwKCAiAvK2bBhB8EiwAZUbP1OJYbLI2OhSoV1fn48A6Gt9AzDz5cSkTdwIXOB5PCLuhyx6ngpeDlhoCLpAQAvD_BwE)| Avocado Plushie |


|[Click here](https://www.google.com/shopping/product/9910092399480056401?q=Plushies+food&rlz=1C1ONGR_en-GBGB992GB992&sxsrf=ALiCzsbGEVhtYhLhH0DyXw-FAHCRh3iz_A:1668031777914&biw=1920&bih=961&dpr=1&prds=eto:10209888280867773364_0,pid:1792594186089744155&sa=X&ved=0ahUKEwie3qXbjqL7AhWWEMAKHUuzCGgQ8gIIoAooAA)| Ice Cream Plushie |
|[Click here](https://www.bigbountyshop.com/collections/plushies/products/giant-spider-plushie-animal-plush-toy)| Spider Plushie |
|[Click here](https://www.amazon.co.uk/Zappi-Co-Collectible-Turtle-Cuddly/dp/B07PJSH4MG/ref=sr_1_31?keywords=Plush%2BAnimals&qid=1668032197&sr=8-31&th=1)| Turtle Plushie |
|[Click here](https://www.amazon.co.uk/Sanei-Crossing-Tanukichi-Horizons-Atsumare/dp/B08CXYF6BH/ref=sr_1_42?keywords=Plush+Animals&qid=1668032197&sr=8-42)| Animal Crossing New Horizon Tom Nook Plushie |
|[Click here](https://www.argos.co.uk/product/3361973?istCompanyId=a74d8886-5df9-4baa-b776-166b3bf9111c&istFeedId=30f62ea9-9626-4cac-97c8-9ff3921f8558&istItemId=rxatxlqli&istBid=t&&cmpid=GS001&_$ja=tsid:59157%7cacid:629-618-1342%7ccid:16634989433%7cagid:133162502845%7ctid:pla-870087826733%7ccrid:588879114441%7cnw:u%7crnd:16820350002314530517%7cdvc:c%7cadp:%7cmt:%7cloc:1007452&utm_source=Google&utm_medium=cpc&utm_campaign=16634989433&utm_term=3361973&utm_content=shopping&utm_custom1=133162502845&utm_custom2=629-618-1342&GPDP=true&gclid=CjwKCAiAvK2bBhB8EiwAZUbP1MufeLcyf-IwO9cbAyJOM6Ly44FirdUJxeu8pScpAitt7B-9DvgUohoCb2wQAvD_BwE&gclsrc=aw.ds)| Lobster Plushie |
|[Click here](https://www.carousell.sg/p/snorlax-plush-toy-50cm-1122374686/)| Pokémon Snorlax Plushie |
|[Click here](https://www.game.co.uk/en/pok-mon-18-inch-sleeping-plush-jigglypuff-2885161)| Pokémon Jigglypuff Plushie |
|[Click here](https://battlegroundgaming.co.uk/collections/plush/products/pokemon-8-inch-plush-happy-pikachu)| Pokémon Pikachu Plushie |
|[Click here](https://www.sportsdirect.com/pokemon-pok%C3%A9mon-8-inch-vulpix-plush-900797#colcode=90079790)| Pokémon Vulpix Plushie |
|[Click here](https://www.campusgifts.co.uk/jellycat-amuseable-popcorn-a6pc?gclid=CjwKCAiAvK2bBhB8EiwAZUbP1C3L-_Ph_JnlzJYxorAsPvZLLNsT9xNr5BGyYriI44ukqBvP68yKJBoCW2sQAvD_BwE)| Popcorn Plushie |
|[Click here](https://www.boutiquesdemusees.fr/en/plushs/clementine-plush-9-x-12-cm-jellycat/34280.html?gclid=CjwKCAiAvK2bBhB8EiwAZUbP1NVjTit0xNpsRN4XN52CyuoRsfEdM4OFeQx0cRjkpF2Ol9xRr3cUuRoCnygQAvD_BwE)| Clementine Plushie |
|[Click here](https://www.campusgifts.co.uk/product/jellycat-vivacious-vegetable-onion?gclid=CjwKCAiAvK2bBhB8EiwAZUbP1LMRmw17QQqEpTDpWUoUZJOsAlbWYgdOt6B3ndEyTPnFul_T74DNfxoCHxoQAvD_BwE)| Onion Plushie |
|[Click here](https://www.campusgifts.co.uk/jellycat-fabulous-fruit-peach-fabf6peach?gclid=CjwKCAiAvK2bBhB8EiwAZUbP1OTR9PVKBgUCDrwkAHVxO1ALP-pcwVinVrTM8P8Lfy9iD9-fya2nMBoCnMUQAvD_BwE)| Peach Plushie |
|[Click here](https://www.campusgifts.co.uk/jellycat-vivacious-vegetable-tomato-jellycat?gclid=CjwKCAiAvK2bBhB8EiwAZUbP1Mu0vg2JAYctGFDX3qsEsa10NhHPEs6e_E8hClTEqN9Z-3IGSYa1HxoCvGgQAvD_BwE)| Vine Tomatoes Plushie |
|[Click here](https://www.highworthemporium.co.uk/p/jellycat-soft-toys-vivacious-vegetable-mushroom)| Mushroom Plushie |


