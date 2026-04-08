def grade_action(action, correct_action):
    if action == correct_action:
        return 1.0
    elif action.startswith("suggest") and correct_action.startswith("suggest"):
        return 0.5
    else:
        return 0.0