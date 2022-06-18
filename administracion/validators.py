from django.core.validators import RegexValidator

cp_validator = RegexValidator(
    regex='\d{5}',
    message='El código postal no tiene un formato válido',
    code='cp_invalido'
)
