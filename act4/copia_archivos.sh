
if [ -z "$1" ]; then
    echo "Por favor, proporciona el nombre del archivo de destino."
    exit 1
fi

if [ ! -f eventos.txt ]; then
    echo "El archivo eventos.txt no existe en el directorio."
    exit 1
fi

cp eventos.txt "$1"
echo "El contenido de eventos.txt ha sido copiado a $1"
