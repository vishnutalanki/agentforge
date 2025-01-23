from abc import ABC, abstractmethod

class Agent(ABC):
    """Abstract base class for an AI agent."""

    def __init__(self, agent_id: str):
        """
        Initialize an agent with a unique identifier.

        Args:
            agent_id (str): Unique identifier for the agent.
        """
        self.agent_id = agent_id

    @abstractmethod
    def execute(self):
        """
        Abstract method to define the behavior or action of the agent.
        Must be implemented by subclasses.
        """
        pass

    def __repr__(self):
        return f"Agent(id={self.agent_id})"
