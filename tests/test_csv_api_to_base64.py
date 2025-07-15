import os
import base64
import tempfile
import sys
from scripts.csv_api_to_base64 import main as convert_to_base64

def test_csv_to_base64_conversion(monkeypatch, capsys):
    # Crear archivo CSV temporal
    with tempfile.NamedTemporaryFile(delete=False, mode='w', suffix='.csv', encoding='utf-8') as temp_csv:
        temp_csv.write("col1,col2\nval1,val2")
        temp_csv_path = temp_csv.name

    # Ruta esperada del archivo de salida
    expected_output_path = temp_csv_path.replace('.csv', '-base64.txt')

    # Simular sys.argv para pasarle la ruta del CSV como argumento
    monkeypatch.setattr(sys, 'argv', ['script.py', temp_csv_path])

    # Ejecutar función principal
    convert_to_base64()

    # Verificar si el archivo base64 fue creado
    assert os.path.exists(expected_output_path), "El archivo base64 no fue creado."

    # Leer contenido original y codificar manualmente
    with open(temp_csv_path, 'r', encoding='utf-8') as f:
        original_content = f.read()
    expected_base64 = base64.b64encode(original_content.encode('utf-8')).decode('utf-8')

    # Verificar que el contenido generado sea correcto
    with open(expected_output_path, 'r', encoding='utf-8') as f:
        result_content = f.read()
    assert result_content == expected_base64, "El contenido base64 no coincide con lo esperado."

    # Limpiar archivos temporales
    os.remove(temp_csv_path)
    os.remove(expected_output_path)

    # Verificar que se imprima el mensaje correcto (opcional)
    captured = capsys.readouterr()
    assert "Archivo convertido exitosamente" in captured.out
