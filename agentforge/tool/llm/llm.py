from agentforge.tool.Tool import Tool

class llm(Tool):
    """Base class for Language Model tools."""

    def __init__(self, tool_id: str, model: str):
        """
        Initialize the llm tool with a unique identifier and model name.

        Args:
            tool_id (str): Unique identifier for the tool.
            model (str): Name of the language model.
        """
        super().__init__(tool_id)
        self.model = model

    def __repr__(self):
        return f"llm(id={self.tool_id}, model={self.model})"

    def execute(self, input_data: any) -> any:
        """
        Abstract method to be implemented by subclasses.
        This method will define how the llm processes input data.

        Args:
            input_data (any): Input data for the llm.

        Returns:
            any: Processed output from the llm.
        """
        raise NotImplementedError("Subclasses must implement the execute method.")
