class ApiError(Exception):
    code = 500
    description = "Error interno"


class BadRequest(ApiError):
    code = 400
    description = "Los campos de la petición están incompletos o no cumplen el formato esperado"


class Unauthorized(ApiError):
    code = 401
    description = "La petición no cuenta con el token, no es válido o está vencido"


class Forbidden(ApiError):
    code = 403
    description = "No tiene permisos para acceder al recurso solicitado"


class ResourceNotFound(ApiError):
    def __init__(self, description=None):
        super().__init__()
        self.code = 404
        self.description = description or "El recurso solicitado no existe"


class PreconditionFailed(ApiError):
    code = 412
    description = "La información de la petición no es válida"
