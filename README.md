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

### Local database

***LocalDBManager*** class manages the MySQL tables : connection, tables creation, data insertion.


### OpenFoodFact data retrieving

 ***OpenFoodFactsClient***  get_products_by_categories() method gets the products using the OpenFoodFacts API for a given category and for a given number of products (default value is 10, this setting can be changed in params.py).

 ***data_to_product*** converts the list of dictionaries in list of Product objects.

***Product*** class affects data for each product in a Product object with the following attributes (and their quivalent in OpenFoodFacts tables):
category / categories
brand / brands
name / product_name_fr
full_name / generic_name_fr
quantity / quantity
nutriscore / nutrition_grade_fr
url / url
ingredients / ingredients_text_fr
stores / stores


***Menu*** Manages the main menu.

### Main program





