from fastapi import FastAPI
from app.routes import (
    auth, users, blood_groups, donations, requests, inventory
)
from app.database import *

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Blood Bank Management System")

app.include_router(auth.router)
app.include_router(users.router)
app.include_router(blood_groups.router)
app.include_router(donations.router)
app.include_router(requests.router)
app.include_router(inventory.router)
