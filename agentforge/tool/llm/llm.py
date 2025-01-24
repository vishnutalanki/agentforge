from agentforge.tool.Tool import Tool

class LLM(Tool):
    """Base class for Language Model tools."""

    def __init__(self, tool_id: str, model: str):
        """
        Initialize the LLM tool with a unique identifier and model name.

        Args:
            tool_id (str): Unique identifier for the tool.
            model (str): Name of the language model.
        """
        super().__init__(tool_id)
        self.model = model

    def __repr__(self):
        return f"LLM(id={self.tool_id}, model={self.model})"

    def execute(self, input_data: any) -> any:
        """
        Abstract method to be implemented by subclasses.
        This method will define how the LLM processes input data.

        Args:
            input_data (any): Input data for the LLM.

        Returns:
            any: Processed output from the LLM.
        """
        raise NotImplementedError("Subclasses must implement the execute method.")
