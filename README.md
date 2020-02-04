# Open Food Fact project

This program uses the OpenFoodFacts public database to help to choose a healthier substitute for breakfast spreads.

## Prerequisites

### Database

1. MySQL must be installed on the user's computer.
WARNING : this program will handle a database named 'openfoodfacts2020p5' and a user named 'offuser' who will have all privileges on it. If they already exist on the computer, please modify the dtabase and/or user name in parameters.py to avoid any data deletion.

2. A database named 'openfoodfacts2020p5' has to exist on localhost.

3. User 'offuser' must be granted all privileges on this database. 

### Python

See requirements.txt.


## How it works

### Tables creation

***LocalDBManager*** class creates the required tables and foreign keys.

### Database filling 

 ***OpenFoodFactsClient*** class uses the get_products_by_category() method gets the products using the OpenFoodFacts API for a given category and for a given number of products (default value is 10, this setting can be changed in params.py).

***DataTrimmer*** cleans retrieved data and suppress multiple entries (as the weight of the product is not considered)

***Product*** converts data for each product in a Product with the following fields :
categories
generic_name_fr
product_name_fr
brands 
url
stores
nutrition_grade_fr
ingredient_text_fr

***LocalDBManager*** class, as the name suggests, has the following methods:
- insert_in_database() 
- reset_database()

***Menu*** Manages the main menu.

### Main program





