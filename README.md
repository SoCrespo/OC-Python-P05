# Open Food Fact project

This program uses the OpenFoodFacts public database to help to choose a healthier substitute for breakfast spreads available in France, based on french index "Nutriscore" (ranks from A to E).

## Prerequisites

### Database

1. MySQL must be installed on the user's computer.

2. A database named 'openfoodfacts2020p5' must exist on localhost.

3. User 'offuser' must be granted all privileges on this database.

If this database or user already exist on the computer, please modify the database and/or user name in config.py to avoid any data deletion.

### Python

Python 3.8 is required. It can be downloaded here : <https://www.python.org/downloads/>

Install required extensions by doing (in command line) : `python install -r requirements.txt`

## How it works

### Functionalities

On first run, this app downloads from the OpenFoodFacts data about product from certain categories of breakfast spreads. These categories are specified, and can be modified, in config.py file.

Main menu offers 4 options:  

1) Find a substitute for a product. User is first asked to select a category, then a product in this category. The program then searches products from the same category and with a better nutriscore index. If it finds some, it displays the list. User can type a number to display information about the product they selected : ingredients, nutriscore, link to the Openfoodfacts.org page, stores where this product can be available. Then user is asked if they want to record this substitution to the initial product.

2) Display recorded substitutions

3) Reset the database. This can be useful if, for instance, user changed / added categories, or modified the max number of items to be downloaded from the Openfoodfact database. These parameters (categories and max number) can be changed in config.py file, see below. This reset definitely erases substitutions recorded so far.

4) Quit the program.

## Technical specifications

### OpenFoodFact data retrieving

 ***OpenFoodFactsClient*** class manages the API queries to retrieve data.

Data are then transformed in Category objects and Product objects (see below) before insertion in MySQL database.

### MySQL data storing

***CustomDBManager*** retrieves data from and inserts them into MySQL database offdb2020p5, based on the tables created by ***database_schema.sql script***.

***Category*** class affects categories data, from Mysql Database, to category object with following attributes :  
name (in ASCII, e.g. pates-a-tartiner)  
full name (ex : Pâtes à tartiner)  
id (from MySQL table).  

***Product*** class affects data for each product to a Product object with the following attributes (and their quivalent in OpenFoodFacts tables:  
category / categories  
brand / brands  
name / product_name_fr  
full_name / generic_name_fr  
quantity / quantity  
nutriscore / nutrition_grade_fr  
url / url  
ingredients / ingredients_text_fr  
stores / stores.  

### User interface

***MainMenu*** class manages main menu ;-)

***Menu*** class manages selection menus using ListOfChoice objects and constants.py file.

***ListOfChoice*** class creates objects with a title and a content (list of any item). The Menu class uses ListOfChoice to display easily a list of products with a title.

### Main program

Instanciantes a Main object. Main.start() launches and manages the main program.
