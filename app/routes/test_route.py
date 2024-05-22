from fastapi.responses import JSONResponse
from fastapi import APIRouter, Depends

router = APIRouter(prefix="/test", tags=["Test"])

@router.get("/", summary="")
def testIndex():
    # should through a division by zero exception
    content = {"value": 1/0}
    return JSONResponse(status_code=200, content=content)


@router.get("/key-error", summary="")
def testIndex():
    # should through a division by zero exception
    a = {}
    content = {"value": a["b"]}
    return JSONResponse(status_code=200, content=content)

