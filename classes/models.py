from typing import List, Optional
from sqlmodel import SQLModel, Field, Relationship
from datetime import datetime

# -------------------- TEMPLATE USER --------------------

class TemplateUser(SQLModel, table=True):
    """
    user table
    """

    __tablename__ = "template_user"

    id_template: int = Field(default=None, primary_key=True)
    subscription_id: Optional[int] = Field(default=None)
    name: str
    created_at: Optional[datetime] = Field(default=None)

    subscription: Optional["TemplateSubscription"] = Relationship(back_populates="users")

# -------- SUBMODELS --------
class TemplateUserBase(SQLModel):
    name: str
    subscription_id: Optional[int] = None

class TemplateUserRead(TemplateUserBase):
    id_template: int

class TemplateUserCreate(TemplateUserBase):
    pass

class TemplateUserUpdate(TemplateUserBase):
    pass

class TemplateUserDelete(TemplateUserBase):
    id_template: int

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

class TemplateSubscriptionDelete(TemplateSubscriptionBase):
    id_subscription: int

# ---------------------------------------------------------------