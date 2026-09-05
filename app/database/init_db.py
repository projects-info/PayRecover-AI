from app.database.connection import engine
from app.models.base import Base

# Import all models
from app.models.merchant import Merchant
from app.models.customer import Customer
from app.models.payment import Payment

Base.metadata.create_all(bind=engine)

print("Database created successfully!")