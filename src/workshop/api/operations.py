from typing import (
    List,
    Optional,
)
from fastapi import APIRouter
from fastapi import Depends

from database import get_session
from models.operations import Operation, OperationCreate, OperationKind
from services.opetations import OperationsService

router = APIRouter(
    prefix='/operations',
)

@router.get('/', response_model=List[Operation])
def get_operations(
    kind: Optional[OperationKind] = None,
    service: OperationsService = Depends()
):
    return service.get_list(kind=kind)
    
@router.post('/', response_model=Operation)
def create(
    operation_data: OperationCreate,
    service: OperationsService = Depends()
):
    return service.create(operation_data)