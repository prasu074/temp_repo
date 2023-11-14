import json
import logging
import os

from fastapi import APIRouter
from scripts.config import Service
from scripts.core.constants.api import DefaultAPI
from scripts.core.schemas.response_models import DefaultResponse
from starlette.responses import FileResponse

router = APIRouter(prefix=DefaultAPI.api_widget)


@router.get(DefaultAPI.load_styles)
async def load_styles():
    """
    Default: Loads required endpoints to get filenames in the build
    Do not edit this
    """
    try:
        js_files = [f"{Service.PROXY}/widget/load_file?filename={file}" for file
                    in
                    os.listdir(Service.BUILD_DIR)
                    if os.path.isfile(os.path.join(Service.BUILD_DIR, file)) and file.endswith(".js")]
        return DefaultResponse(message="Styles loaded successfully", data=js_files)
    except Exception as e:
        logging.exception(e)
        return DefaultResponse(message="Failed to load file paths", status="failed")


@router.get(DefaultAPI.api_load_file)
def download_resource(filename: str):
    """Default: Request Build Files to redner widget configurations on the frontend
    Do not edit this
    """
    try:
        file_path = os.path.join(Service.BUILD_DIR, filename)
        if os.path.isfile(os.path.join(Service.BUILD_DIR, filename)) and filename.endswith(".js"):
            return FileResponse(file_path, media_type='application/octet-stream', filename=filename)
        else:
            return DefaultResponse(message="Failed to load resources")
    except Exception as e:
        logging.error("Exception " + str(e))
        return DefaultResponse(message="File not found")


@router.get(DefaultAPI.api_load_configuration)
async def load_configuration():
    """
    Default: Load widget configuration JSON for listing plugins while creating widgets
    Do not edit this
    """
    try:
        with open(f"{Service.BUILD_DIR}/widgetConfig.json", "r") as file:
            file_content = json.loads(file.read())
        return file_content
    except Exception as e:
        logging.error(e)
        return DefaultResponse(message="Failed to load configurations")


# TODO: Add preview logic. Do not change the API endpoint

@router.get(DefaultAPI.api_preview)
async def preview(request_type: str = "refresh"):
    """
    Request Type Options
    Preview: Can take in all widget configuration from payload and return Chart Preview Response
    Refresh: Will accept widget ID and derive the widget configuration from Widget collection, to then return the
    chart response
    """
    try:
        if request_type not in ["refresh", "preview"]:
            return DefaultResponse(message="Invalid Query Parameter")
        # Route to Handler for Processing Chart json
        return {}
    except Exception as e:
        logging.error(e)
        return DefaultResponse(message="Not found")
