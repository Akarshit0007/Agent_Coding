from utils.agent_starter import start_agent
import sys
from pathlib import Path

# Automatically finds the 'src' folder and adds it to Python's path
src_path = Path(__file__).resolve().parent / "src"
sys.path.append(str(src_path))

# Now you can import normally
from utils.agent_starter import start_agent

print("--- Testing Agent Starter Logic ---")

# Try starting the mock agent
result = start_agent("test_agent")

# Check if the starter successfully decoded/loaded it
if result["status"] == "success":
    print("✅ Verification Passed: The dynamic import logic works perfectly!")

    # Test using the mock agent instance
    my_agent = result["agent_instance"]
    response = my_agent["invoke"]("Hello from the test machine!")
    print(f"Agent Output: {response}")
else:
    print("❌ Verification Failed. Check your folder structure.")