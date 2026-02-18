"""Battle models - combates y snapshots."""

from sqlalchemy import Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from app.infrastructure.database.base import Base
from app.infrastructure.database.models.utils import _utc_now


class Battle(Base):
    """Resultado de un run de mapa (PvE)."""

    __tablename__ = "battles"

    id = Column(Integer, primary_key=True, autoincrement=True)
    character_id = Column(Integer, ForeignKey("characters.id", ondelete="CASCADE"), nullable=False, index=True)
    map_instance_id = Column(Integer, ForeignKey("map_instances.id", ondelete="CASCADE"), nullable=False, index=True)
    map_id = Column(Integer, ForeignKey("maps.id", ondelete="CASCADE"), nullable=False, index=True)

    result = Column(String(20), nullable=False)  # victory | defeat
    started_at = Column(DateTime, nullable=False)
    ended_at = Column(DateTime, default=_utc_now)

    xp_gained = Column(Integer, default=0, nullable=False)
    coins_gained = Column(Integer, default=0, nullable=False)

    character = relationship("Character", back_populates="battles")
    map_instance = relationship("MapInstance", back_populates="battles")
    map = relationship("Map")
    loot = relationship("BattleLoot", back_populates="battle")
    snapshots = relationship("BattleSnapshot", back_populates="battle")


class BattleLoot(Base):
    """Ítems dropados en una batalla."""

    __tablename__ = "battle_loot"

    id = Column(Integer, primary_key=True, autoincrement=True)
    battle_id = Column(Integer, ForeignKey("battles.id", ondelete="CASCADE"), nullable=False, index=True)
    character_gear_id = Column(Integer, ForeignKey("character_gear.id", ondelete="CASCADE"), nullable=False, index=True)

    battle = relationship("Battle", back_populates="loot")
    character_gear = relationship("CharacterGear", back_populates="battle_loot")


class BattleSnapshot(Base):
    """Estado del combate en un tick - para validación/replay."""

    __tablename__ = "battle_snapshots"

    id = Column(Integer, primary_key=True, autoincrement=True)
    battle_id = Column(Integer, ForeignKey("battles.id", ondelete="CASCADE"), nullable=False, index=True)

    tick = Column(Integer, nullable=False)
    snapshot_data = Column(String(2000), nullable=True)  # JSON: positions, hp, actions, etc.

    battle = relationship("Battle", back_populates="snapshots")
