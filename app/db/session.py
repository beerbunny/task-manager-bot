from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine

from app.core.config import settings


engine = create_async_engine(settings.database_url, echo=False)

async_session_maker = async_sessionmaker(
    bind=engine,
    expire_on_commit=False,
)