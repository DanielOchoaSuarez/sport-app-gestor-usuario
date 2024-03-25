class ApiError(Exception):
    code = 500
    description = "Error interno"


class BadRequest(ApiError):
    code = 400
    description = "Los campos de la petición están incompletos o no cumplen el formato esperado"


class Unauthorized(ApiError):
    code = 401
    description = "El sesión no es válida o está vencida"


class Forbidden(ApiError):
    code = 403
    description = "No tiene permisos para acceder al recurso solicitado"


class PreconditionFailed(ApiError):
    code = 412
    description = "La información de la petición no es válida"
