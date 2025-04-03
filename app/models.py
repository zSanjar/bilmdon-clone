from sqlalchemy.orm import mapped_column , Mapped, relationship

from app.database import Base

from datetime import datetime, date, timezone

class User(Base):
    __tabelname__ = "user"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[int] = mapped_column(unique=True)
    hashed_password: Mapped[str] = mapped_column(String(128))
    username: Mapped[str] = mapped_column(String(32), unique=True)
    first_name: Mapped[str] = mapped_column(String(32))
    last_name: Mapped[str] = mapped_column(String(32))
    birthdate = Mapped[date] =  mapped_column(DateTime, default=datetime.now(timezone.utc))
    is_active: Mapped[bool] = mapped_column(default=True)
    is_staff: Mapped[bool] = mapped_column(default=False)
    is_superuser: Mapped[bool] = mapped_column(default=False)


    