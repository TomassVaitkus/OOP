from sqlalchemy.orm import sessionmaker
from main import Car, User, engine
import pandas as pd

Session = sessionmaker(bind=engine)
session = Session()

# randam visas masinas, kurios priklauso vartotojui su id == 2 ir masinos brandas == BMW
cars = session.query(Car).join(User).filter(User.id == 2, Car.brand == 'BMW').all()

# sukraunam i dictionary tam, kad galetumem deti i dataframe
car_dicts = [car.__dict__ for car in cars]


# susikraunam i df
cars_df = pd.DataFrame(car_dicts)
cars_df = cars_df[cars_df.columns[1:]].copy()


print(cars_df)
