from fastapi import FastAPI
from exceptions import (
    PinCodeNotFound,
    InvalidPinCodeError,
    pin_code_not_found_handler,
    invalid_pin_code_handler,
)
from models import LocationResponse, BulkResponse, BulkRequest
from pincode_data import pincode_db

app = FastAPI(
    title="Pincode Lookup API",
    description="A simple API to lookup indian pincode details",
)

# Register your custom exception handler
app.add_exception_handler(PinCodeNotFound, pin_code_not_found_handler)
app.add_exception_handler(InvalidPinCodeError, invalid_pin_code_handler)


@app.get("/")
def root():
    return {"message": "Welcome to Pincode Lookup API!"}


@app.get("/pincode/{code}", response_model=LocationResponse)
def lookup_pinncode(code: str):
    if len(code) != 6 or not code.isdigit():
        raise InvalidPinCodeError(code, "Must be exactly 6 digit")

    if code not in pincode_db:
        raise PinCodeNotFound(code)
    return pincode_db[code]


@app.post("/pincode/bulk", response_model=BulkResponse)
def bulk_lookup(req: BulkRequest):
    results = []
    missing = []

    for code in req.pincodes:
        if code in pincode_db:
            results.append(pincode_db[code])

        else:
            missing.append(code)

    return BulkResponse(
        found=len(results), not_found=len(missing), results=results, missing=missing
    )
