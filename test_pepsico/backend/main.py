from dataclasses import dataclass

from fastapi import FastAPI

from scripts.core.services.widget import router


@dataclass
class FastAPIConfig:
    title: str = "test_pepsico"
    version: str = "1.0.0"
    description: str = "testing pepsico"


app = FastAPI(**FastAPIConfig().__dict__)
app.include_router(router)
