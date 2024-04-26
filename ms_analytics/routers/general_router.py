from fastapi import APIRouter

from ..controllers import get_general_info

router = APIRouter()


router.get("/info")(get_general_info)
