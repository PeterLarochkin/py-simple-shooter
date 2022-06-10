from pydantic import BaseModel, Field
path_to_menu = "/".join(str(__file__).split("/")[:-1]) + "/"


class SettingsData(BaseModel):
    volume: int = Field(alias="volume")
    music: int = Field(alias="music")
    language: int = Field(alias="language")


class Settings():
    def __init__(self, path: str = path_to_menu + "menu/settings.json") -> None:
        self.path = path
        file = open(self.path, "r")
        setting_string = file.read()
        self.data = SettingsData.parse_raw(setting_string)
        file.close()

    def save(self):
        file = open(path_to_menu + "menu/settings.json", "w")
        file.write(self.data.json())
        file.close()