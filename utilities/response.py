from fastapi import Response


class JSONResponse(Response):
    def __init__(self, content: dict, status_code=200, **kwargs):
        super().__init__(
            content=content, status_code=200, media_type="application/json", **kwargs
        )
