from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Boolean, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from sqlalchemy_utils import create_database
from sqlalchemy import create_engine


from sqlalchemy.orm import relationship




engine = create_engine('postgresql://chef:yesyesye@localhost/chefaidb')
# create_database(engine.url)

# Create a connection to the database
conn = engine.connect()



Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    user_id = Column(Integer, primary_key=True)
    email = Column(String)
    password = Column(String)
    date_created = Column(DateTime)
    last_active_time = Column(DateTime)
    language_preference = Column(String)
    diet_preference = Column(String)
    allergies = Column(String)
    recipes = relationship('Recipe', secondary='user_recipes')

class Recipe(Base):
    __tablename__ = 'recipes'
    recipe_id = Column(Integer, primary_key=True)
    name = Column(String)
    diet = Column(String)
    ingredients = Column(String)
    instructions = Column(String)
    times_favorited = Column(Integer)

class UserRecipe(Base):
    __tablename__ = 'user_recipes'
    user_id = Column(Integer, ForeignKey('users.user_id'), primary_key=True)
    recipe_id = Column(Integer, ForeignKey('recipes.recipe_id'), primary_key=True)

class Subscription(Base):
    __tablename__ = 'subscriptions'
    subscription_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.user_id'))
    start_date = Column(DateTime)
    end_date = Column(DateTime)
    is_lifetime = Column(Boolean)

Base.metadata.create_all(engine)

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()
