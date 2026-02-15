# TaskFlow - Task & Project Manager

Applicazione web per la gestione di progetti e task, sviluppata come progetto per il corso di Tecnologie Web - UNIMORE.

## 👨‍💻 Autore
Colince Tcheussieu Mendji

## 📝 Descrizione

TaskFlow è un'applicazione web semplice ma completa per organizzare progetti e task. Permette di:
- ✅ Creare e gestire progetti
- ✅ Aggiungere task ai progetti
- ✅ Visualizzare lo stato dei task (Da Fare, In Corso, Completato)
- ✅ Dashboard interattiva con React
- ✅ API REST per accesso ai dati

## 🛠 Tecnologie Utilizzate

### Backend
- **Flask** - Framework web Python
- **CSV** - Storage dei dati

### Frontend
- **HTML5** - Struttura pagine
- **CSS3** - Styling e responsive design
- **Jinja2** - Template engine
- **React** - Dashboard interattiva

## 📁 Struttura Progetto

```
TaskFlow/
├── app.py                      # Applicazione Flask principale
├── requirements.txt            # Dipendenze Python
├── static/
│   ├── data/
│   │   ├── projects.csv       # Database progetti
│   │   └── tasks.csv          # Database task
│   └── css/
│       └── style.css          # Stili CSS
└── templates/
    ├── base.html              # Template base
    ├── index.html             # Homepage - Lista progetti
    ├── project_detail.html    # Dettaglio progetto
    ├── create_project.html    # Form nuovo progetto
    ├── create_task.html       # Form nuovo task
    └── dashboard.html         # Dashboard React
```

## 🚀 Installazione e Avvio

### 1. Prerequisiti
- Python 3.8 o superiore

### 2. Installazione

```bash
# Entra nella directory del progetto
cd TaskFlow

# Installa le dipendenze
pip install -r requirements.txt

# Avvia l'applicazione
python app.py
```

### 3. Accesso

Apri il browser su: **http://127.0.0.1:5000**

## 📄 Pagine dell'Applicazione

1. **Home** (`/`) - Lista di tutti i progetti con statistiche
2. **Dettaglio Progetto** (`/project/<id>`) - Visualizza task del progetto
3. **Nuovo Progetto** (`/create-project`) - Form per creare un progetto
4. **Nuovo Task** (`/create-task/<id>`) - Form per creare un task
5. **Dashboard** (`/dashboard`) - Dashboard interattiva con React

## 🔌 API REST

L'applicazione espone le seguenti API in formato JSON:

- `GET /api/projects` - Restituisce tutti i progetti
- `GET /api/tasks` - Restituisce tutti i task
- `GET /api/projects/<id>/tasks` - Restituisce i task di un progetto

### Esempio di utilizzo:

```javascript
// Recupera tutti i progetti
fetch('/api/projects')
    .then(response => response.json())
    .then(data => console.log(data));
```

## ✨ Funzionalità CRUD

### Progetti
- **CREATE**: Form `/create-project`
- **READ**: Lista progetti `/` e dettaglio `/project/<id>`
- **UPDATE**: Non implementato (può essere aggiunto)
- **DELETE**: Link "Elimina" su ogni progetto

### Task
- **CREATE**: Form `/create-task/<project_id>`
- **READ**: Lista task in dettaglio progetto
- **UPDATE**: Cambio status task (Da Fare → In Corso → Completato)
- **DELETE**: Link "Elimina" su ogni task

## 🎨 Design

- Design moderno e pulito
- Colori personalizzabili per i progetti
- Badge per status e priorità
- Progress bar per completamento progetti
- Responsive design per mobile

## 🎯 Requisiti Soddisfatti per la Tesina

- ✅ **Almeno 4 pagine**: Home, Dettaglio, Create Project, Create Task, Dashboard
- ✅ **Template**: Uso di Jinja2 per template riutilizzabili
- ✅ **CSS**: Styling completo e responsive
- ✅ **JavaScript**: Dashboard interattiva con React
- ✅ **API**: API REST per progetti e task
- ✅ **CRUD**: Visualizzare, inserire, eliminare, modificare risorse
- ✅ **Funzionalità**: Sistema completo di gestione progetti e task

## 📊 Dati di Esempio

L'applicazione include dati di esempio:
- 3 progetti predefiniti
- 7 task di esempio distribuiti tra i progetti

## 🔧 Personalizzazione

### Aggiungere nuovi progetti
Aggiungi righe al file `static/data/projects.csv`:
```
id,name,description,color,created_at
4,Nuovo Progetto,Descrizione,#3b82f6,2024-01-01T10:00:00
```

### Modificare i colori
Modifica le variabili CSS in `static/css/style.css`:
```css
:root {
    --primary: #3b82f6;
    --success: #10b981;
    ...
}
```

## 📝 Note Tecniche

- I dati sono salvati in file CSV nella directory `static/data/`
- Non richiede database esterni
- Session-less: nessun sistema di autenticazione
- Ideale per uso singolo utente o demo

## 🐛 Troubleshooting

**Problema: ModuleNotFoundError: No module named 'flask'**
```bash
pip install -r requirements.txt
```

**Problema: File CSV non trovato**
Assicurati che la struttura delle directory sia corretta e che i file CSV esistano in `static/data/`.

## 📚 Risorse

- [Flask Documentation](https://flask.palletsprojects.com/)
- [Jinja2 Documentation](https://jinja.palletsprojects.com/)
- [React Documentation](https://react.dev/)

## 📜 Licenza

Progetto sviluppato per scopi didattici - Corso Tecnologie Web UNIMORE 2024

# TESINA-TECNOLOGIE-WEB
# TESINA-TECNOLOGIE-WEB
# TESINA-TECNOLOGIE-WEB
# TESINA-TECNOLOGIE-WEB
# TESINA-TECNOLOGIE-WEB
