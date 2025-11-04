from pydantic import BaseModel, field_validator, ValidationError
import re

# Patrón básico para detectar inyecciones SQL
# Esto es una simplificación; la forma más segura es usar consultas parametrizadas.