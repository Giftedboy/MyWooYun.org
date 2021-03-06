"""empty message

Revision ID: dd1ed2388f10
Revises: 
Create Date: 2020-07-23 13:29:18.580127

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'dd1ed2388f10'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('bugs', 'replys',
               existing_type=mysql.LONGTEXT(),
               nullable=False,
               comment=None,
               existing_comment='漏洞评论')
    op.alter_column('bugs', 'wybug_author',
               existing_type=mysql.VARCHAR(length=50),
               nullable=False,
               comment=None,
               existing_comment='漏洞作者')
    op.alter_column('bugs', 'wybug_date',
               existing_type=mysql.VARCHAR(length=50),
               nullable=False,
               comment=None,
               existing_comment='漏洞提交时间')
    op.alter_column('bugs', 'wybug_detail',
               existing_type=mysql.LONGTEXT(),
               nullable=False,
               comment=None,
               existing_comment='漏洞详情')
    op.alter_column('bugs', 'wybug_id',
               existing_type=mysql.VARCHAR(length=50),
               nullable=False,
               comment=None,
               existing_comment='漏洞编号')
    op.alter_column('bugs', 'wybug_level',
               existing_type=mysql.VARCHAR(length=20),
               nullable=False,
               comment=None,
               existing_comment='危害等级')
    op.alter_column('bugs', 'wybug_reply',
               existing_type=mysql.LONGTEXT(),
               nullable=False,
               comment=None,
               existing_comment='漏洞回应')
    op.alter_column('bugs', 'wybug_title',
               existing_type=mysql.VARCHAR(length=150),
               nullable=False,
               comment=None,
               existing_comment='漏洞标题')
    op.alter_column('bugs', 'wybug_type',
               existing_type=mysql.VARCHAR(length=50),
               nullable=False,
               comment=None,
               existing_comment='漏洞类型')
    op.drop_index('bugs_wybug_id', table_name='bugs')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_index('bugs_wybug_id', 'bugs', ['wybug_id'], unique=False)
    op.alter_column('bugs', 'wybug_type',
               existing_type=mysql.VARCHAR(length=50),
               nullable=True,
               comment='漏洞类型')
    op.alter_column('bugs', 'wybug_title',
               existing_type=mysql.VARCHAR(length=150),
               nullable=True,
               comment='漏洞标题')
    op.alter_column('bugs', 'wybug_reply',
               existing_type=mysql.LONGTEXT(),
               nullable=True,
               comment='漏洞回应')
    op.alter_column('bugs', 'wybug_level',
               existing_type=mysql.VARCHAR(length=20),
               nullable=True,
               comment='危害等级')
    op.alter_column('bugs', 'wybug_id',
               existing_type=mysql.VARCHAR(length=50),
               nullable=True,
               comment='漏洞编号')
    op.alter_column('bugs', 'wybug_detail',
               existing_type=mysql.LONGTEXT(),
               nullable=True,
               comment='漏洞详情')
    op.alter_column('bugs', 'wybug_date',
               existing_type=mysql.VARCHAR(length=50),
               nullable=True,
               comment='漏洞提交时间')
    op.alter_column('bugs', 'wybug_author',
               existing_type=mysql.VARCHAR(length=50),
               nullable=True,
               comment='漏洞作者')
    op.alter_column('bugs', 'replys',
               existing_type=mysql.LONGTEXT(),
               nullable=True,
               comment='漏洞评论')
    # ### end Alembic commands ###
