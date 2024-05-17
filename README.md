# Sistema-de-gestion-de-almacen
Esun sistema que gestiona los productos almacenados segun su categoria y proveedor
# Endpoints
[Categoria](http://andresmedin11.pythonanywhere.com/categoria)

POST: {"nombre": "valor"}
PUT: http://andresmedin11.pythonanywhere.com/categoria/{id_categoria} y {"nombre": "valor"}
GET: SOLO EL ENLACE
DELETE: http://andresmedin11.pythonanywhere.com/categoria/{id_categoria}

[Proveedor](http://andresmedin11.pythonanywhere.com/proveedor)

POST: {"nombre": "valor", "correo": "valor"}
PUT: http://andresmedin11.pythonanywhere.com/proveedor/{id_proveedor} y {"nombre": "valor", "correo": "valor"}
GET: SOLO EL ENLACE
DELETE: http://andresmedin11.pythonanywhere.com/proveedor/{id_proveedor}

[Producto](http://andresmedin11.pythonanywhere.com/producto)

POST: {"nombre": "valor", "cantidad": "valor", "categoria_id": "valor", "proveedor_id": "valor"}
PUT: http://andresmedin11.pythonanywhere.com/producto/{id_producto} y {"nombre": "valor", "cantidad": "valor", "categoria_id": "valor", "proveedor_id": "valor"}
GET: SOLO EL ENLACE
DELETE: http://andresmedin11.pythonanywhere.com/producto/{id_producto}
