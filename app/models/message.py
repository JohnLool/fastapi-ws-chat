from __future__ import annotations

from datetime import datetime
from typing import Optional
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, DateTime, ForeignKey, func

from app.core.database import Base


class MessageOrm(Base):
    __tablename__ = "messages"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    room_id: Mapped[int] = mapped_column(ForeignKey("rooms.id"), nullable=False)
    user_id: Mapped[Optional[int]] = mapped_column(nullable=True)
    username: Mapped[str] = mapped_column(String(50), nullable=False)

    content: Mapped[str] = mapped_column(String(1000), nullable=False)
    timestamp: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=func.now())

    room: Mapped["RoomOrm"] = relationship(back_populates="messages")
