"""users table

Revision ID: 9b6995406dd8
Revises: 0fcd6bba0072
Create Date: 2019-12-12 00:11:38.353766

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '9b6995406dd8'
down_revision = '0fcd6bba0072'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('posts', sa.Column('body', sa.String(length=140), nullable=True))
    op.add_column('posts', sa.Column('timestamp', sa.DateTime(), nullable=True))
    op.add_column('posts', sa.Column('user_id', sa.Integer(), nullable=True))
    op.create_index(op.f('ix_posts_timestamp'), 'posts', ['timestamp'], unique=False)
    op.drop_index('ix_posts_email', table_name='posts')
    op.drop_index('ix_posts_username', table_name='posts')
    op.create_foreign_key(None, 'posts', 'photographer', ['user_id'], ['id'])
    op.drop_column('posts', 'email')
    op.drop_column('posts', 'password_hash')
    op.drop_column('posts', 'username')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('posts', sa.Column('username', mysql.VARCHAR(length=64), nullable=True))
    op.add_column('posts', sa.Column('password_hash', mysql.VARCHAR(length=128), nullable=True))
    op.add_column('posts', sa.Column('email', mysql.VARCHAR(length=120), nullable=True))
    op.drop_constraint(None, 'posts', type_='foreignkey')
    op.create_index('ix_posts_username', 'posts', ['username'], unique=True)
    op.create_index('ix_posts_email', 'posts', ['email'], unique=True)
    op.drop_index(op.f('ix_posts_timestamp'), table_name='posts')
    op.drop_column('posts', 'user_id')
    op.drop_column('posts', 'timestamp')
    op.drop_column('posts', 'body')
    # ### end Alembic commands ###
