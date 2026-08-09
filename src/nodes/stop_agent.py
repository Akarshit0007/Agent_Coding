from src.state.BaseState import BaseState


def stop_agent(state: BaseState):
    """This method
    will be used to stop agent because Judge Agent Also to run as we dont want exception of memory ran out
    passing the agent name in params will be removing the agent """
    print("Stopping Agent ")
    return ""