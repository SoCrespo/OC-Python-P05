# Open Food Fact project

This program uses the OpenFoodFacts public database to help to choose a healthier substitute for breakfast spreads.

## Prerequisites

### Database

1. MySQL must be installed on the user's computer.
WARNING : this program will handle a database named 'openfoodfacts2020p5' and a user named 'offuser' who will have all privileges on it. If they already exist on the computer, please modify the dtabase and/or user name in parameters.py to avoid any data deletion.

2. A database named 'openfoodfacts2020p5' has to exist on localhost.

3. User 'offuser' must be granted all privileges on this database.

### Python

Install required extensions by doing (in command line) : `python install -r requirements.txt`

## How it works

### Local database

***CustomDBManager*** class manages the MySQL tables : connection, tables creation, data insertion and retrieving.  
***database_schema.sql*** is the MySQL script used to create or reset database.

### OpenFoodFact data retrieving

 ***OpenFoodFactsClient*** class manages the API queries.

 **get_products_by_categories()** method gets the products using the OpenFoodFacts API for given categories (default values CATEGORIES are in config.py), and for a given number of products (default value MAX_PRODUCTS_NB in config is 50).

Data are then transformed in Category objects and Product objects (see below) before insertion in MySQL database.

***Category*** class affects categories data, from Mysql Database, to category objectwith following attributes :
name (in ASCII, e.g. pates-a-tartiner)
full name (ex : Pâtes à tartiner)
id (from MySQL table).

***Product*** class affects data for each product to a Product object with the following attributes (and their quivalent in OpenFoodFacts tables):
category / categories
brand / brands
name / product_name_fr
full_name / generic_name_fr
quantity / quantity
nutriscore / nutrition_grade_fr
url / url
ingredients / ingredients_text_fr
stores / stores.

***Menu*** Manages the main menu and selection menus using Option object and constant.py file.

***Option*** class creates objects with a title and a content (list of any item). The Menu class uses Option to display easily a list of products with a title.

### Main program

Instanciantes a Main object. Main.start() launches and manages the main program.
