"""create stock table

Revision ID: 17615e42022c
Revises: 
Create Date: 2018-03-04 08:54:13.689895

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '17615e42022c'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():

    conn = op.get_bind()
    conn.execute(
        sa.sql.text(
            """
            CREATE TABLE stocks (
            id integer CONSTRAINT stocks_pkey PRIMARY KEY,
            label text NOT NULL
            );
            """
        )
    )

def downgrade():
    conn = op.get_bind()
    conn.execute(
        sa.sql.text(
            """
            DROP TABLE stocks;
            """
        )
    )
