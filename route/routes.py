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
async def post_user(user: UserModel):
    collection_name.insert_one(dict(user))

