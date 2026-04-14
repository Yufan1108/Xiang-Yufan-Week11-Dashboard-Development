import os


def run_agent(user_query: str, response_style: str = "Standard") -> str:
    response_prefix = os.getenv("AGENT_RESPONSE_PREFIX", "Agent response:")

    if response_style == "Detailed":
        return (
            f"{response_prefix} {user_query}\n\n"
            f"Mode: {response_style}\n"
            "This is a mock detailed response from the local agent module."
        )

    if response_style == "Brief":
        return f"{response_prefix} {user_query} ({response_style})"

    return f"{response_prefix} {user_query}"
