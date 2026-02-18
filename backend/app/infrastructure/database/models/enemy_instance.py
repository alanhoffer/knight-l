"""Enemy instance - mob en mapa (tiempo real)."""

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from app.infrastructure.database.base import Base


class EnemyInstance(Base):
    """Instancia de enemigo en map_instance - mob vivo en el mapa."""

    __tablename__ = "enemy_instances"

    id = Column(Integer, primary_key=True, autoincrement=True)
    map_instance_id = Column(Integer, ForeignKey("map_instances.id", ondelete="CASCADE"), nullable=False, index=True)
    enemy_id = Column(Integer, ForeignKey("enemies.id", ondelete="CASCADE"), nullable=False, index=True)

    position_x = Column(Integer, nullable=False)
    position_y = Column(Integer, nullable=False)
    current_hp = Column(Integer, nullable=False)
    state = Column(String(20), default="alive", nullable=False)  # alive | dead

    map_instance = relationship("MapInstance", back_populates="enemy_instances")
    enemy = relationship("Enemy", back_populates="instances")
