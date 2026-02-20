from pydantic import BaseModel, Field


class Source(BaseModel):
    """ "Schema for the source of the search result"""

    url: str = Field(description="The URL of the source")


class SearchResult(BaseModel):
    """Schema for the search result"""

    answer: str = Field(description="The answer to the question")
    sources: list[Source] = Field(
        description="The sources of the search result", default_factory=list
    )
