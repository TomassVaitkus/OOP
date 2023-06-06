from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from main import Car, User  # Import your model classes

engine = create_engine('sqlite:///L:/OOP/testing_db.db', echo=True)
Session = sessionmaker(bind=engine)
session = Session()

# Find all cars with user_id = 2
cars = session.query(Car).join(User).filter(User.id == 2).all()

for car in cars:
    print(car.brand, car.plate_nr, car.year)