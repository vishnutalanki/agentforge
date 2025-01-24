from agentforge.tool.Tool import Tool

# Define a subclass of Tool
class BasicTool(Tool):
    def execute(self, input_data: str) -> str:
        """
        Implementation of the abstract execute method.
        This tool simply echoes the input data.

        Args:
            input_data (str): Input data for the tool to process.

        Returns:
            str: Echoed input data.
        """
        return f"BasicTool processed: {input_data}"

# Instantiate the BasicTool
if __name__ == "__main__":
    tool = BasicTool(tool_id="basic_tool_001")
    result = tool.execute("Hello, Tool!")

    # Print the result
    print(result)

    # Print the tool's representation
    print(tool)
