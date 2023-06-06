from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, sessionmaker

engine = create_engine('sqlite:///L:/OOP/testing_db.db', echo=True)
Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)
    car = relationship('Car', back_populates='user')

class Car(Base):
    __tablename__ = 'car'

    id = Column(Integer, primary_key=True)
    brand = Column(String)
    plate_nr = Column(String) 
    user_id = Column(Integer, ForeignKey('users.id'))
    year = Column(String)
    user = relationship('User', back_populates='car')

Base.metadata.create_all(engine)

user1 = User(name='John Smith', email='blabla@gmail.com')
user2 = User(name='Tomas Vaitkus', email='tomas.vaitkus@gmail.com')
user3 = User(name='Vygandas Vaitkus', email='vygandas.vaitkus@gmail.com')
user4 = User(name='Juozapas Kazkoks', email='juozapas.kazkas@gmail.com')

car1 = Car(brand='Opel Zafira', plate_nr='LAA489',user_id=1, year='1985')
car2 = Car(brand='Opel Astra', plate_nr='LAA489',user_id=1, year='1985')
car3 = Car(brand='Opel Sigma', plate_nr='LAA500',user_id=1, year='1985')
car4 = Car(brand='Ford Escort', plate_nr='LAS800',user_id=1, year='1985')
car5 = Car(brand='Mercedes Benz', plate_nr='LAA889',user_id=1, year='1985')
car6 = Car(brand='Ford Siera', plate_nr='ppp800',user_id=2, year='1985')
car7 = Car(brand='BMW', plate_nr='qqq998',user_id=2, year='1985')
car8 = Car(brand='Fiat', plate_nr='wwq963',user_id=2, year='1985')
car9 = Car(brand='Fiat 500', plate_nr='LAA489',user_id=2, year='1985')

# sukraunam objektus i sesija ir uzcommitinam
session.add_all([user1, user2, user3, user4, car1, car2, car3, car4, car5, car6, car7, car8, car9])
session.commit()

print('done')