from typing import (
    List,
    Optional,
)
from fastapi import APIRouter, Depends, Response, status

from database import get_session
from models.operations import Operation, OperationCreate, OperationKind, OperationUpdate
from services.opetations import OperationsService
from models.auth import User
from services.auth import get_curretn_user

router = APIRouter(
    prefix='/operations',
)

@router.get('/', response_model=List[Operation])
def get_operations(
    kind: Optional[OperationKind] = None,
    user: User = Depends(get_curretn_user),
    service: OperationsService = Depends()
):
    return service.get_list(user_id=user.id, kind=kind)
    
@router.post('/', response_model=Operation)
def create(
    operation_data: OperationCreate,
    user: User = Depends(get_curretn_user),
    service: OperationsService = Depends()
):
    return service.create(user_id=user.id, operation_data=operation_data)

@router.get('/{operation_id}', response_model=Operation)
def get_operation(
    operation_id: int,
    user: User = Depends(get_curretn_user),
    service: OperationsService = Depends()
):
    return service.get(user_id=user.id, operation_id=operation_id)

@router.put('/{operation_id}', response_model=Operation)
def updete_operation(
    operation_id: int,
    operation_data: OperationUpdate,
    user: User = Depends(get_curretn_user),
    service: OperationsService = Depends()
):
    return service.update(
        user_id=user.id, 
        operation_id=operation_id,
        operation_data=operation_data
    )

@router.delete('/{operation_id}')
def delete_operation(
    operation_id: int,
    user: User = Depends(get_curretn_user),
    service: OperationsService = Depends()
):
    service.delete(user_id=user.id, operation_id=operation_id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)