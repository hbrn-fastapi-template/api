from fastapi import APIRouter, Depends, HTTPException
from fastapi.params import Form
from sqlmodel import Session
from funcs.db import get_session
from classes.models import TemplateSubscription, TemplateSubscriptionRead, TemplateSubscriptionCreate
from utils import get, save

router = APIRouter(prefix='/subscription', tags=["Subscription"])

@router.get("/", response_model=list[TemplateSubscriptionRead])
def get_subscriptions(session: Session = Depends(get_session)):
    # IMPLEMENT CUSTOM LOGIC HERE
    return get(session, TemplateSubscription)


@router.post("/", response_model=list[TemplateSubscriptionRead])
def create_subscription(session: Session = Depends(get_session), subscription: TemplateSubscriptionCreate):
    # IMPLEMENT CUSTOM LOGIC HERE

    # INPUT FORMAT:
    # subscription = TemplateSubscription(
    #     name="Free",
    #     price=0,
    # )
    return save(session, subscription)