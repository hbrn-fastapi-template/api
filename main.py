from typing import Any
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from funcs.info import (title, description, version, contact, tags)
from routes.custom_subscription_router import custom_subscription_router
from classes.models import (
    TemplateUser, TemplateUserCreate, TemplateUserRead, TemplateUserUpdate
)
from utils import (
    DATABASE_URL, create_db_and_tables, 
    get_engine, make_crud_router, lifespan
)

# DATABASE_URL is read from the environment (falls back to sqlite:///./database.db)
engine = get_engine(echo=False)
create_db_and_tables()

app = FastAPI(
    title=title,
    description=description,
    openapi_tags=tags,
    version=version,
    contact=contact,
    lifespan=lifespan
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, specify the allowed domains
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --------------------- BASIC ROUTES ----------------------

# ---------------------  ROOT ----------------------

@app.get("/", tags=["Root"])
def root():
    return {"message": "API running"}


# --------------------- BASIC CRUD ---------------------
template_user_router = make_crud_router(TemplateUser, TemplateUserBase, TemplateUserRead, TemplateUserCreate, "/user", tags=["User"])

# --------------------- Include Routers ---------------------

# Include routers
app.include_router(template_user_router)

# Custom router is included separately due to custom logic
app.include_router(custom_subscription_router)