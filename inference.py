import os
import json
import requests
from openai import OpenAI

# Environment variables (set by evaluators)
API_BASE_URL = os.environ["API_BASE_URL"]
MODEL_NAME = os.environ["MODEL_NAME"]
HF_TOKEN = os.environ["HF_TOKEN"]

# Your Space URL
ENV_URL = "https://shyamapriya-openenv-done.hf.space"

# Task and benchmark names (customize as needed)
TASK_NAME = os.getenv("TASK_NAME", "internet_not_working")
BENCHMARK = os.getenv("BENCHMARK", "support-env")

client = OpenAI(base_url=API_BASE_URL, api_key=HF_TOKEN)

def log_start(task, env, model):
    print(f"[START] task={task} env={env} model={model}", flush=True)

def log_step(step, action, reward, done, error):
    error_val = error if error else "null"
    done_val = str(done).lower()
    print(f"[STEP] step={step} action={action} reward={reward:.2f} done={done_val} error={error_val}", flush=True)

def log_end(success, steps, score, rewards):
    rewards_str = ",".join(f"{r:.2f}" for r in rewards)
    print(f"[END] success={str(success).lower()} steps={steps} score={score:.3f} rewards={rewards_str}", flush=True)

# Run episode
log_start(TASK_NAME, BENCHMARK, MODEL_NAME)

# Reset
resp = requests.get(f"{ENV_URL}/reset", params={"difficulty": "easy"})
resp.raise_for_status()
obs = resp.json()["observation"]

done = False
step_num = 0
rewards_list = []
total_possible_reward = 10.0  # adjust based on your max possible reward per episode

while not done and step_num < 20:  # safety limit
    # Build prompt for LLM
    prompt = f"""Current issue: {obs['issue']}. Steps taken: {obs['steps_taken']}.
Possible actions: ask_issue, suggest_restart, suggest_cleanup, suggest_reconnect, confirm_fix, check_cables, suggest_close_apps.
Reply with only the action name."""
    
    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[{"role": "user", "content": prompt}],
        temperature=0.0,
        max_tokens=10,
    )
    action = response.choices[0].message.content.strip().lower()
    
    # Take step
    step_resp = requests.get(f"{ENV_URL}/step", params={"action": action})
    step_resp.raise_for_status()
    data = step_resp.json()
    
    obs = data["observation"]
    reward = data["reward"]
    terminated = data["terminated"]
    truncated = data["truncated"]
    done = terminated or truncated
    step_num += 1
    rewards_list.append(reward)
    
    log_step(step=step_num, action=action, reward=reward, done=done, error=None)

# Compute final score (normalized to [0,1])
# Adjust max possible reward based on your environment (e.g., max 1.0 per step * max steps)
max_possible_reward = 10.0  # change this to your actual max
score = min(sum(rewards_list) / max_possible_reward, 1.0)
success = done and score > 0.5  # or whatever success threshold

log_end(success=success, steps=step_num, score=score, rewards=rewards_list)