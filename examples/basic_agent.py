from agentforge.agent.Agent import Agent


# Define a subclass of Agent
class SimpleAgent(Agent):
    def execute(self):
        """
        Implementation of the abstract execute method.
        """
        print(f"SimpleAgent with id {self.agent_id} is executing a task.")

# Instantiate the SimpleAgent
if __name__ == "__main__":
    agent = SimpleAgent(agent_id="simple_001")
    agent.execute()

    # Print the agent's representation
    print(agent)
