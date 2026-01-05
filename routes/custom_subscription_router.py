from fastapi import APIRouter, Depends, HTTPException
from fastapi.params import Form
from sqlmodel import Session
from funcs.db import get_session
from classes.models import TemplateSubscription, TemplateSubscriptionRead, TemplateSubscriptionCreate
from utils import get, save, db_commit

router = APIRouter(prefix='/subscription', tags=["Subscription"])

@router.get("/", response_model=list[TemplateSubscriptionRead])
def get_subscriptions(session: Session = Depends(get_session)):
    # IMPLEMENT CUSTOM LOGIC HERE
    return get(session, TemplateSubscription)


@router.post("/", response_model=list[TemplateSubscriptionRead])
@db_commit
def create_subscription(session: Session = Depends(get_session), subscription: TemplateSubscriptionCreate):
    # IMPLEMENT CUSTOM LOGIC HERE

    # INPUT FORMAT:
    # subscription = TemplateSubscription(
    #     name="Free",
    #     price=0
    #     created_at=datetime.now()
    # )
    try:
        return save(session, subscription)
    except HTTPException:
        raise
    except ValueError as e:
        raise HTTPException(status_code=fastapi.status.HTTP_422_UNPROCESSABLE_ENTITY, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=fastapi.status.HTTP_500_INTERNAL_SERVER_ERROR,detail=f"Erro ao criar documento: {str(e)}")
