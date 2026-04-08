from env import SupportEnv

env = SupportEnv()

for difficulty in ["easy", "medium", "hard"]:
    print("\n---", difficulty, "---")

    issue = env.reset(difficulty)
    print("Issue:", issue)

    actions = ["ask_issue", "suggest_restart", "confirm_fix"]

    for action in actions:
        next_state, reward, done, _ = env.step(action)
        print(action, "| reward:", reward, "| next:", next_state)

        if done:
            print("✅ Task completed")
            break