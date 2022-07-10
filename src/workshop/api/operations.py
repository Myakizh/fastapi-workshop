import imp
import re
from fastapi import APIRouter

router = APIRouter(
    prefix='/operations',
)

@router.get('/')
def get_operations():
    return []
    