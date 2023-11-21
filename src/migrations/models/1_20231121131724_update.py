from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "article" ADD "description" TEXT NOT NULL;
        CREATE TABLE IF NOT EXISTS "author" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "name" VARCHAR(200) NOT NULL
);
        CREATE TABLE IF NOT EXISTS "book" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "title" VARCHAR(100) NOT NULL
);
        CREATE TABLE IF NOT EXISTS "category" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "name" VARCHAR(100) NOT NULL
);"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "article" DROP COLUMN "description";
        DROP TABLE IF EXISTS "author";
        DROP TABLE IF EXISTS "book";
        DROP TABLE IF EXISTS "category";"""
