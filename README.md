# api-aws-ec2

API mínima en Flask que devuelve "Hola Mundo".

## Requisitos

- Python 3.10+ (recomendado 3.11 o 3.12)

## Configuración rápida (macOS / zsh)

1. Crear entorno virtual (opcional pero recomendado)

```zsh
python3 -m venv .venv
source .venv/bin/activate
```

2. Instalar dependencias

```zsh
pip install -r requirements.txt
```

3. Ejecutar la API

```zsh
python main.py
```

La API se iniciará en http://127.0.0.1:5000

4. Probar

```zsh
curl -s http://127.0.0.1:5000/
```

Deberías ver:

```
Hola Mundo
```

## Estructura

- `main.py`: App Flask con una ruta `/` que devuelve "Hola Mundo".
- `requirements.txt`: Dependencias del proyecto.
