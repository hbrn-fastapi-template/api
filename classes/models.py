from typing import List, Optional
from sqlmodel import SQLModel, Field, Relationship
from datetime import datetime

# -------------------- TEMPLATE USER --------------------

class TemplateUser(SQLModel, table=True):
    """
    user table
    """

    __tablename__ = "template_user"

    id_user: int = Field(default=None, primary_key=True)
    subscription_id: Optional[int] = Field(default=None)
    name: str
    created_at: Optional[datetime] = Field(default=None)

    subscription: Optional["TemplateSubscription"] = Relationship(back_populates="users")

# -------- SUBMODELS --------
class TemplateUserBase(SQLModel):
    name: str
    subscription_id: Optional[int] = None

class TemplateUserRead(TemplateUserBase):
    id_user: int

class TemplateUserCreate(TemplateUserBase):
    pass

class TemplateUserUpdate(TemplateUserBase):
    pass

# ---------------------------------------------------------------
# -------------------- TEMPLATE SUBSCRIPTION --------------------

class TemplateSubscription(SQLModel, table=True):
    """
    subscription table
    """

    __tablename__ = "template_subscription"

    id_subscription: int = Field(default=None, primary_key=True)
    name: str
    price: float
    created_at: Optional[datetime] = Field(default=None)

    users: List["TemplateUser"] = Relationship(back_populates="subscription")

# -------- SUBMODELS --------
class TemplateSubscriptionBase(SQLModel):
    name: str
    price: float

class TemplateSubscriptionRead(TemplateSubscriptionBase):
    id_subscription: int

class TemplateSubscriptionCreate(TemplateSubscriptionBase):
    created_at: Optional[datetime] = None

class TemplateSubscriptionUpdate(TemplateSubscriptionBase):
    pass

# ---------------------------------------------------------------


for _cls in [
    # models
    TemplateUser, TemplateSubscription,
    
    # submodels for CRUD routers
    TemplateUserCreate, TemplateUserRead, TemplateUserUpdate,
    TemplateSubscriptionCreate, TemplateSubscriptionRead, TemplateSubscriptionUpdate,
]:
    try:
        _cls.model_rebuild()
    except Exception:
        # model_rebuild might not exist in older SQLModel/Pydantic versions; ignore if absent.
        pass