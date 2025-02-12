"""users table

Revision ID: e25c66f8f8c6
Revises: 
Create Date: 2019-12-11 23:46:00.236123

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'e25c66f8f8c6'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=64), nullable=True),
    sa.Column('email', sa.String(length=120), nullable=True),
    sa.Column('password_hash', sa.String(length=128), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_user_email'), 'user', ['email'], unique=True)
    op.create_index(op.f('ix_user_username'), 'user', ['username'], unique=True)
    op.drop_table('cycle')
    op.drop_table('order')
    op.drop_table('customer')
    op.drop_table('price_list')
    op.drop_table('photographer')
    op.drop_table('item')
    op.drop_table('photos')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('photos',
    sa.Column('id', mysql.BIGINT(display_width=20, unsigned=True), autoincrement=True, nullable=False),
    sa.Column('photographer_id', mysql.BIGINT(display_width=20, unsigned=True), autoincrement=False, nullable=False),
    sa.Column('photo_link', mysql.VARCHAR(collation='utf8_unicode_ci', length=50), nullable=False),
    sa.Column('photo_type', mysql.VARCHAR(collation='utf8_unicode_ci', length=50), nullable=False),
    sa.Column('category', mysql.VARCHAR(collation='utf8_unicode_ci', length=50), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    mysql_collate='utf8_unicode_ci',
    mysql_default_charset='utf8',
    mysql_engine='InnoDB'
    )
    op.create_table('item',
    sa.Column('id', mysql.INTEGER(display_width=11), autoincrement=False, nullable=False),
    sa.Column('name', mysql.VARCHAR(length=255), nullable=False),
    sa.Column('price', mysql.DECIMAL(precision=5, scale=2), server_default=sa.text("'0.00'"), nullable=True),
    sa.Column('created_at', mysql.DATETIME(), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=True),
    sa.Column('updated_at', mysql.DATETIME(), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=True),
    mysql_default_charset='latin1',
    mysql_engine='InnoDB'
    )
    op.create_table('photographer',
    sa.Column('id', mysql.BIGINT(display_width=20, unsigned=True), autoincrement=True, nullable=False),
    sa.Column('username', mysql.VARCHAR(collation='utf8_unicode_ci', length=50), nullable=False),
    sa.Column('userpic', mysql.VARCHAR(collation='utf8_unicode_ci', length=50), nullable=False),
    sa.Column('email', mysql.VARCHAR(collation='utf8_unicode_ci', length=50), nullable=False),
    sa.Column('phone', mysql.VARCHAR(collation='utf8_unicode_ci', length=50), nullable=False),
    sa.Column('city', mysql.VARCHAR(collation='utf8_unicode_ci', length=50), nullable=False),
    sa.Column('information', mysql.VARCHAR(collation='utf8_unicode_ci', length=300), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    mysql_collate='utf8_unicode_ci',
    mysql_default_charset='utf8',
    mysql_engine='InnoDB'
    )
    op.create_table('price_list',
    sa.Column('id', mysql.BIGINT(display_width=20, unsigned=True), autoincrement=True, nullable=False),
    sa.Column('photographer_id', mysql.BIGINT(display_width=20, unsigned=True), autoincrement=False, nullable=False),
    sa.Column('duration', mysql.VARCHAR(collation='utf8_unicode_ci', length=50), nullable=False),
    sa.Column('place', mysql.VARCHAR(collation='utf8_unicode_ci', length=50), nullable=False),
    sa.Column('category', mysql.VARCHAR(collation='utf8_unicode_ci', length=50), nullable=False),
    sa.Column('price', mysql.INTEGER(display_width=10, unsigned=True), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id'),
    mysql_collate='utf8_unicode_ci',
    mysql_default_charset='utf8',
    mysql_engine='InnoDB'
    )
    op.create_table('customer',
    sa.Column('id', mysql.BIGINT(display_width=20, unsigned=True), autoincrement=True, nullable=False),
    sa.Column('username', mysql.VARCHAR(collation='utf8_unicode_ci', length=50), nullable=False),
    sa.Column('userpic', mysql.VARCHAR(collation='utf8_unicode_ci', length=50), nullable=True),
    sa.Column('email', mysql.VARCHAR(collation='utf8_unicode_ci', length=50), nullable=False),
    sa.Column('phone', mysql.VARCHAR(collation='utf8_unicode_ci', length=50), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    mysql_collate='utf8_unicode_ci',
    mysql_default_charset='utf8',
    mysql_engine='InnoDB'
    )
    op.create_table('order',
    sa.Column('id', mysql.BIGINT(display_width=20, unsigned=True), autoincrement=True, nullable=False),
    sa.Column('customer_id', mysql.BIGINT(display_width=20), autoincrement=False, nullable=False),
    sa.Column('photographer_id', mysql.BIGINT(display_width=20), autoincrement=False, nullable=False),
    sa.Column('place', mysql.VARCHAR(collation='utf8_unicode_ci', length=50), nullable=False),
    sa.Column('date_begin', sa.DATE(), nullable=False),
    sa.Column('comment', mysql.VARCHAR(collation='utf8_unicode_ci', length=300), nullable=True),
    sa.Column('state', mysql.VARCHAR(collation='utf8_unicode_ci', length=20), server_default=sa.text("'In progress'"), nullable=True),
    sa.Column('date_end', sa.DATE(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    mysql_collate='utf8_unicode_ci',
    mysql_default_charset='utf8',
    mysql_engine='InnoDB'
    )
    op.create_table('cycle',
    sa.Column('id', mysql.BIGINT(display_width=20), autoincrement=True, nullable=False),
    sa.Column('sth', mysql.CHAR(length=50), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    mysql_default_charset='latin1',
    mysql_engine='InnoDB'
    )
    op.drop_index(op.f('ix_user_username'), table_name='user')
    op.drop_index(op.f('ix_user_email'), table_name='user')
    op.drop_table('user')
    # ### end Alembic commands ###
