"""Enemy and loot models."""

from sqlalchemy import Column, Float, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from app.infrastructure.database.base import Base


class LootTable(Base):
    """Tabla de loot - agrupa ítems que pueden dropear."""

    __tablename__ = "loot_tables"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)

    entries = relationship("LootTableEntry", back_populates="loot_table")
    enemies = relationship("Enemy", back_populates="loot_table")


class LootTableEntry(Base):
    """Entrada en tabla de loot - ítem + probabilidad."""

    __tablename__ = "loot_table_entries"

    id = Column(Integer, primary_key=True, autoincrement=True)
    loot_table_id = Column(Integer, ForeignKey("loot_tables.id", ondelete="CASCADE"), nullable=False, index=True)
    gear_template_id = Column(Integer, ForeignKey("gear_templates.id", ondelete="CASCADE"), nullable=False, index=True)

    drop_chance = Column(Float, nullable=False)  # 0.0 - 1.0
    min_quantity = Column(Integer, default=1, nullable=False)
    max_quantity = Column(Integer, default=1, nullable=False)

    loot_table = relationship("LootTable", back_populates="entries")
    gear_template = relationship("GearTemplate", back_populates="loot_entries")


class Enemy(Base):
    """Template de enemigo por mapa."""

    __tablename__ = "enemies"

    id = Column(Integer, primary_key=True, autoincrement=True)
    map_id = Column(Integer, ForeignKey("maps.id", ondelete="CASCADE"), nullable=False, index=True)
    name = Column(String(100), nullable=False)
    level = Column(Integer, nullable=False)

    hp = Column(Integer, nullable=False)
    atk = Column(Integer, nullable=False)
    def_ = Column("def", Integer, nullable=False)
    spd = Column(Integer, nullable=False)
    crit = Column(Integer, default=0, nullable=False)
    eva = Column(Integer, default=0, nullable=False)

    loot_table_id = Column(Integer, ForeignKey("loot_tables.id", ondelete="SET NULL"), nullable=True, index=True)

    map = relationship("Map", back_populates="enemies")
    loot_table = relationship("LootTable", back_populates="enemies")
    instances = relationship("EnemyInstance", back_populates="enemy")
