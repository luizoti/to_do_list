"""Added file_path to ImageHistory

Revision ID: cd451a977804
Revises: 
Create Date: 2024-06-25 22:41:10.685398

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = 'cd451a977804'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('period')
    op.drop_table('downloaded_pdf')
    op.drop_table('messages_sent')
    op.add_column('image_history', sa.Column('file_path', sa.String(), nullable=True))
    op.add_column('image_history', sa.Column('dia', sa.String(), nullable=True))
    op.create_unique_constraint(None, 'image_history', ['message_id'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'image_history', type_='unique')
    op.drop_column('image_history', 'dia')
    op.drop_column('image_history', 'file_path')
    op.create_table('messages_sent',
    sa.Column('id', sa.INTEGER(), server_default=sa.text("nextval('messages_sent_id_seq'::regclass)"), autoincrement=True, nullable=False),
    sa.Column('message', sa.TEXT(), autoincrement=False, nullable=False),
    sa.Column('message_hash', sa.TEXT(), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='messages_sent_pkey'),
    postgresql_ignore_search_path=False
    )
    op.create_table('downloaded_pdf',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('file_name', sa.TEXT(), autoincrement=False, nullable=False),
    sa.Column('message_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('date_time', postgresql.TIMESTAMP(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['message_id'], ['messages_sent.id'], name='downloaded_pdf_message_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='downloaded_pdf_pkey'),
    sa.UniqueConstraint('file_name', name='downloaded_pdf_file_name_key')
    )
    op.create_table('period',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('year', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('month', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('period', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='period_pkey'),
    sa.UniqueConstraint('period', name='period_period_key')
    )
    # ### end Alembic commands ###
