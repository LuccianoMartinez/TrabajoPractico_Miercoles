from flask import Flask, render_template, request, jsonify, redirect, url_for
import requests
import traceback

app = Flask(__name__)
app.config['SECRET_KEY'] = 'dev-secret-key'

API_URL = 'http://localhost:8000/api'

@app.route('/')
def index():
    try:
        print(f"\n🔍 DEBUG: Intentando conectar a {API_URL}/eventos/")
        response = requests.get(f'{API_URL}/eventos/', timeout=5)
        print(f"✅ DEBUG: Status code: {response.status_code}")
        print(f"📦 DEBUG: Response text: {response.text[:200]}")
        
        data = response.json()
        print(f"📊 DEBUG: JSON recibido: {data}")
        
        eventos = data if isinstance(data,list) else data.get('results',[])
        print(f"✅ DEBUG: Eventos encontrados: {len(eventos)}")
                
    except Exception as e:
        print(f"❌ ERROR en index(): {str(e)}")
        traceback.print_exc()
        eventos = []
    
    return render_template('index.html', eventos=eventos)

@app.route('/evento/<int:evento_id>')
def detalle_evento(evento_id):
    try:
        response = requests.get(f'{API_URL}/eventos/{evento_id}/')
        evento = response.json()
    except:
        evento = None
    return render_template('detalle.html', evento=evento)

@app.route('/crear', methods=['GET', 'POST'])
def crear_evento():
    if request.method == 'POST':
        datos = {
            'titulo': request.form['titulo'],
            'descripcion': request.form['descripcion'],
            'fecha': request.form['fecha'],
            'ubicacion': request.form['ubicacion'],
            'capacidad': int(request.form['capacidad']),
        }
        try:
            print(f"\n📝 DEBUG: Enviando datos a Django: {datos}")
            response = requests.post(f'{API_URL}/eventos/', json=datos, timeout=5)
            print(f"✅ DEBUG: Response status: {response.status_code}")
            print(f"✅ DEBUG: Response text: {response.text}")
            
            if response.status_code == 201:
                return redirect('/')
        except Exception as e:
            print(f"❌ ERROR al crear: {str(e)}")
    return render_template('crear.html')

@app.route('/api/confirmar/<int:evento_id>', methods=['POST'])
def confirmar_asistencia(evento_id):
    try:
        response = requests.post(f'{API_URL}/eventos/{evento_id}/confirmar_asistencia/')
        return jsonify(response.json())
    except:
        return jsonify({'error': 'Error'}), 400

@app.route('/api/cancelar/<int:evento_id>', methods=['POST'])
def cancelar_asistencia(evento_id):
    try:
        response = requests.post(f'{API_URL}/eventos/{evento_id}/cancelar_asistencia/')
        return jsonify(response.json())
    except:
        return jsonify({'error': 'Error'}), 400

if __name__ == '__main__':
    app.run(debug=True, port=5000)