from pydantic import BaseModel, Field


class ResponseFormat(BaseModel):
    """Response schema for the agent."""

    # A punny response (always required)
    punny_response: str = Field(..., description="A punny response")
    # Any interesting information about the weather if available
    weather_conditions: str | None = Field(
        None, description="Any interesting information about the weather if available"
    )
