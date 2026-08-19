from pydantic import BaseModel, Field, model_validator


class GameModel(BaseModel):
    players: dict = Field(...)

    @model_validator(mode='after')
    def validate_model(self) -> 'GameModel':
        return self
