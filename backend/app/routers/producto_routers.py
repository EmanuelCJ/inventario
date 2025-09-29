from flask import Blueprint, request, jsonify
from app.controllers.producto_controllers import ProductoControllers

producto_bp = Blueprint("producto_bp", __name__)

# CREATE
@producto_bp.route("/productos", methods=["POST"])
def create_producto():
    data = request.get_json()
    producto = ProductoControllers.create_producto(data)
    if producto:
        return jsonify(producto.to_dict()), 201
    return jsonify({"error": "No se pudo crear el producto"}), 400

# READ ONE
@producto_bp.route("/productos/<int:id_producto>", methods=["GET"])
def get_producto(id_producto):
    producto = ProductoControllers.get_producto(id_producto)
    if producto:
        return jsonify(producto.to_dict()), 200
    return jsonify({"error": "Producto no encontrado"}), 404

# READ ALL
@producto_bp.route("/productos", methods=["GET"])
def get_productos():
    productos = ProductoControllers.get_productos()
    return jsonify([p.to_dict() for p in productos]), 200

# UPDATE
@producto_bp.route("/productos/<int:id_producto>", methods=["PUT"])
def update_producto(id_producto):
    data = request.get_json()
    producto = ProductoControllers.update_producto(id_producto, data)
    if producto:
        return jsonify(producto.to_dict()), 200
    return jsonify({"error": "No se pudo actualizar el producto"}), 400

# DELETE
@producto_bp.route("/productos/<int:id_producto>", methods=["DELETE"])
def delete_producto(id_producto):
    success = ProductoControllers.delete_producto(id_producto)
    if success:
        return jsonify({"message": "Producto eliminado"}), 200
    return jsonify({"error": "No se pudo eliminar el producto"}), 400