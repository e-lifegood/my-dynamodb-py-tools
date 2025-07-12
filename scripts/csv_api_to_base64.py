import os
import base64
import sys

def main():
    try:
        # Verifica que se haya pasado un argumento por la línea de comandos        
        if len(sys.argv) < 2:
            print("Uso: python script.py <ruta_del_archivo_csv>")            
            csv_file_path = input("Ingrese la ruta completa del archivo CSV: ")
        else:
            csv_file_path = sys.argv[1]
            print(csv_file_path)
            
        if not csv_file_path or not os.path.exists(csv_file_path):
            print("El archivo especificado no existe.")
            return

        # Lee todo el contenido del archivo CSV
        with open(csv_file_path, 'r', encoding='utf-8') as file:
            csv_content = file.read()

        # Convierte el contenido a Base64
        base64_content = base64.b64encode(csv_content.encode('utf-8')).decode('utf-8')

        # Genera el nombre del archivo de salida con extensión .txt
        output_file_path = os.path.splitext(csv_file_path)[0] + "-base64.txt"

        # Escribe el contenido Base64 en el archivo de salida
        with open(output_file_path, 'w', encoding='utf-8') as file:
            file.write(base64_content)

        print(f"Archivo convertido exitosamente. Guardado como: {output_file_path}")

    except Exception as ex:
        print(f"Ocurrió un error: {ex}")

    input("**Fin**")

if __name__ == "__main__":
    main()
