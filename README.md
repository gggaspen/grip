# HedgeDoc - Collaborative Markdown Editor

Proyecto HedgeDoc configurado para deployment en Railway.

## Deployment en Railway

### Paso 1: Crear nuevo proyecto en Railway

1. Ve a [Railway](https://railway.app)
2. Crea un nuevo proyecto
3. Conecta tu repositorio de GitHub

### Paso 2: Agregar base de datos PostgreSQL

1. En tu proyecto de Railway, haz clic en "New Service"
2. Selecciona "Database" → "PostgreSQL"
3. Railway creará automáticamente la base de datos y la variable `DATABASE_URL`

### Paso 3: Configurar variables de entorno

En la configuración de tu servicio principal, agrega estas variables:

```
CMD_DB_URL=${{Postgres.DATABASE_URL}}
CMD_DOMAIN=tu-app.up.railway.app
CMD_URL_ADDPORT=false
CMD_PROTOCOL_USESSL=true
CMD_SESSION_SECRET=genera_un_string_aleatorio_seguro_aqui
```

**Importante:** Reemplaza `tu-app.up.railway.app` con el dominio que Railway te asigne.

### Paso 4: Deploy

Railway detectará automáticamente el Dockerfile y hará el build. El servicio estará disponible en el puerto 3000.

## Desarrollo Local con Docker Compose

Para correr localmente:

```bash
docker-compose up -d
```

Accede a http://localhost:3000

## Configuración Adicional

Consulta la [documentación oficial de HedgeDoc](https://docs.hedgedoc.org/configuration/) para más opciones de configuración.

## Variables de Entorno Importantes

- `CMD_DB_URL`: URL de conexión a PostgreSQL
- `CMD_DOMAIN`: Dominio de tu aplicación
- `CMD_SESSION_SECRET`: Secret para las sesiones (debe ser aleatorio y seguro)
- `CMD_PROTOCOL_USESSL`: Usar HTTPS (true en producción)
