from src.state.BaseState import BaseState
from src.utils.handle_agent import run_agent


def start_judge(state: BaseState):
    """This Node will start the judge """
    print("Starting Judge")
    MODEL_NAME = "gemma4:12b"
    result = run_agent("agent")
    return {
        "active_agent_model": MODEL_NAME
    }