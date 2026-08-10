import asyncio
from app.WebHandler import app


async def main():
    app.listen(8080)
    await asyncio.Event().wait()

if __name__ == "__main__":
    asyncio.run(main())