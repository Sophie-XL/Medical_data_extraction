# Create an API call using FastAPI to connect with the frontend and test using postman
from fastapi import FastAPI, Form, UploadFile, File
import uvicorn
from extractor import extract
import uuid
import os

app = FastAPI()

# use postman to upload file
@app.post("/extract_from_doc")
def extract_from_doc(
        file_format: str = Form(...),
        file: UploadFile = File(...),

):
    contents = file.file.read()
    # create a unique file for each uploaded file
    file_path = "uploads/" + str(uuid.uuid4())+".pdf"
    with open(file_path,"wb") as f:
        f.write(contents)
# Exception Handling
    try:
        data = extract(file_path, file_format)
    except Exception as e:
        data ={
            'error': str(e)
        }


# Delete file after information extracted
    if os.path.exists(file_path):
        os.remove(file_path)

    return data

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)