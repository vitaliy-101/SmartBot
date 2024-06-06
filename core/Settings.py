from environs import Env
from dataclasses import dataclass


@dataclass
class Bots:
    bot_token: str
    admin_id: int
    donation_provider_token: str

@dataclass
class Settings:
    bots: Bots


def getSettings(path: str):
    env = Env()
    env.read_env(path)
    return Settings(
        bots=Bots(
            bot_token=env.str("TOKEN"),
            admin_id=env.int("ADMIN_ID"),
            donation_provider_token=env.str("DONATION_PROVIDER_TOKEN")
        )
    )


settings = getSettings('input')
