import string
from secrets import choice

from fastapi import FastAPI



app = FastAPI()

ALPHABET: str = string.ascii_letters + string.digits

def generate_random_slug() -> str:
    slug = ""
    for _ in range(6):
        slug += choice(ALPHABET)


@app.post("/short_url")
async def generate_short_url():
    return {"data": "1"}


@app.post("/{slug}")
async def redirect_to_url(slug: str):
    return ... # redirect




