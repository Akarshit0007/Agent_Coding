import time

from src.state.BaseState import BaseState
from src.utils.unload_ollama_model import unload_ollama_model


def stop_agent(state: BaseState):
    """This method
    will be used to stop agent because Judge Agent Also to run as we dont want exception of memory ran out
    passing the agent name in params will be removing the agent """
    print("Stopping Agent ")
    """Perform time calculating calculations here """
    time.sleep(1)
    MODEL_NAME = state["active_agent_model"]

    # Unload deepseek
    unload_ollama_model(MODEL_NAME)

    return {
        "active_agent_model": None,

    }