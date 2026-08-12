import time
from src.state.Product_Cost import Product_Cost
from src.state.TimeConstraint import TimeConstraint

def calculate_cost(input_tokens: int, output_tokens: int, model_name: str):
    """
    calculate the monetary cost based on token usage to get an idea for it
    """

    model_lower = model_name.lower()

    pricing_table = {
        # Full flagship reasoning model (671B MoE)
        "deepseek-r1": (0.55, 2.19),  # $0.55 / input, $2.19 / output per 1M tokens
        "deepseek-chat": (0.14, 0.28),

        # Distilled R1 variants
        "deepseek-r1-distill-7b": (0.15, 0.15),
        "deepseek-r1-distill-8b": (0.14, 0.14),

        # Meta Llama models (including 8B and 70B)
        "llama-3.1-8b": (0.05, 0.08),
        "llama-3.3-70b": (0.59, 0.79),

        # Alibaba Qwen models
        "qwen-turbo": (0.05, 0.25),
        "qwen-plus": (0.26, 0.78),

        # Mistral AI models (including 7B / 8B / 12B classes like Ministral & Pixtral)
        "ministral-8b": (0.15, 0.15),
        "pixtral-12b": (0.15, 0.15),
        "mistral-nemo": (0.02, 0.03),
        "mistral-large-3": (0.50, 1.50),

        # Google Gemma models (including compact and mid-size variants)
        "gemma-3-4b": (0.04, 0.08),
        "gemma-3-12b": (0.06, 0.12),
        "gemma-3-27b": (0.08, 0.16),

        # OpenAI models
        "gpt-4o": (2.50, 10.00),
        "gpt-4o-mini": (0.15, 0.60)
    }

    rates = (0.50, 1.50)  # Default fallback rate per 1M tokens
    for key, rate_tuple in pricing_table.items():
        if key in model_lower:
            rates = rate_tuple
            break

    input_cost_per_1m, output_cost_per_1m = rates

    total_cost = ((input_tokens * input_cost_per_1m) + (output_tokens * output_cost_per_1m)) / 1_000_000

    return round(total_cost, 6)




def extract_ollama_metrics(answer, start_time: float, end_time: float, model_name: str = "deepseek-r1:7b"):
    """
    Extracts token usage, calculates execution duration, and runs the simulated cost calculation.
    """
    total_time_sec = end_time - start_time

    prompt_tokens = 0
    completion_tokens = 0

    try:
        metadata = getattr(answer, "response_metadata", {})
        token_usage = metadata.get("token_usage", {})

        prompt_tokens = token_usage.get("prompt_tokens", 0)
        completion_tokens = token_usage.get("completion_tokens", 0)
    except Exception:
        print("Warning: Token metadata not directly exposed; defaulting to 0.")

    p_tokens = prompt_tokens if isinstance(prompt_tokens, int) else 0
    c_tokens = completion_tokens if isinstance(completion_tokens, int) else 0

    simulated_cost = calculate_cost(p_tokens, c_tokens, model_name)

    agent_cost = Product_Cost(
        model_Name=model_name,
        input_token=[p_tokens],
        output_token=[c_tokens],
        total_cost=simulated_cost
    )

    time_constraint = TimeConstraint(
        input_time=str(start_time),
        output_time=str(end_time),
        total_time=int(total_time_sec),
        model_name=model_name
    )

    return agent_cost, time_constraint