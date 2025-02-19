
if [ -z "$1" ]; then
    echo "Por favor, proporciona el nombre del directorio."
    exit 1
fi

directorio=$1
output="atributos_archivos.txt"

if [ ! -d "$directorio" ]; then
    echo "El directorio no existe."
    exit 1
fi

> "$output"

for archivo in "$directorio"/*; do
    if [ -f "$archivo" ]; then
        echo "Archivo: $archivo" >> "$output"
        ls -l "$archivo" | awk '{print "Permisos: " $1; print "Usuario: " $3; print "Grupo: " $4; print "Tamaño: " $5 " bytes"; print "Fecha de modificación: " $6 " " $7 " " $8}' >> "$output"
        echo "--------------------------" >> "$output"
    fi
done

echo "Los atributos de los archivos han sido guardados en $output"
