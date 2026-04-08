TASKS = {
    "easy": ["internet not working"],
    "medium": ["slow laptop"],
    "hard": ["wifi disconnecting", "battery draining fast"]
}

ISSUES = {
    "internet not working": [
        ["ask_issue", "suggest_restart", "confirm_fix"],
        ["ask_issue", "check_cables", "confirm_fix"]
    ],
    "slow laptop": [
        ["ask_issue", "suggest_cleanup", "confirm_fix"]
    ],
    "wifi disconnecting": [
        ["ask_issue", "suggest_reconnect", "confirm_fix"]
    ],
    "battery draining fast": [
        ["ask_issue", "suggest_close_apps", "confirm_fix"]
    ]
}