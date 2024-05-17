from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///almacen.db'
db = SQLAlchemy(app)


# Definición de modelos
class Categoria(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(80), unique=True, nullable=False)
    productos = db.relationship('Producto', backref='categoria', lazy='dynamic')


    def __repr__(self):
        return f'<Categoria {self.nombre}>'


class Proveedor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(80), unique=True, nullable=False)
    correo = db.Column(db.String(100), unique=True, nullable=False)
    productos = db.relationship('Producto', backref='proveedor', lazy='dynamic')


    def __repr__(self):
        return f'<Proveedor {self.nombre}>'


class Producto(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(80), nullable=False)
    cantidad = db.Column(db.Integer, nullable=False)
    categoria_id = db.Column(db.Integer, db.ForeignKey('categoria.id'), nullable=False)
    proveedor_id = db.Column(db.Integer, db.ForeignKey('proveedor.id'), nullable=False)


    def __repr__(self):
        return f'<Producto {self.nombre}>'


# CRUD para Categorías
@app.route('/categoria', methods=['POST'])
def crear_categoria():
    data = request.get_json()
    nueva_categoria = Categoria(nombre=data['nombre'])
    db.session.add(nueva_categoria)
    db.session.commit()
    return jsonify({'mensaje': 'Categoría creada exitosamente'}), 201


@app.route('/categoria', methods=['GET'])
def leer_categorias():
    categorias = Categoria.query.all()
    return jsonify([{'id': cat.id, 'nombre': cat.nombre} for cat in categorias])


@app.route('/categoria/<int:id>', methods=['PUT'])
def actualizar_categoria(id):
    categoria = Categoria.query.get_or_404(id)
    data = request.get_json()
    categoria.nombre = data['nombre']
    db.session.commit()
    return jsonify({'mensaje': 'Categoría actualizada exitosamente'})


@app.route('/categoria/<int:id>', methods=['DELETE'])
def eliminar_categoria(id):
    categoria = Categoria.query.get_or_404(id)
    db.session.delete(categoria)
    db.session.commit()
    return jsonify({'mensaje': 'Categoría eliminada exitosamente'})


# CRUD para Proveedores
@app.route('/proveedor', methods=['POST'])
def crear_proveedor():
    data = request.get_json()
    nuevo_proveedor = Proveedor(nombre=data['nombre'], correo=data['correo'])
    db.session.add(nuevo_proveedor)
    db.session.commit()
    return jsonify({'mensaje': 'Proveedor creado exitosamente'}), 201


@app.route('/proveedor', methods=['GET'])
def leer_proveedores():
    proveedores = Proveedor.query.all()
    return jsonify([{'id': prov.id, 'nombre': prov.nombre, 'correo': prov.correo} for prov in proveedores])


@app.route('/proveedor/<int:id>', methods=['PUT'])
def actualizar_proveedor(id):
    proveedor = Proveedor.query.get_or_404(id)
    data = request.get_json()
    proveedor.nombre = data['nombre']
    proveedor.correo = data['correo']
    db.session.commit()
    return jsonify({'mensaje': 'Proveedor actualizado exitosamente'})


@app.route('/proveedor/<int:id>', methods=['DELETE'])
def eliminar_proveedor(id):
    proveedor = Proveedor.query.get_or_404(id)
    db.session.delete(proveedor)
    db.session.commit()
    return jsonify({'mensaje': 'Proveedor eliminado exitosamente'})


# CRUD para Productos
@app.route('/producto', methods=['POST'])
def crear_producto():
    data = request.get_json()
    nuevo_producto = Producto(
        nombre=data['nombre'],
        cantidad=data['cantidad'],
        categoria_id=data['categoria_id'],
        proveedor_id=data['proveedor_id']
    )
    db.session.add(nuevo_producto)
    db.session.commit()
    return jsonify({'mensaje': 'Producto creado exitosamente'}), 201


@app.route('/producto', methods=['GET'])
def leer_productos():
    productos = Producto.query.all()
    return jsonify([
        {
            'id': prod.id,
            'nombre': prod.nombre,
            'cantidad': prod.cantidad,
            'categoria': prod.categoria.nombre,
            'proveedor': prod.proveedor.nombre
        } for prod in productos
    ])


@app.route('/producto/<int:id>', methods=['PUT'])
def actualizar_producto(id):
    producto = Producto.query.get_or_404(id)
    data = request.get_json()
    producto.nombre = data['nombre']
    producto.cantidad = data['cantidad']
    producto.categoria_id = data['categoria_id']
    producto.proveedor_id = data['proveedor_id']
    db.session.commit()
    return jsonify({'mensaje': 'Producto actualizado exitosamente'})


@app.route('/producto/<int:id>', methods=['DELETE'])
def eliminar_producto(id):
    producto = Producto.query.get_or_404(id)
    db.session.delete(producto)
    db.session.commit()
    return jsonify({'mensaje': 'Producto eliminado exitosamente'})


if __name__ == '__main__':  # Crea las tablas en la base de datos
    app.run(debug=True, host='0.0.0.0')