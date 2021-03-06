from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.dialects.postgresql import UUID
import sqlalchemy as sa
from sqlalchemy import orm
import uuid
from .enums import GlobalRoleEnum, ProjectRoleEnum

Base = declarative_base()



class User(Base):
    __tablename__ = 'user'
    id = sa.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = sa.Column(sa.String(length=50), nullable=False)
    role = sa.Column(sa.Enum(GlobalRoleEnum), nullable=False)
    company_id = sa.Column(UUID(as_uuid=True), sa.ForeignKey('company.id'))

    company = orm.relationship("Company")

    memberships = orm.relationship("Membership", back_populates="user")


class Company(Base):
    __tablename__ = 'company'
    id = sa.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = sa.Column(sa.String(length=50), nullable=False)


class Project(Base):
    __tablename__ = 'project'
    id = sa.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = sa.Column(sa.String(length=30), nullable=False)
    company_id = sa.Column(UUID(as_uuid=True), sa.ForeignKey('company.id'))

    company = orm.relationship("Company")
    memberships = orm.relationship("Membership", back_populates="project")


class Membership(Base):
    __tablename__ = 'membership'
    # id = sa.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = sa.Column(UUID(as_uuid=True), sa.ForeignKey('user.id'), primary_key=True)
    project_id = sa.Column(UUID(as_uuid=True), sa.ForeignKey('project.id'), primary_key=True)
    role = sa.Column(sa.Enum(ProjectRoleEnum), nullable=False)

    user = orm.relationship("User", back_populates="memberships")
    project = orm.relationship("Project", back_populates="memberships")


sa.schema.Index('user_id_index', User.id, postgresql_using='hash')
sa.schema.Index('company_id_index', Company.id, postgresql_using='hash')
sa.schema.Index('project_id_index', Project.id, postgresql_using='hash')
sa.schema.Index('membership_user_id_index', Membership.user_id, postgresql_using='hash')
sa.schema.Index('membership_project_id_index', Membership.project_id, postgresql_using='hash')
