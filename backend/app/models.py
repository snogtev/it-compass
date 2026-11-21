import asyncio
import enum
from decimal import Decimal

from sqlalchemy import (
    CheckConstraint,
    ForeignKey,
    Identity,
    Numeric,
    Text,
    UniqueConstraint,
)
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

DATABASE_URL = 'postgresql+asyncpg://user:password@localhost:5432/database'


class Direction(str, enum.Enum):
    forward = 'forward'
    backward = 'backward'

class Base(DeclarativeBase):
    pass

# ============================================================================
# Справочные сущности
# ============================================================================

class Region(Base):
    __tablename__ = 'regions'

    id: Mapped[int] = mapped_column(Identity(), primary_key=True)
    name: Mapped[str] = mapped_column(Text, unique=True)
    slug: Mapped[str] = mapped_column(Text, unique=True)
    population: Mapped[int] = mapped_column()

class Metric(Base):
    __tablename__ = 'metrics'

    id: Mapped[int] = mapped_column(Identity(), primary_key=True)
    name: Mapped[str] = mapped_column(Text, unique=True)
    is_graded: Mapped[bool]
    direction: Mapped[Direction] = mapped_column()


class Grade(Base):
    __tablename__ = 'grades'

    id: Mapped[int] = mapped_column(Identity(), primary_key=True)
    name: Mapped[str] = mapped_column(Text, unique=True)
    slug: Mapped[str] = mapped_column(Text, unique=True)

# ============================================================================
# Операционные сущности
# ============================================================================


class RawMetricRecord(Base):
    __tablename__ = 'raw_metric_records'

    id: Mapped[int] = mapped_column(Identity(), primary_key=True)
    raw_region_name: Mapped[str] = mapped_column(Text)
    raw_metric_name: Mapped[str] = mapped_column(Text)
    raw_grade_name: Mapped[str | None] = mapped_column(Text)
    raw_value: Mapped[str | None] = mapped_column(Text)

class NormalizedMetricRecord(Base):
    __tablename__ = 'normalized_metric_records'

    id: Mapped[int] = mapped_column(Identity(), primary_key=True)
    region_id: Mapped[int] = mapped_column(ForeignKey('regions.id'))
    metric_id: Mapped[int] = mapped_column(ForeignKey('metrics.id'))
    grade_id: Mapped[int | None] = mapped_column(ForeignKey('grades.id'))
    value: Mapped[Decimal] = mapped_column(Numeric(10, 1))
    normalized_score: Mapped[Decimal] = mapped_column(Numeric(4, 1))

    __table_args__ = (
        CheckConstraint(
            'normalized_score >= 0.0 AND normalized_score <= 100.0',
            name='ck_normalized_score_range',
        ),
        UniqueConstraint(
            'region_id',
            'metric_id',
            'grade_id',
            postgresql_nulls_not_distinct=True,
        ),
    )

class RegionRating(Base):
    __tablename__ = 'region_ratings'

    id: Mapped[int] = mapped_column(Identity(), primary_key=True)
    region_id: Mapped[int] = mapped_column(ForeignKey('regions.id'))
    grade_id: Mapped[int] = mapped_column(ForeignKey('grades.id'))
    total_score: Mapped[int]

    __table_args__ = (
        CheckConstraint(
            'total_score >= 1 AND total_score <= 100',
            name='ck_total_score_range',
        ),
        UniqueConstraint(
            'region_id',
            'grade_id',
            name='uq_rating_region_grade',
        ),
    )

# ============================================================================
# Конфигурационные сущности
# ============================================================================

class Weight(Base):
    __tablename__ = 'weights'

    id: Mapped[int] = mapped_column(Identity(), primary_key=True)
    grade_id: Mapped[int] = mapped_column(ForeignKey('grades.id'))
    metric_id: Mapped[int] = mapped_column(ForeignKey('metrics.id'))
    weight: Mapped[Decimal] = mapped_column(Numeric(3, 2))

    __table_args__ = (
        CheckConstraint(
            'weight >= 0.00 AND weight <= 1.00',
            name='ck_weight_range',
        ),
        UniqueConstraint(
            'grade_id',
            'metric_id',
            name='uq_weight_grade_metric',
        ),
    )

async def main():
    engine = create_async_engine(DATABASE_URL, echo=False)
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    await engine.dispose()
    print('Успех')

if __name__ == '__main__':
    asyncio.run(main())