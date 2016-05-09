"""

This file is the place to write solutions for the
skills assignment called skills-sqlalchemy. Remember to
consult the exercise directions for more complete
explanations of the assignment.

All classes from model.py are being imported for you
here, so feel free to refer to classes without the
[model.]User prefix.

"""

from model import *

init_app()

# -------------------------------------------------------------------
# Part 2: Write queries


# Get the brand with the **id** of 8.
Brand.query.get(8)

# Get all models with the **name** Corvette and the **brand_name** Chevrolet.
Model.query.filter_by(name='Corvette', brand_name='Chevrolet').all()

# Get all models that are older than 1960.
#SQL SELECT * FROM models WHERE year<1960
Model.query.filter(Model.year < 1960).all()

# Get all brands that were founded after 1920.
#SQL SELECT * FROM brands WHERE founded<1920
Brand.query.filter(Brand.founded < 10).all()

# Get all models with names that begin with "Cor".
Model.query.filter(Model.name.like('Cor%')).all()

# Get all brands that were founded in 1903 and that are not yet discontinued.
Brand.query.filter_by(founded = 1903, discontinued=None).all()

# Get all brands that are either 1) discontinued (at any time) or 2) founded before 1950.
Brand.query.filter_by().all()

# Get any model whose brand_name is not Chevrolet.
Model.query.filter(Model.brand_name!='Chevrolet').all()


# Fill in the following functions. (See directions for more info.)

def get_model_info(year):
    '''Takes in a year, and prints out each model, brand_name, and brand
    headquarters for that year using only ONE database query.'''

    #attempt 1: doesn't join to get brand headquarters
    # car_info = Model.query.filter_by(year=year).all()
    # print model_info

    #attempt 2: primarykey error
    # car_info = Model.query.options(db.joinedload('brand')).filter_by(year=year).all()

    #attempt 3: changing from Model.query to db.session.query
    car_info =  db.session.query(Model.name, Model.brand_name, Brand.headquarters).filter_by(model.year=year).joinload(Brand).all()

    print car_info

def get_brands_summary(brand_name):
    '''Prints out each brand name, and each model name for that brand
     using only ONE database query.'''

    brand_summary = Model.query(brand_name, name).filter_by(brand_name=brand_name).all()

    print brand_summary

# -------------------------------------------------------------------
# Part 2.5: Discussion Questions (Include your answers as comments.)

# 1. What is the returned value and datatype of ``Brand.query.filter_by(name='Ford')``?
#Answer - the returned value is "<flask_sqlalchemy.BaseQuery object at 0x10e15d410>" and its datatype is an object. The query is basically a question because there is no part of it actually asking for anything to be returned yet, example: if there was an all() at the end you'd get the actual answer of the query.


# 2. In your own words, what is an association table, and what *type* of relationship does an association table manage?
#Answer - an association table is basically the middle table that manages only enough to connect the other two tables in relation to it. There's generally nothing interesting happening in the association table. An example of this is having a DB for books and genres and then having an association table called bookgenre which only manages the foreign keys of the two other tables and thus links them together. Association tables typically manage a "many to many" relationship.

# -------------------------------------------------------------------
# Part 3

def search_brands_by_name(mystr):
    pass


def get_models_between(start_year, end_year):
    pass
