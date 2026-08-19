from pydantic import BaseModel, Field, model_validator


class GameModel(BaseModel):
    raw_data: dict[str, dict[str, str | int] | list[int]] = Field(...)

    @model_validator(mode='after')
    def validate_model(self) -> 'GameModel':
        return self
