from sqlalchemy import select

from fast_zero.models import User


def test_create_user(session):
    user = User(
        username='carlos',
        email='carlos@email.com',
        password='123',
    )

    session.add(user)
    session.commit()

    result = session.scalar(
        select(User).where(User.email == 'carlos@email.com')
    )

    assert result.username == 'carlos'
