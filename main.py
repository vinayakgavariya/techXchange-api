from fastapi import FastAPI
app = FastAPI()

@app.get("/")
def first_example():
    """
    GFG Example First FastAPI Example
    """
    return {"yayyyy": "it's my first api"}
