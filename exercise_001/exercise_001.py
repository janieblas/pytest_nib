def calcular_area_rectangulo(base, altura):
    """
    Calcula el área de un rectángulo.

    Args:
    - base (float): La base del rectángulo.
    - altura (float): La altura del rectángulo.

    Returns:
    - float: El área calculada del rectángulo.
    """
    if base <= 0 or altura <= 0:
        raise ValueError("La base y altura deben ser mayores que cero.")
    return base * altura