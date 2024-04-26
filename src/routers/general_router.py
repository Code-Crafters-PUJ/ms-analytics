from fastapi import APIRouter

router = APIRouter()


router.get("/")(lambda: {"message": "Hello, World!"})
