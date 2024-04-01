from fastapi import APIRouter, File, UploadFile
from typing import Optional
import os
from models.user import UserModel
from config.database import collection_name
from schema.schemas import list_serials
from bson import ObjectId

router = APIRouter()

UPLOAD_DIR= "uploads"

@router.get("/")
async def get_user():
    users = list_serials(collection_name.find())
    return users


@router.post("/")
async def post_user(user: UserModel, e_url: UploadFile = File(...)):
    #save profile picture
    
    file_path = os.path.join(UPLOAD_DIR,e_url.filename)
    with open(file_path, "wb") as f:
        f.write(e_url.file.read())
    # inserting in mangodb
    user_dict = dict(user)
    user_dict["eUrl"] = file_path
    collection_name.insert_one(dict(user))

