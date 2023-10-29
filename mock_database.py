# Mock database, all data will be pruned once the main code execution finished
from typing import Dict, List

"""
User database
[
    {
        "username": "arajdianaltaf",
        "password": "plain password string"
    }
]
"""
DATABASE: List = []

def add_user(account: Dict[str, str]) -> None:
    DATABASE.append({
        "username": account["username"],
        "password": account["password"]
    })

def get_user(username: str) -> Dict[str, str]:
    for user in DATABASE:
        if user["username"] == username:
            return user
    
    return {}
