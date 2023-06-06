from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from main import Car, User  

engine = create_engine('sqlite:///L:/OOP/testing_db.db', echo=True)
Session = sessionmaker(bind=engine)
session = Session()

# randam visas masinas, kurios priklauso vartotojui su id == 2
cars = session.query(Car).join(User).filter(User.id == 2).all()

for car in cars:
    print(car.brand, car.plate_nr, car.year)