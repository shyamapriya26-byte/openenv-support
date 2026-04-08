from fastapi import FastAPI
from env import SupportEnv
from models import Observation
import os

app = FastAPI()
env = SupportEnv()  # single persistent environment

@app.get("/")
def home():
    return {"message": "SupportEnv running"}

@app.get("/reset")
def reset(difficulty: str = "easy"):
    obs = env.reset(difficulty)
    # Return observation as dict (matches OpenEnv expected format)
    return {
        "observation": {
            "issue": obs.issue,
            "current_step": obs.current_step,
            "steps_taken": obs.steps_taken
        }
    }

@app.get("/step")
def step(action: str = "ask_issue"):
    next_state, reward, done, _ = env.step(action)
    # Get current observation after step
    obs = env.state()
    return {
        "observation": {
            "issue": obs.issue,
            "current_step": obs.current_step,
            "steps_taken": obs.steps_taken
        },
        "reward": reward,
        "terminated": done,   # OpenEnv uses 'terminated'
        "truncated": False,   # not used in your env
        "info": {}
    }

@app.get("/state")
def get_state():
    obs = env.state()
    return {
        "issue": obs.issue,
        "current_step": obs.current_step,
        "steps_taken": obs.steps_taken
    }