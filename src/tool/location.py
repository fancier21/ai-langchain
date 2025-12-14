from langchain.tools import ToolRuntime, tool

from model.context import Context


@tool("get_user_location", description="Retrieve user location based on user ID.")
def get_user_location(runtime: ToolRuntime[Context]) -> str:
    user_id = runtime.context.user_id
    return "Florida" if user_id == "1" else "SF"
