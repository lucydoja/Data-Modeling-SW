import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()
class User(Base):
    __tablename__ = "user"
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    user_name = Column(String(250), nullable=False)
    first_name = Column(String(250), nullable=False)
    last_name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)

class Planets(Base):
    __tablename__ = "planets"
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    population = Column(Integer)
    terrain = Column(String(250))
    diameter = Column(Integer)
    rotation_period = Column(Integer)
    orbital_period = Column(Integer)
    gravity = Column(String(250))
    url = Column(String(250), nullable=False)
   
class People(Base):
    __tablename__ = "people"
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    height = Column(Integer)
    mass = Column(Integer)
    hair_color = Column(String(250))
    skin_color = Column(String(250))
    eye_color = Column(String(250))
    birth_year = Column(Integer)
    url = Column(String(250), nullable=False)

class Favorites(Base):
    __tablename__ = "Favorites"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    planet_name = Column(String(250), ForeignKey('planets.name'))
    planet_id = Column(Integer, ForeignKey('planets.id'))
    people_name = Column(String(250), ForeignKey('people.name'))
    people_id = Column(Integer, ForeignKey('people.id'))


## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')