"""add characters, maps, gear, enemies, battles, snapshots

Revision ID: 002
Revises: 001
Create Date: 2024-01-01

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

revision: str = "002"
down_revision: Union[str, None] = "001"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # maps
    op.create_table(
        "maps",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("name", sa.String(100), nullable=False),
        sa.Column("level_requirement", sa.Integer(), nullable=False),
        sa.Column("description", sa.Text(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )

    # gear_templates
    op.create_table(
        "gear_templates",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("name", sa.String(100), nullable=False),
        sa.Column("type", sa.String(20), nullable=False),
        sa.Column("atk_bonus", sa.Integer(), nullable=False),
        sa.Column("def_bonus", sa.Integer(), nullable=False),
        sa.Column("spd_bonus", sa.Integer(), nullable=False),
        sa.Column("crit_bonus", sa.Integer(), nullable=False),
        sa.Column("eva_bonus", sa.Integer(), nullable=False),
        sa.Column("passive_effect", sa.String(500), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )

    # loot_tables
    op.create_table(
        "loot_tables",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("name", sa.String(100), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )

    # loot_table_entries
    op.create_table(
        "loot_table_entries",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("loot_table_id", sa.Integer(), nullable=False),
        sa.Column("gear_template_id", sa.Integer(), nullable=False),
        sa.Column("drop_chance", sa.Float(), nullable=False),
        sa.Column("min_quantity", sa.Integer(), nullable=False),
        sa.Column("max_quantity", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(["gear_template_id"], ["gear_templates.id"], ondelete="CASCADE"),
        sa.ForeignKeyConstraint(["loot_table_id"], ["loot_tables.id"], ondelete="CASCADE"),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index("ix_loot_table_entries_gear_template_id", "loot_table_entries", ["gear_template_id"])
    op.create_index("ix_loot_table_entries_loot_table_id", "loot_table_entries", ["loot_table_id"])

    # characters
    op.create_table(
        "characters",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("user_id", sa.Integer(), nullable=False),
        sa.Column("name", sa.String(50), nullable=False),
        sa.Column("level", sa.Integer(), nullable=False),
        sa.Column("experience", sa.Integer(), nullable=False),
        sa.Column("hp", sa.Integer(), nullable=False),
        sa.Column("max_hp", sa.Integer(), nullable=False),
        sa.Column("atk", sa.Integer(), nullable=False),
        sa.Column("def", sa.Integer(), nullable=False),
        sa.Column("spd", sa.Integer(), nullable=False),
        sa.Column("crit", sa.Integer(), nullable=False),
        sa.Column("eva", sa.Integer(), nullable=False),
        sa.Column("lives", sa.Integer(), nullable=False),
        sa.Column("max_lives", sa.Integer(), nullable=False),
        sa.Column("last_life_regen", sa.DateTime(), nullable=True),
        sa.Column("coins", sa.Integer(), nullable=False),
        sa.Column("gems", sa.Integer(), nullable=False),
        sa.Column("position_x", sa.Integer(), nullable=True),
        sa.Column("position_y", sa.Integer(), nullable=True),
        sa.Column("current_map_instance_id", sa.Integer(), nullable=True),
        sa.Column("created_at", sa.DateTime(), nullable=True),
        sa.ForeignKeyConstraint(["user_id"], ["users.id"], ondelete="CASCADE"),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index("ix_characters_user_id", "characters", ["user_id"])

    # enemies (needs maps, loot_tables)
    op.create_table(
        "enemies",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("map_id", sa.Integer(), nullable=False),
        sa.Column("name", sa.String(100), nullable=False),
        sa.Column("level", sa.Integer(), nullable=False),
        sa.Column("hp", sa.Integer(), nullable=False),
        sa.Column("atk", sa.Integer(), nullable=False),
        sa.Column("def", sa.Integer(), nullable=False),
        sa.Column("spd", sa.Integer(), nullable=False),
        sa.Column("crit", sa.Integer(), nullable=False),
        sa.Column("eva", sa.Integer(), nullable=False),
        sa.Column("loot_table_id", sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(["loot_table_id"], ["loot_tables.id"], ondelete="SET NULL"),
        sa.ForeignKeyConstraint(["map_id"], ["maps.id"], ondelete="CASCADE"),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index("ix_enemies_map_id", "enemies", ["map_id"])
    op.create_index("ix_enemies_loot_table_id", "enemies", ["loot_table_id"])

    # map_instances
    op.create_table(
        "map_instances",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("character_id", sa.Integer(), nullable=False),
        sa.Column("map_id", sa.Integer(), nullable=False),
        sa.Column("started_at", sa.DateTime(), nullable=True),
        sa.ForeignKeyConstraint(["character_id"], ["characters.id"], ondelete="CASCADE"),
        sa.ForeignKeyConstraint(["map_id"], ["maps.id"], ondelete="CASCADE"),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index("ix_map_instances_character_id", "map_instances", ["character_id"])
    op.create_index("ix_map_instances_map_id", "map_instances", ["map_id"])

    # Note: characters.current_map_instance_id referencia map_instances (sin FK por compatibilidad SQLite)

    # enemy_instances
    op.create_table(
        "enemy_instances",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("map_instance_id", sa.Integer(), nullable=False),
        sa.Column("enemy_id", sa.Integer(), nullable=False),
        sa.Column("position_x", sa.Integer(), nullable=False),
        sa.Column("position_y", sa.Integer(), nullable=False),
        sa.Column("current_hp", sa.Integer(), nullable=False),
        sa.Column("state", sa.String(20), nullable=False),
        sa.ForeignKeyConstraint(["enemy_id"], ["enemies.id"], ondelete="CASCADE"),
        sa.ForeignKeyConstraint(["map_instance_id"], ["map_instances.id"], ondelete="CASCADE"),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index("ix_enemy_instances_map_instance_id", "enemy_instances", ["map_instance_id"])
    op.create_index("ix_enemy_instances_enemy_id", "enemy_instances", ["enemy_id"])

    # character_gear
    op.create_table(
        "character_gear",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("character_id", sa.Integer(), nullable=False),
        sa.Column("gear_template_id", sa.Integer(), nullable=False),
        sa.Column("level", sa.Integer(), nullable=False),
        sa.Column("rarity", sa.String(20), nullable=False),
        sa.Column("atk_bonus", sa.Integer(), nullable=False),
        sa.Column("def_bonus", sa.Integer(), nullable=False),
        sa.Column("spd_bonus", sa.Integer(), nullable=False),
        sa.Column("crit_bonus", sa.Integer(), nullable=False),
        sa.Column("eva_bonus", sa.Integer(), nullable=False),
        sa.Column("is_equipped", sa.Boolean(), nullable=False),
        sa.Column("slot", sa.String(20), nullable=True),
        sa.Column("quantity", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(["character_id"], ["characters.id"], ondelete="CASCADE"),
        sa.ForeignKeyConstraint(["gear_template_id"], ["gear_templates.id"], ondelete="CASCADE"),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index("ix_character_gear_character_id", "character_gear", ["character_id"])
    op.create_index("ix_character_gear_gear_template_id", "character_gear", ["gear_template_id"])

    # battles
    op.create_table(
        "battles",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("character_id", sa.Integer(), nullable=False),
        sa.Column("map_instance_id", sa.Integer(), nullable=False),
        sa.Column("map_id", sa.Integer(), nullable=False),
        sa.Column("result", sa.String(20), nullable=False),
        sa.Column("started_at", sa.DateTime(), nullable=False),
        sa.Column("ended_at", sa.DateTime(), nullable=True),
        sa.Column("xp_gained", sa.Integer(), nullable=False),
        sa.Column("coins_gained", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(["character_id"], ["characters.id"], ondelete="CASCADE"),
        sa.ForeignKeyConstraint(["map_id"], ["maps.id"], ondelete="CASCADE"),
        sa.ForeignKeyConstraint(["map_instance_id"], ["map_instances.id"], ondelete="CASCADE"),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index("ix_battles_character_id", "battles", ["character_id"])
    op.create_index("ix_battles_map_id", "battles", ["map_id"])
    op.create_index("ix_battles_map_instance_id", "battles", ["map_instance_id"])

    # battle_loot
    op.create_table(
        "battle_loot",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("battle_id", sa.Integer(), nullable=False),
        sa.Column("character_gear_id", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(["battle_id"], ["battles.id"], ondelete="CASCADE"),
        sa.ForeignKeyConstraint(["character_gear_id"], ["character_gear.id"], ondelete="CASCADE"),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index("ix_battle_loot_battle_id", "battle_loot", ["battle_id"])
    op.create_index("ix_battle_loot_character_gear_id", "battle_loot", ["character_gear_id"])

    # battle_snapshots
    op.create_table(
        "battle_snapshots",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("battle_id", sa.Integer(), nullable=False),
        sa.Column("tick", sa.Integer(), nullable=False),
        sa.Column("snapshot_data", sa.String(2000), nullable=True),
        sa.ForeignKeyConstraint(["battle_id"], ["battles.id"], ondelete="CASCADE"),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index("ix_battle_snapshots_battle_id", "battle_snapshots", ["battle_id"])


def downgrade() -> None:
    op.drop_index("ix_battle_snapshots_battle_id", table_name="battle_snapshots")
    op.drop_table("battle_snapshots")
    op.drop_index("ix_battle_loot_character_gear_id", table_name="battle_loot")
    op.drop_index("ix_battle_loot_battle_id", table_name="battle_loot")
    op.drop_table("battle_loot")
    op.drop_index("ix_battles_map_instance_id", table_name="battles")
    op.drop_index("ix_battles_map_id", table_name="battles")
    op.drop_index("ix_battles_character_id", table_name="battles")
    op.drop_table("battles")
    op.drop_index("ix_character_gear_gear_template_id", table_name="character_gear")
    op.drop_index("ix_character_gear_character_id", table_name="character_gear")
    op.drop_table("character_gear")
    op.drop_index("ix_enemy_instances_enemy_id", table_name="enemy_instances")
    op.drop_index("ix_enemy_instances_map_instance_id", table_name="enemy_instances")
    op.drop_table("enemy_instances")
    op.drop_index("ix_map_instances_map_id", table_name="map_instances")
    op.drop_index("ix_map_instances_character_id", table_name="map_instances")
    op.drop_table("map_instances")
    op.drop_index("ix_enemies_loot_table_id", table_name="enemies")
    op.drop_index("ix_enemies_map_id", table_name="enemies")
    op.drop_table("enemies")
    op.drop_index("ix_characters_user_id", table_name="characters")
    op.drop_table("characters")
    op.drop_index("ix_loot_table_entries_loot_table_id", table_name="loot_table_entries")
    op.drop_index("ix_loot_table_entries_gear_template_id", table_name="loot_table_entries")
    op.drop_table("loot_table_entries")
    op.drop_table("loot_tables")
    op.drop_table("gear_templates")
    op.drop_table("maps")
