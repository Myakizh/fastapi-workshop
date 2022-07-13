from typing import List
from fastapi import APIRouter
from fastapi import Depends

from database import get_session
from models.operations import Operation
from services.opetations import OperationsService

router = APIRouter(
    prefix='/operations',
)

@router.get('/', response_model=List[Operation])
def get_operations(service: OperationsService = Depends()):
    return service.get_list()
    