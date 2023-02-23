# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker
# from dealership_db import Base, Dealership

# engine = create_engine('sqlite:///dealerships.db')
# Base.metadata.bind = engine

# DBSession = sessionmaker(bind=engine)
# session = DBSession()

# dealerships = session.query(Dealership).all()

# for dealership in dealerships:
#     print(dealership.name, dealership.address, dealership.latitude, dealership.longitude)
