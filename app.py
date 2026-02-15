from flask import Flask, render_template, request, redirect, url_for, jsonify
import csv
from datetime import datetime
import os

app = Flask(__name__)

# ============================================================================
# FUNZIONI PER LEGGERE I DATI DAI FILE CSV
# ============================================================================

def get_projects():
    """Legge e restituisce tutti i progetti dal file CSV"""
    projects = []
    csv_path = os.path.join('static', 'data', 'projects.csv')
    try:
        with open(csv_path, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                projects.append(row)
    except FileNotFoundError:
        print(f"File {csv_path} non trovato")
    return projects

def get_tasks():
    """Legge e restituisce tutti i task dal file CSV"""
    tasks = []
    csv_path = os.path.join('static', 'data', 'tasks.csv')
    try:
        with open(csv_path, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                tasks.append(row)
    except FileNotFoundError:
        print(f"File {csv_path} non trovato")
    return tasks

# ============================================================================
# ROUTE: HOME - Lista tutti i progetti
# ============================================================================

@app.route('/')
def index():
    """Pagina principale con lista progetti"""
    projects = get_projects()
    tasks = get_tasks()

    # Aggiungi conteggio task per ogni progetto
    for project in projects:
        project_tasks = [t for t in tasks if t['project_id'] == project['id']]
        project['task_count'] = len(project_tasks)
        project['tasks_completed'] = len([t for t in project_tasks if t['status'] == 'done'])

    return render_template('index.html', projects=projects)

# ============================================================================
# ROUTE: DETTAGLIO PROGETTO - Mostra un progetto con i suoi task
# ============================================================================

@app.route('/project/<project_id>')
def project_detail(project_id):
    """Pagina di dettaglio di un progetto con lista task"""
    projects = get_projects()
    tasks = get_tasks()

    # Trova il progetto
    project = None
    for p in projects:
        if p['id'] == project_id:
            project = p
            break

    if not project:
        return "Progetto non trovato", 404

    # Trova i task del progetto
    project_tasks = [t for t in tasks if t['project_id'] == project_id]

    return render_template('project_detail.html', project=project, tasks=project_tasks)

# ============================================================================
# ROUTE: CREA PROGETTO - Form e salvataggio
# ============================================================================

@app.route('/create-project', methods=['GET'])
def create_project_form():
    """Form per creare un nuovo progetto"""
    return render_template('create_project.html')

@app.route('/create-project', methods=['POST'])
def create_project():
    """Salva un nuovo progetto nel CSV"""
    name = request.form.get('name')
    description = request.form.get('description', '')
    color = request.form.get('color', '#3b82f6')

    # Genera nuovo ID
    projects = get_projects()
    new_id = '1'
    if projects:
        max_id = max([int(p['id']) for p in projects])
        new_id = str(max_id + 1)

    # Salva nel CSV
    csv_path = os.path.join('static', 'data', 'projects.csv')
    with open(csv_path, 'a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow([new_id, name, description, color, datetime.now().isoformat()])

    return redirect(url_for('index'))

# ============================================================================
# ROUTE: ELIMINA PROGETTO
# ============================================================================

@app.route('/delete-project/<project_id>')
def delete_project(project_id):
    """Elimina un progetto e i suoi task"""
    # Leggi progetti
    projects = get_projects()
    # Filtra il progetto da eliminare
    projects = [p for p in projects if p['id'] != project_id]

    # Riscrivi il file CSV
    csv_path = os.path.join('static', 'data', 'projects.csv')
    with open(csv_path, 'w', newline='', encoding='utf-8') as file:
        fieldnames = ['id', 'name', 'description', 'color', 'created_at']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(projects)

    # Elimina anche i task del progetto
    tasks = get_tasks()
    tasks = [t for t in tasks if t['project_id'] != project_id]

    csv_path = os.path.join('static', 'data', 'tasks.csv')
    with open(csv_path, 'w', newline='', encoding='utf-8') as file:
        fieldnames = ['id', 'project_id', 'title', 'description', 'status', 'priority', 'created_at']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(tasks)

    return redirect(url_for('index'))

# ============================================================================
# ROUTE: CREA TASK - Form e salvataggio
# ============================================================================

@app.route('/create-task/<project_id>', methods=['GET'])
def create_task_form(project_id):
    """Form per creare un nuovo task"""
    projects = get_projects()
    project = None
    for p in projects:
        if p['id'] == project_id:
            project = p
            break
    return render_template('create_task.html', project=project)

@app.route('/create-task/<project_id>', methods=['POST'])
def create_task(project_id):
    """Salva un nuovo task nel CSV"""
    title = request.form.get('title')
    description = request.form.get('description', '')
    status = request.form.get('status', 'todo')
    priority = request.form.get('priority', 'medium')

    # Genera nuovo ID
    tasks = get_tasks()
    new_id = '1'
    if tasks:
        max_id = max([int(t['id']) for t in tasks])
        new_id = str(max_id + 1)

    # Salva nel CSV
    csv_path = os.path.join('static', 'data', 'tasks.csv')
    with open(csv_path, 'a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow([new_id, project_id, title, description, status, priority, datetime.now().isoformat()])

    return redirect(url_for('project_detail', project_id=project_id))

# ============================================================================
# ROUTE: ELIMINA TASK
# ============================================================================

@app.route('/delete-task/<task_id>/<project_id>')
def delete_task(task_id, project_id):
    """Elimina un task"""
    tasks = get_tasks()
    tasks = [t for t in tasks if t['id'] != task_id]

    # Riscrivi il file CSV
    csv_path = os.path.join('static', 'data', 'tasks.csv')
    with open(csv_path, 'w', newline='', encoding='utf-8') as file:
        fieldnames = ['id', 'project_id', 'title', 'description', 'status', 'priority', 'created_at']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(tasks)

    return redirect(url_for('project_detail', project_id=project_id))

# ============================================================================
# ROUTE: CAMBIA STATUS TASK (per Kanban)
# ============================================================================

@app.route('/update-task-status/<task_id>/<new_status>/<project_id>')
def update_task_status(task_id, new_status, project_id):
    """Aggiorna lo status di un task"""
    tasks = get_tasks()

    for task in tasks:
        if task['id'] == task_id:
            task['status'] = new_status
            break

    # Riscrivi il file CSV
    csv_path = os.path.join('static', 'data', 'tasks.csv')
    with open(csv_path, 'w', newline='', encoding='utf-8') as file:
        fieldnames = ['id', 'project_id', 'title', 'description', 'status', 'priority', 'created_at']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(tasks)

    return redirect(url_for('project_detail', project_id=project_id))

# ============================================================================
# API: Restituisce tutti i progetti in JSON
# ============================================================================

@app.route('/api/projects')
def api_projects():
    """API che restituisce tutti i progetti in JSON"""
    projects = get_projects()
    return jsonify(projects)

# ============================================================================
# API: Restituisce tutti i task in JSON
# ============================================================================

@app.route('/api/tasks')
def api_tasks():
    """API che restituisce tutti i task in JSON"""
    tasks = get_tasks()
    return jsonify(tasks)

# ============================================================================
# API: Restituisce i task di un progetto
# ============================================================================

@app.route('/api/projects/<project_id>/tasks')
def api_project_tasks(project_id):
    """API che restituisce i task di un progetto specifico"""
    tasks = get_tasks()
    project_tasks = [t for t in tasks if t['project_id'] == project_id]
    return jsonify(project_tasks)

# ============================================================================
# ROUTE: DASHBOARD REACT - Kanban board interattiva
# ============================================================================

@app.route('/dashboard')
def dashboard():
    """Dashboard interattiva con React"""
    return render_template('dashboard.html')

# ============================================================================
# AVVIO APPLICAZIONE
# ============================================================================

if __name__ == '__main__':
    print("\n" + "="*60)
    print("🚀 TaskFlow - Task & Project Manager")
    print("="*60)
    print("Server: http://127.0.0.1:5000")
    print("=" *60 + "\n")
    app.run(debug=True)
