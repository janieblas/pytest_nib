"""
Filename: test_004.py
Description: differents marks

Author: janieblas
Date Created: 29/06/2024
Last Modified: 29/06/2024
"""

import pytest

# Función de prueba que será omitida usando @pytest.mark.skip
@pytest.mark.skip(reason="Test is skipped due to incomplete feature")
def test_feature_in_progress():
    # Simular código de prueba
    assert False

# Función de prueba que se espera que falle usando @pytest.mark.xfail
@pytest.mark.xfail(reason="Expected to fail until issue #123 is resolved")
def test_bug_fix():
    # Simular código de prueba que fallará
    assert 1 + 1 == 3

# Función de prueba que se ejecutará solo con la etiqueta 'smoke'
@pytest.mark.smoke
def test_login():
    # Simular código de prueba para la funcionalidad de inicio de sesión
    assert True

# Función de prueba normal que se ejecutará sin marcadores
def test_addition():
    assert 2 + 2 == 4
