from __future__ import annotations

from typing import List
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, UniqueConstraint

from app.core.database import Base


class RoomOrm(Base):
    __tablename__ = "rooms"
    __table_args__ = (
        UniqueConstraint("user_1_id", "user_2_id", name="unique_users_in_room"),
    )

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)

    user_1_id: Mapped[int] = mapped_column() # must be less than user_2_id
    user_2_id: Mapped[int] = mapped_column()

    name: Mapped[str] = mapped_column(String(100), nullable=False)
    description: Mapped[str] = mapped_column(String(255), default="", nullable=False)

    messages: Mapped[List["Message"]] = relationship(
        back_populates="room", cascade="all, delete-orphan"
    )
