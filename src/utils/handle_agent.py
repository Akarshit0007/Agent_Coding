import logging
from src.utils.agent_starter import start_agent


def run_agent(name: str) -> dict:
    """
    Handles starting the specified agent dynamically.
    """
    result = start_agent(name)

    # Check if the starter successfully loaded
    if result["status"] == "success":
        print(f"✅ Verification Passed: The Agent ({name}) is Powering")

        my_agent = result["agent_instance"]
        return {"agent_instance": my_agent}
    else:
        # Properly raise or log the failure
        error_msg = f"Agent '{name}' Failed To Start: {result.get('message', 'Unknown error')}"
        logging.error(error_msg)
        raise Exception(error_msg)