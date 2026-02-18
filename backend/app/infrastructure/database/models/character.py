"""Character model - jugadores por usuario."""

from sqlalchemy import Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from app.infrastructure.database.base import Base
from app.infrastructure.database.models.utils import _utc_now

# Stats iniciales fijos para todos (MVP)
DEFAULT_HP = 100
DEFAULT_ATK = 10
DEFAULT_DEF = 5
DEFAULT_SPD = 10
DEFAULT_CRIT = 5
DEFAULT_EVA = 5
DEFAULT_LIVES = 5


class Character(Base):
    """Personaje del jugador - stats, posición, recursos."""

    __tablename__ = "characters"

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False, index=True)
    name = Column(String(50), nullable=False)

    # Progresión
    level = Column(Integer, default=1, nullable=False)
    experience = Column(Integer, default=0, nullable=False)

    # Stats
    hp = Column(Integer, default=DEFAULT_HP, nullable=False)
    max_hp = Column(Integer, default=DEFAULT_HP, nullable=False)
    atk = Column(Integer, default=DEFAULT_ATK, nullable=False)
    def_ = Column("def", Integer, default=DEFAULT_DEF, nullable=False)
    spd = Column(Integer, default=DEFAULT_SPD, nullable=False)
    crit = Column(Integer, default=DEFAULT_CRIT, nullable=False)
    eva = Column(Integer, default=DEFAULT_EVA, nullable=False)

    # Vidas (PvP)
    lives = Column(Integer, default=DEFAULT_LIVES, nullable=False)
    max_lives = Column(Integer, default=DEFAULT_LIVES, nullable=False)
    last_life_regen = Column(DateTime, nullable=True)

    # Recursos
    coins = Column(Integer, default=0, nullable=False)
    gems = Column(Integer, default=0, nullable=False)

    # Posición actual (online)
    position_x = Column(Integer, default=0, nullable=True)
    position_y = Column(Integer, default=0, nullable=True)
    current_map_instance_id = Column(Integer, nullable=True, index=True)  # FK agregado en migración 002

    created_at = Column(DateTime, default=_utc_now)

    user = relationship("User", back_populates="characters")
    map_instances = relationship("MapInstance", back_populates="character", foreign_keys="MapInstance.character_id")
    gear = relationship("CharacterGear", back_populates="character")
    battles = relationship("Battle", back_populates="character")
