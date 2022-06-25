import io
from re import template
from unicodedata import name
from fastapi import Depends, FastAPI,Body,Request,UploadFile,Form,WebSocket
from pydantic import BaseModel
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import path
import os
from fastapi.security import OAuth2PasswordBearer,OAuth2PasswordRequestForm

app = FastAPI()
list_username=list()
# templates=Jinja2Templates(directory=template)
pth=os.path.dirname(os.path.abspath(__file__))

# pth = os.walk(__file__)
templates = Jinja2Templates (directory=os.path.join(pth, "template"))

oauth_sceheme=OAuth2PasswordBearer(tokenUrl="token")

@app.post("/token")
async def token_genarate(form_data:OAuth2PasswordRequestForm=Depends()):
    print(form_data)
    return{"acess_token":form_data.username,"token_type":"bearer"}


@app.get("/username/login")
async def login_dta(token:str=Depends(oauth_sceheme)):
    print(token)
    return{
        "username":"daneil",
        "message":"message was sent"
    }
       

    

@app.get("/login/",response_class=HTMLResponse)
def write_home(request:Request):
    return templates.TemplateResponse("home.html",{"request":request})

@app.post("/loginform")
async def handle_form(username:str=Form(...),messagetext:str=Form(...)):
    print(messagetext)
@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        data = await websocket.receive_text()
        await websocket.send_text(f"Message was sent to: {data}")
        