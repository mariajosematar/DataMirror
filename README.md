# DataMirror

DataMirror es una aplicación innovadora que analiza tu huella digital para proporcionar insights personalizados sobre tus hábitos en línea y proyecciones futuras.

## Características
- Conexión segura con plataformas externas (GitHub implementado como ejemplo)
- Análisis de datos de usuario en tiempo real
- Visualización de insights y predicciones personalizadas
- Arquitectura escalable y segura

## Tecnologías utilizadas
- **Backend**: FastAPI (Python)
- **Frontend**: React con TypeScript
- **Base de datos**: PostgreSQL
- **Autenticación**: OAuth2 con GitHub
- **Despliegue**: Docker, Docker Compose

## Configuración del proyecto

### Requisitos previos
- Python 3.8+
- Node.js 14+
- Docker y Docker Compose
- Cuenta de GitHub y una aplicación OAuth registrada

### Configuración del backend
1. Navega al directorio backend: `cd backend`
2. Crea un archivo `.env` con las siguientes variables:
    ```env
    DATABASE_URL=postgresql://user:password@db/datamirror
    GITHUB_CLIENT_ID=tu_github_client_id
    GITHUB_CLIENT_SECRET=tu_github_client_secret
    ```
3. Instala las dependencias: `pip install -r requirements.txt`
4. Inicia el backend: `uvicorn main:app --reload`

### Configuración del frontend
1. Navega al directorio frontend: `cd frontend`
2. Crea un archivo `.env` con las siguientes variables:
    ```env
    REACT_APP_API_URL=http://localhost:8000
    REACT_APP_GITHUB_CLIENT_ID=tu_github_client_id
    ```
3. Instala las dependencias: `npm install`
4. Inicia el frontend: `npm start`

### Ejecución del proyecto
1. En la raíz del proyecto, ejecuta: `docker-compose up --build`
2. Abre un navegador y ve a `http://localhost:3000`

## Desarrollo

### Para ejecutar los tests del backend:
1. Navega al directorio backend: `cd backend`
2. Ejecuta los tests: `pytest`

### Para ejecutar los tests del frontend:
1. Navega al directorio frontend: `cd frontend`
2. Ejecuta los tests: `npm test`

## Contribuciones

Las contribuciones son bienvenidas. Por favor, abre un issue para discutir cambios mayores antes de crear un pull request.

## Licencia

Este proyecto está licenciado bajo la Licencia MIT.
