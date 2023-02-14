from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from flask_restful import Api
from modelos.modelos import db
from datetime import timedelta
from vistas import VistaHealthCheck, VistaObtenerOrden, VistaCrearOrden, VistaObtenerOrdenes, VistaActualizarStatus, VistaCancelarOrden
DATABASE_URI = 'sqlite:///restaurants.db'

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = 'frase-secreta-restaurante'
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(minutes=1)

app_context = app.app_context()
app_context.push()
db.init_app(app)
db.create_all()

cors = CORS(app)

api = Api(app)
# HealthCheck -> GET
api.add_resource(VistaHealthCheck, '/orders/health')
# Crear Orden -> POST
api.add_resource(VistaCrearOrden, '/orders/')
# Obtener Ordenes -> GET
api.add_resource(VistaObtenerOrdenes, '/orders/')
# Obtener orden por ID -> GET
api.add_resource(VistaObtenerOrden, '/orders/<int:id_orden>')
# Actualizar orden por id -> PUT
api.add_resource(VistaActualizarStatus, '/orders/<int:id_orden>')
# Cancelar orden por id -> DELETE
api.add_resource(VistaCancelarOrden, '/orders/<int:id_orden>')

# Componente para manejar JWT
jwt = JWTManager(app)

print(' * ORDERS corriendo ----------------')

if __name__ == "__main__":
    HOST = '0.0.0.0'
    PORT = 5001
    app.run(HOST, PORT, debug=True) 

# orders = []

# @app.route('/orders', methods=['GET'])
# def get_orders():
#     return jsonify(orders)

# @app.route('/orders', methods=['POST'])
# def create_order():
#     data = request.get_json()
#     order = {
#         'id': len(orders) + 1,
#         'item': data['item'],
#         'price': data['price'],
#         'status': 'pending'
#     }
#     orders.append(order)
#     return jsonify(order)

# if __name__ == '__main__':
#     app.run()
