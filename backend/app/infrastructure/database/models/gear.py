"""Gear models - catálogo e inventario."""

from sqlalchemy import Column, Boolean, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from app.infrastructure.database.base import Base

# Tipos y rarezas
GEAR_TYPE_WEAPON = "weapon"
GEAR_TYPE_ARMOR = "armor"
RARITY_COMMON = "common"
RARITY_UNCOMMON = "uncommon"
RARITY_RARE = "rare"
RARITY_EPIC = "epic"
RARITY_LEGENDARY = "legendary"


class GearTemplate(Base):
    """Catálogo de ítems base (armas, armaduras)."""

    __tablename__ = "gear_templates"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    type = Column(String(20), nullable=False)  # weapon | armor

    # Stats base (bonus por defecto)
    atk_bonus = Column(Integer, default=0, nullable=False)
    def_bonus = Column(Integer, default=0, nullable=False)
    spd_bonus = Column(Integer, default=0, nullable=False)
    crit_bonus = Column(Integer, default=0, nullable=False)
    eva_bonus = Column(Integer, default=0, nullable=False)

    # Pasiva genérica (JSON): {"type": "stun", "chance": 0.1, ...}
    passive_effect = Column(String(500), nullable=True)  # JSON string para SQLite

    character_gear = relationship("CharacterGear", back_populates="gear_template")
    loot_entries = relationship("LootTableEntry", back_populates="gear_template")


class CharacterGear(Base):
    """Instancia de ítem en inventario - nivel y rareza propios."""

    __tablename__ = "character_gear"

    id = Column(Integer, primary_key=True, autoincrement=True)
    character_id = Column(Integer, ForeignKey("characters.id", ondelete="CASCADE"), nullable=False, index=True)
    gear_template_id = Column(Integer, ForeignKey("gear_templates.id", ondelete="CASCADE"), nullable=False, index=True)

    # Instancia única
    level = Column(Integer, default=1, nullable=False)
    rarity = Column(String(20), nullable=False)

    # Stats finales de esta instancia
    atk_bonus = Column(Integer, default=0, nullable=False)
    def_bonus = Column(Integer, default=0, nullable=False)
    spd_bonus = Column(Integer, default=0, nullable=False)
    crit_bonus = Column(Integer, default=0, nullable=False)
    eva_bonus = Column(Integer, default=0, nullable=False)

    is_equipped = Column(Boolean, default=False, nullable=False)
    slot = Column(String(20), nullable=True)  # weapon | armor | null
    quantity = Column(Integer, default=1, nullable=False)

    character = relationship("Character", back_populates="gear")
    gear_template = relationship("GearTemplate", back_populates="character_gear")
    battle_loot = relationship("BattleLoot", back_populates="character_gear", uselist=False)
