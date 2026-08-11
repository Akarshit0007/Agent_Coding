import importlib


def start_agent(agent_name: str) -> dict:
    """Finds and starts an agent file from the 'brain' folder."""
    try:
        # 1. Open the file inside the brain folder (e.g., brain.agent_one)
        my_agent_file = importlib.import_module(f"models.brain.{agent_name}")

        # 2. Get the agent from the file (or use the whole file if no special setup exists)
        if hasattr(my_agent_file, "agent"):
            running_agent = my_agent_file.agent
        else:
            running_agent = my_agent_file

        print(f"Agent '{agent_name}' started successfully!")
        return {"status": "success", "agent_instance": running_agent}

    except Exception as error:
        print(f"Could not start agent: {error}")
        return {"status": "error", "message": str(error)}