---
title: AI Customer Support RL Env
emoji: 🤖
colorFrom: blue
colorTo: green
sdk: docker
app_file: app.py
pinned: false
---

# AI Customer Support RL Environment

## Overview

This project implements a structured reinforcement learning environment simulating real world customer support workflows. An AI agent must diagnose and resolve user issues through multi-step interactions.

## Key Features

* Dynamic issue generation across difficulty levels
* Multiple valid solution paths per issue
* Graded reward system (0.0 – 1.0)
* Efficiency based scoring (faster resolution rewarded)
* Real world scenario: AI customer support decision making

## Project Structure

models.py → typed models (Observation, Action)
tasks.py → task and issue definitions
grader.py → reward evaluation logic
env.py → environment implementation (step/reset/state)
test.py → local testing script
inference.py → baseline inference script (required)
app.py → API for deployment (FastAPI)
openenv.yaml → OpenEnv configuration
Dockerfile → container setup

## Environment API

* `reset(difficulty)` → initializes a new task
* `step(action)` → returns (next_state, reward, done, info)
* `state()` → returns structured observation

## Task Levels

* Easy
* Medium
* Hard

## Example Actions

ask_issue
suggest_restart
suggest_cleanup
suggest_reconnect
confirm_fix

## Reward System

* Correct action → 1.0
* Partially correct → 0.5
* Incorrect → 0.0
* Efficiency bonus/penalty applied on completion

## Running Locally

```bash
python3 test.py