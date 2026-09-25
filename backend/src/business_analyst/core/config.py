import os
from dataclasses import dataclass

@dataclass(frozen=True)
class Settings:
    app_name: str = "Financial AI Agent"
    version: str = "0.1.0"
    @classmethod
    def from_env(cls):
        return cls(
            app_name=os.getenv(
                "APP_NAME",
                "Financial AI Agent",
        ),
        version=os.getenv(
            "APP_VERSION",
            "0.1.0"
        ),
    )