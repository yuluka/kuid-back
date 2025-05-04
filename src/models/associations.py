from sqlalchemy import Table, Column, String, ForeignKeyConstraint, PrimaryKeyConstraint
from src.db.base import Base

t_user_achievement = Table(
    "user_achievement", Base.metadata,
    Column("user_id", String(20), primary_key=True, nullable=False),
    Column("achievement_id", String(20), primary_key=True, nullable=False),
    ForeignKeyConstraint(["achievement_id"], ["achievement.id"], name="user_achievement_achievement_id_fkey"), 
    ForeignKeyConstraint(["user_id"], ["USER.id"], name="user_achievement_user_id_fkey"),
    PrimaryKeyConstraint("user_id", "achievement_id", name="user_achievement_pkey")
)


t_user_insurance_module = Table(
    "user_insurance_module", Base.metadata,
    Column("user_id", String(20), primary_key=True, nullable=False),
    Column("insurance_module_id", String(20), primary_key=True, nullable=False),
    ForeignKeyConstraint(["insurance_module_id"], ["insurance_module.id"], name="user_insurance_module_insurance_module_id_fkey"),
    ForeignKeyConstraint(["user_id"], ["USER.id"], name="user_insurance_module_user_id_fkey"),
    PrimaryKeyConstraint("user_id", "insurance_module_id", name="user_insurance_module_pkey")
)


t_user_reward = Table(
    "user_reward", Base.metadata,
    Column("user_id", String(20), primary_key=True, nullable=False),
    Column("reward_id", String(20), primary_key=True, nullable=False),
    ForeignKeyConstraint(["reward_id"], ["reward.id"], name="user_reward_reward_id_fkey"),
    ForeignKeyConstraint(["user_id"], ["USER.id"], name="user_reward_user_id_fkey"),
    PrimaryKeyConstraint("user_id", "reward_id", name="user_reward_pkey")
)