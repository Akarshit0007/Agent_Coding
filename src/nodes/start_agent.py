from src.state.BaseState import BaseState
from src.utils.handle_agent import run_agent


def start_agent(state: BaseState):
    """In this methpd agent will be started through ollama and it will be sending its identity which will be helpfull in generating result
    & this method then send the instance of agent which is activated"""
    print("Welcome !")

    result = run_agent("agent")
    agent = result["agent_instance"]
    return {
        "active_agent_instance": agent
    }