"""Map instance - sesión activa de jugador en mapa (tiempo real)."""

from sqlalchemy import Column, DateTime, ForeignKey, Integer
from sqlalchemy.orm import relationship

from app.infrastructure.database.base import Base
from app.infrastructure.database.models.utils import _utc_now


class MapInstance(Base):
    """Instancia de mapa - dungeon en curso."""

    __tablename__ = "map_instances"

    id = Column(Integer, primary_key=True, autoincrement=True)
    character_id = Column(Integer, ForeignKey("characters.id", ondelete="CASCADE"), nullable=False, index=True)
    map_id = Column(Integer, ForeignKey("maps.id", ondelete="CASCADE"), nullable=False, index=True)

    started_at = Column(DateTime, default=_utc_now)

    character = relationship("Character", back_populates="map_instances")
    map = relationship("Map", back_populates="map_instances")
    enemy_instances = relationship("EnemyInstance", back_populates="map_instance")
    battles = relationship("Battle", back_populates="map_instance")
