"""Add adresse column to User table

Revision ID: e324801acd72
Revises: 3d841b731564
Create Date: 2024-07-02 11:26:12.338976

"""

from typing import Sequence, Union

import sqlalchemy as sa # type: ignore[attr-defined]
from alembic import op # type: ignore[attr-defined]

# revision identifiers, used by Alembic.
revision: str = "e324801acd72"
down_revision: Union[str, None] = "3d841b731564"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column("users", sa.Column("adresse", sa.String(), nullable=True))
    op.create_index(op.f("ix_users_adresse"), "users", ["adresse"], unique=False)
    op.create_index(op.f("ix_users_full_name"), "users", ["full_name"], unique=False)
    op.create_index(
        op.f("ix_users_password_hashed"), "users", ["password_hashed"], unique=False
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f("ix_users_password_hashed"), table_name="users")
    op.drop_index(op.f("ix_users_full_name"), table_name="users")
    op.drop_index(op.f("ix_users_adresse"), table_name="users")
    op.drop_column("users", "adresse")
    # ### end Alembic commands ###
