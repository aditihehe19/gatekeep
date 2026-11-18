from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.core.security import hash_password
from app.modules.iam.models import User


class EmailAlreadyRegistered(Exception):
    pass


def create_user(db: Session, email: str, password: str) -> User:
    normalized = email.strip().lower()

    if db.scalar(select(User).where(User.email == normalized)):
        raise EmailAlreadyRegistered

    user = User(email=normalized, password_hash=hash_password(password))
    db.add(user)
    try:
        db.commit()
    except IntegrityError:
        db.rollback()
        raise EmailAlreadyRegistered
    db.refresh(user)
    return user