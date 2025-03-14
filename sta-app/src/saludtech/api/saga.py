from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel
from typing import Any, Dict
from modules.sagas.coordinadores.saga_imagenes import SagaImagenes
from seedwork.infrastructure.saga_repository import SagaRepository

class SagaRequest(BaseModel):
    image_id: str
    data: Any

class SagaResponse(BaseModel):
    id: str
    result: str = None
    error: str = None
    data: Dict[str, Any] = None


router = APIRouter(tags=["saga"])

@router.post("/saga", response_model=SagaResponse)
async def start_saga(request: SagaRequest):
    """
    Endpoint para iniciar la ejecución de la saga.
    Se espera un JSON con la información necesaria.
    """
    saga = SagaImagenes()
    result = await saga.execute(request.dict())
    if "error" in result:
        raise HTTPException(status_code=400, detail=result)
    return result

@router.get("/saga/{saga_id}")
async def get_saga_status(saga_id: str):
    """
    Endpoint para consultar el estado de la saga mediante su identificador.
    """
    repo = SagaRepository()
    record = await repo.get_saga_by_id(saga_id)
    if record:
        return record
    raise HTTPException(status_code=404, detail="Saga no encontrada")


@router.get("/saga_all")
async def get_saga_status():
    """
    Endpoint para obtener todos los registros de la base de datos.
    """
    repo = SagaRepository()
    record = await repo.get_all_registers()
    if record:
        return record
    raise HTTPException(status_code=404, detail="Sin registros en la base de datos")


class HealthCheck(BaseModel):
    """Response model to validate and return when performing a health check."""
    status: str = "OK"

def get_health() -> HealthCheck:
    return HealthCheck(status="OK")

@router.get(
    "/ping",
    tags=["healthcheck"],
    summary="Perform a Health Check",
    response_description="Return HTTP Status Code 200 (OK)",
    status_code=status.HTTP_200_OK,
    response_model=HealthCheck,
)
async def ping() -> HealthCheck:
    """
    Endpoint para consultar el estado de la saga mediante su identificador.
    """
    return HealthCheck(status="OK")
