"""add unique constraint

Revision ID: 49bb5a76c589
Revises: 17615e42022c
Create Date: 2018-03-04 09:49:13.381590

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '49bb5a76c589'
down_revision = '17615e42022c'
branch_labels = None
depends_on = None


def upgrade():
    conn = op.get_bind()
    conn.execute(
        sa.sql.text(
            """
            ALTER TABLE stocks ADD CONSTRAINT stocks_label_uq UNIQUE (label);
            """
        )
    )


def downgrade():
    conn = op.get_bind()
    conn.execute(
        sa.sql.text(
            """
            ALTER TABLE stocks DROP CONSTRAINT stocks_label_uq;
            """
        )
    )
