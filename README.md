# Custom FastAPI Template

This is a custom FastAPI template that uses SQLModel for data models, and provides a set of tools to make it easier to create and manage your API.

## Endpoints

### User
- GET `/user`
- GET `/user/{id}`
- POST `/user`
- PUT `/user`
- DELETE `/user`

### Subscription
- GET `/subscription`
- POST `/subscription`


## Models

### User
- `id_user`: int
- `subscription_id`: Optional[int] = None
- `name`: str
- `created_at`: Optional[datetime] = None

### Subscription
- `id_subscription`: int
- `name`: str
- `price`: float
- `created_at`: Optional[datetime] = None


## ORM Cascade Save

```python
user = TemplateUser(
    name="John Doe",
    subscription=TemplateSubscription(
        name="Free",
        price=0
    )
)
save(session, user)
```