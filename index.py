from fastapi import FastAPI
from routes.sim_data import sim_card
app = FastAPI()
app.include_router(sim_card)