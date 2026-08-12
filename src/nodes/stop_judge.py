from datetime import time

from src.state.BaseState import BaseState
from src.utils.unload_ollama_model import unload_ollama_model


def stop_judge(state: BaseState):
    """This Method will stop THe judge as to leave the resources free whenever needed we start the agnet it will use less
    resources """
    print("Stopping Judge")

    time.sleep(1)
    MODEL_NAME = state["active_agent_model"]

    # Unload deepseek
    unload_ollama_model(MODEL_NAME)

    return {
        "active_agent_model": None,
    }