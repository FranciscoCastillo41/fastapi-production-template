from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from app.core.config import settings

# Create engine with a connection pool
engine = create_async_engine(
    settings.database_url,
    pool_size=5, max_overflow=10,
    future=True  # SQLAlchemy 2.0 style
)
# Session factory bound to engine
AsyncSessionLocal = sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)

# Dependency function to get DB session
async def get_db():
    async with AsyncSessionLocal() as session:
        try:
            yield session
        finally:
            # Session is closed on exit (returned to pool)
            await session.close()
