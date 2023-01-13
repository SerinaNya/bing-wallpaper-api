from enum import Enum
from pydantic import BaseModel, FileUrl, HttpUrl, conint
from pathlib import Path
import requests
from datatypes import BingTime


class HostRegion(str, Enum):
    China = "cn"
    Global = "global"


class HPImageArchive_images(BaseModel):
    startdate: BingTime
    fullstartdate: BingTime
    enddate: BingTime
    url: str
    urlbase: str
    copyright: str
    copyrightlink: HttpUrl
    title: str
    quiz: str
    wp: bool
    hsh: str
    drk: int
    top: int
    bot: int
    hs: list
    full_url: HttpUrl | None
    full_urlbase: HttpUrl | None


class HPImageArchive_tooltips(BaseModel):
    loading: str
    previous: str
    next: str
    walle: str
    walls: str


class HPImageArchive(BaseModel):
    images: list[HPImageArchive_images]
    tooltips: HPImageArchive_tooltips

    def complete_url(cls, url_prefix: str):
        for image in cls.images:
            image.full_url = f"{url_prefix}{image.url}"
            image.full_urlbase = f"{url_prefix}{image.urlbase}"

    @staticmethod
    def get(hostregion: HostRegion, idx: conint(ge=-1, le=7) = -1, n: conint(ge=1) = 1):
        url_prefix = f"https://{hostregion}.bing.com"
        r = requests.get(
            f"{url_prefix}/HPImageArchive.aspx",
            params={"format": "js", "idx": idx, "n": n},
        )
        i = HPImageArchive.parse_obj(r.json())
        i.complete_url(url_prefix)
        return i
