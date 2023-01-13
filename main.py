from fastapi import FastAPI, status
from fastapi.responses import RedirectResponse
from models import HostRegion, HPImageArchive

app = FastAPI()


@app.get("/")
def get_root():
    return {"status": "200"}


@app.get("/latest", status_code=status.HTTP_307_TEMPORARY_REDIRECT)
def get_latest(region: HostRegion = HostRegion.Global):
    i = HPImageArchive.get(region)
    image_url = i.images[0].full_url
    return RedirectResponse(image_url)
