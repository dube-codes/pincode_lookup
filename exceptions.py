from fastapi.responses import JSONResponse
from fastapi import Request, status


# Custom Exception handler class
class PinCodeNotFound(Exception):
    def __init__(self, pincode: str):
        self.pincode = pincode


class InvalidPinCodeError(Exception):
    def __init__(self, pincode: str, reason: str = "Invalid Format"):
        self.pincode = pincode
        self.reason = reason


# Custom Exception handler functions
async def pin_code_not_found_handler(req: Request, exc: PinCodeNotFound):
    return JSONResponse(
        status_code=status.HTTP_404_NOT_FOUND,
        content={
            "error": "pincode_not_found",
            "message": f"No location for Pin Code: {exc.pincode}",
            "pincode": exc.pincode,
        },
    )


async def invalid_pin_code_handler(req: Request, exc: InvalidPinCodeError):
    return JSONResponse(
        status_code=status.HTTP_400_BAD_REQUEST,
        content={
            "error": "invalid_pincode",
            "message": f"Pin Code: {exc.pincode} is invalid & the reason is: {exc.reason}!",
            "pincode": exc.pincode,
        },
    )
