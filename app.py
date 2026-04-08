from fastapi import FastAPI
from env import SupportEnv
from models import Observation

app = FastAPI()
env = SupportEnv()

@app.get("/")
def home():
    return {"message": "SupportEnv running"}

@app.post("/reset")
def reset(difficulty: str = "easy"):
    obs = env.reset(difficulty)
    # obs is an Observation object from models.py
    return {
        "observation": {
            "issue": obs.issue,
            "current_step": obs.current_step,
            "steps_taken": obs.steps_taken
        }
    }

@app.post("/step")
def step(action: str = "ask_issue"):
    next_state, reward, done, _ = env.step(action)
    obs = env.state()
    return {
        "observation": {
            "issue": obs.issue,
            "current_step": obs.current_step,
            "steps_taken": obs.steps_taken
        },
        "reward": reward,
        "terminated": done,
        "truncated": False,
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