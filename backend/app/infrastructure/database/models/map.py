"""Map model - zonas explorables."""

from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.orm import relationship

from app.infrastructure.database.base import Base


class Map(Base):
    """Mapa explorable (dungeon, zona PvE)."""

    __tablename__ = "maps"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    level_requirement = Column(Integer, default=1, nullable=False)
    description = Column(Text, nullable=True)

    map_instances = relationship("MapInstance", back_populates="map")
    enemies = relationship("Enemy", back_populates="map")
