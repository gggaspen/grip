FROM quay.io/hedgedoc/hedgedoc:1.10.5

# HedgeDoc expone el puerto 3000
EXPOSE 3000

# El contenedor ya tiene todo configurado
CMD ["node", "app.js"]
