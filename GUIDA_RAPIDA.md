# Guida Rapida - TaskFlow

## 🚀 Avvio Rapido

### 1. Apri il Terminale

```bash
cd "/Users/colincetcheussieumendji/Desktop/COURSES UNIMORE/Technologie_Web/TaskFlow"
```

### 2. Installa Flask (se necessario)

```bash
pip3 install Flask
```

### 3. Avvia l'applicazione

```bash
python3 app.py
```

Vedrai questo output:
```
============================================================
🚀 TaskFlow - Task & Project Manager
============================================================
Server: http://127.0.0.1:5000
============================================================
```

### 4. Apri il browser

Vai su: **http://127.0.0.1:5000**

## 📱 Naviga l'Applicazione

1. **Homepage**: Visualizza tutti i progetti
2. Clicca su "Visualizza" per vedere i task di un progetto
3. Clicca su "+ Nuovo Progetto" per creare un progetto
4. Clicca su "+ Nuovo Task" per aggiungere task
5. Clicca su "Dashboard" per la vista Kanban con React

## ✨ Funzionalità

### Progetti
- Crea: Bottone "+ Nuovo Progetto"
- Visualizza: Lista nella homepage
- Elimina: Bottone 🗑️ su ogni progetto

### Task
- Crea: Bottone "+ Nuovo Task" nella pagina del progetto
- Cambia Status: Bottoni "▶️ Inizia" e "✓ Completa"
- Elimina: Bottone 🗑️ su ogni task

### Dashboard React
- Visualizza statistiche generali
- Kanban board con colonne: Da Fare, In Corso, Completati
- Dati caricati tramite API REST

## 🔌 API REST (Test)

Prova le API nel browser:

1. **Tutti i progetti**: http://127.0.0.1:5000/api/projects
2. **Tutti i task**: http://127.0.0.1:5000/api/tasks
3. **Task di un progetto**: http://127.0.0.1:5000/api/projects/1/tasks

## 📊 Struttura Dati

### Projects.csv
```
id,name,description,color,created_at
1,Nome Progetto,Descrizione,#3b82f6,2024-01-01T10:00:00
```

### Tasks.csv
```
id,project_id,title,description,status,priority,created_at
1,1,Titolo Task,Descrizione,todo,high,2024-01-01T10:00:00
```

**Status possibili**: `todo`, `in_progress`, `done`
**Priority possibili**: `low`, `medium`, `high`

## 🎨 Personalizzazione Colori

Modifica i colori in `static/css/style.css`:
```css
:root {
    --primary: #3b82f6;    /* Blu */
    --success: #10b981;    /* Verde */
    --warning: #f59e0b;    /* Giallo */
    --danger: #ef4444;     /* Rosso */
}
```

## 🐛 Risoluzione Problemi

### Errore: Flask non installato
```bash
pip3 install Flask
```

### Errore: Porta già in uso
Cambia la porta in `app.py`:
```python
app.run(debug=True, port=5001)
```

### File CSV non trovati
Verifica che esistano:
- `static/data/projects.csv`
- `static/data/tasks.csv`

## 📝 Note per la Tesina

### Requisiti Soddisfatti
- ✅ Almeno 4 pagine (ne abbiamo 5!)
- ✅ Template Jinja2
- ✅ CSS personalizzato e responsive
- ✅ JavaScript/React per interattività
- ✅ API REST in JSON
- ✅ CRUD completo
- ✅ Storage dati (CSV)

### Punti di Forza
1. Design moderno e professionale
2. Codice ben organizzato e commentato
3. Dashboard interattiva con React
4. API REST funzionanti
5. Responsive per mobile
6. Facile da estendere

### Funzionalità Extra Implementate
- Progress bar per progetti
- Badge colorati per status e priorità
- Statistiche nella dashboard React
- Kanban board visuale
- Colori personalizzabili per progetti

## 💡 Idee per Estensioni Future

1. **Ricerca e Filtri**: Aggiungere ricerca per titolo task
2. **Data Scadenza**: Aggiungere campo due_date ai task
3. **Modifica**: Form per modificare progetti/task esistenti
4. **Export**: Esportare progetti in PDF/Excel
5. **Drag & Drop**: Riordinare task con drag & drop
6. **Grafici**: Aggiungere grafici statistiche con Chart.js
7. **Multi-utente**: Sistema di login (opzionale)

## 📚 Documentazione Codice

### Route Principali
- `/` - Homepage con lista progetti
- `/project/<id>` - Dettaglio progetto
- `/create-project` - Form nuovo progetto
- `/create-task/<project_id>` - Form nuovo task
- `/dashboard` - Dashboard React
- `/api/*` - Endpoints API REST

### Template
- `base.html` - Template base ereditato da tutti
- Altri template estendono `base.html` con blocchi:
  - `{% block title %}` - Titolo pagina
  - `{% block content %}` - Contenuto
  - `{% block scripts %}` - Script JS

### Stili CSS
File principale: `static/css/style.css`
- Layout responsive con CSS Grid
- Variabili CSS per colori
- Animazioni e transizioni
- Mobile-first design

## 🎓 Presentazione Tesina

### Cosa Mostrare
1. Homepage con progetti
2. Dettaglio progetto con task
3. Creazione nuovo progetto
4. Creazione task
5. Dashboard React interattiva
6. API REST nel browser
7. Responsive design (resize finestra)

### Punti da Evidenziare
- Semplicità ma completezza
- CRUD funzionante
- Integrazione React
- API REST
- Design professionale
- Codice ben strutturato


