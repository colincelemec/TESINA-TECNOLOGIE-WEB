# Presentazione PowerPoint - TaskFlow
## Contenuto per ogni slide

---

## SLIDE 1 - Copertina
**Layout:** Titolo + sottotitolo centrato

### Contenuto:
```
TaskFlow
Task & Project Manager

Tesina Tecnologie Web
UNIMORE - 2026

Colince Tcheussieu Mendji
```

**Suggerimenti grafici:**
- Sfondo gradiente viola/blu (come il logo)
- Logo TaskFlow grande al centro
- Font moderno e pulito

---

## SLIDE 2 - Introduzione
**Titolo:** Cos'è TaskFlow?

### Contenuto:
**TaskFlow è un'applicazione web per la gestione di progetti e task**

✅ **Obiettivi:**
- Organizzare progetti in modo efficiente
- Tracciare lo stato dei task
- Visualizzare i progressi
- Interfaccia semplice e intuitiva

🎯 **Target:**
- Studenti, professionisti, team di lavoro
- Chiunque abbia bisogno di organizzare il proprio lavoro

---

## SLIDE 3 - Tecnologie Utilizzate
**Titolo:** Stack Tecnologico

### Contenuto:
**Backend:**
- 🐍 **Python 3** - Linguaggio di programmazione
- 🌶️ **Flask** - Framework web minimalista
- 📊 **CSV** - Storage dati semplice e portabile

**Frontend:**
- 📝 **HTML5** - Struttura delle pagine
- 🎨 **CSS3** - Styling e responsive design
- 🔧 **Jinja2** - Template engine di Flask
- ⚛️ **React** - Dashboard interattiva

**API:**
- 🔌 **REST API** - Endpoints JSON per accesso ai dati

---

## SLIDE 4 - Architettura del Progetto
**Titolo:** Struttura dell'Applicazione

### Contenuto:
```
TaskFlow/
├── app.py                  # Backend Flask (270 righe)
├── requirements.txt        # Dipendenze
├── static/
│   ├── data/              # Database CSV
│   │   ├── projects.csv   # Progetti
│   │   └── tasks.csv      # Task
│   └── css/
│       └── style.css      # Stili (700+ righe)
└── templates/             # Template Jinja2
    ├── base.html          # Template base
    ├── index.html         # Homepage
    ├── project_detail.html
    ├── create_project.html
    ├── create_task.html
    └── dashboard.html     # React Dashboard
```

**Pattern:** MVC (Model-View-Controller)

---

## SLIDE 5 - Pagine dell'Applicazione (1/2)
**Titolo:** Le 5 Pagine Principali

### Contenuto:
**1. Homepage** (`/`)
- Lista di tutti i progetti
- Statistiche per ogni progetto
- Progress bar completamento
- Bottone "Nuovo Progetto"

**2. Dettaglio Progetto** (`/project/<id>`)
- Visualizza tutti i task del progetto
- Badge per status e priorità
- Azioni rapide (Inizia, Completa)
- Bottone "Nuovo Task"

**Screenshot:** Mostra la homepage con i 3 progetti

---

## SLIDE 6 - Pagine dell'Applicazione (2/2)
**Titolo:** Le 5 Pagine Principali (continua)

### Contenuto:
**3. Nuovo Progetto** (`/create-project`)
- Form con nome, descrizione
- Selezione colore personalizzato
- Validazione input

**4. Nuovo Task** (`/create-task/<project_id>`)
- Form completo per task
- Status: Da Fare / In Corso / Completato
- Priorità: Bassa / Media / Alta

**5. Dashboard React** (`/dashboard`)
- Statistiche generali
- Kanban board interattiva
- Dati caricati via API REST

**Screenshot:** Mostra la dashboard con Kanban board

---

## SLIDE 7 - Funzionalità CRUD
**Titolo:** Operazioni CRUD Complete

### Contenuto:
**PROGETTI:**
- ✅ **CREATE** - Form di creazione con validazione
- ✅ **READ** - Lista progetti e dettaglio singolo
- ✅ **UPDATE** - Modifica status task associati
- ✅ **DELETE** - Eliminazione progetto e task collegati

**TASK:**
- ✅ **CREATE** - Form con tutti i campi
- ✅ **READ** - Visualizzazione lista task
- ✅ **UPDATE** - Cambio status (Da Fare → In Corso → Completato)
- ✅ **DELETE** - Eliminazione task

**Storage:** Dati salvati in file CSV persistenti

---

## SLIDE 8 - API REST
**Titolo:** API REST in formato JSON

### Contenuto:
**3 Endpoint Disponibili:**

1. **GET** `/api/projects`
   - Restituisce tutti i progetti
   - Formato JSON

2. **GET** `/api/tasks`
   - Restituisce tutti i task
   - Formato JSON

3. **GET** `/api/projects/<id>/tasks`
   - Restituisce i task di un progetto specifico
   - Formato JSON filtrato

**Utilizzo:** Dashboard React consuma queste API per visualizzare i dati

**Demo:** Mostrare nel browser `/api/projects`

---

## SLIDE 9 - Dashboard React
**Titolo:** Dashboard Interattiva con React

### Contenuto:
**Componenti:**
- 📊 **Statistiche Generali**
  - Progetti totali
  - Task totali
  - Task completati
  - Percentuale completamento

- 📋 **Kanban Board**
  - 3 colonne: Da Fare, In Corso, Completati
  - Card colorate per progetto
  - Badge priorità
  - Aggiornamento real-time

**Tecnologia:** React 18 con Hooks (useState, useEffect)

**Screenshot:** Dashboard completa con statistiche e Kanban

---

## SLIDE 10 - Design e UX
**Titolo:** Design Moderno e Responsive

### Contenuto:
**Caratteristiche del Design:**
- 🎨 **Colori personalizzabili** per progetti
- 📱 **Responsive Design** - Funziona su mobile, tablet, desktop
- ⚡ **Animazioni fluide** e transizioni
- 🎯 **UI intuitiva** - Facile da usare
- 🏷️ **Badge visivi** per status e priorità
- 📊 **Progress bar** per visualizzare completamento

**CSS:**
- 700+ righe di CSS personalizzato
- Variabili CSS per consistenza
- Grid Layout per responsività
- Hover effects e feedback visivi

**Screenshot:** Mostra versione desktop e mobile

---

## SLIDE 11 - Storage Dati
**Titolo:** Gestione Dati con CSV

### Contenuto:
**Format progetti.csv:**
```csv
id,name,description,color,created_at
1,Sito Web,Descrizione,#3b82f6,2024-01-15T10:00:00
```

**Format tasks.csv:**
```csv
id,project_id,title,description,status,priority,created_at
1,1,Task 1,Descrizione,todo,high,2024-01-16T10:00:00
```

**Vantaggi:**
- ✅ Nessun database esterno necessario
- ✅ Dati human-readable
- ✅ Facile backup e modifica
- ✅ Portabilità massima

---

## SLIDE 12 - Requisiti Tesina Soddisfatti
**Titolo:** Conformità ai Requisiti

### Contenuto:
| Requisito | Status | Implementazione |
|-----------|--------|-----------------|
| **Almeno 4 pagine** | ✅ | 5 pagine HTML |
| **Template** | ✅ | Jinja2 con ereditarietà |
| **CSS** | ✅ | 700+ righe responsive |
| **JavaScript** | ✅ | React Dashboard |
| **API** | ✅ | 3 endpoint REST JSON |
| **CRUD** | ✅ | Completo per progetti e task |
| **Codice funzionante** | ✅ | Testato e operativo |

**Bonus:**
- Dashboard interattiva React
- Design professionale
- Documentazione completa

---

## SLIDE 13 - Demo Live
**Titolo:** Dimostrazione Pratica

### Contenuto da mostrare:
1. **Homepage** - Mostra i 3 progetti
2. **Crea Progetto** - Aggiungi un nuovo progetto con colore
3. **Visualizza Progetto** - Apri un progetto e mostra i task
4. **Crea Task** - Aggiungi un nuovo task
5. **Cambia Status** - Clicca "Inizia" e poi "Completa"
6. **Dashboard** - Mostra statistiche e Kanban
7. **API** - Apri `/api/projects` nel browser
8. **Responsive** - Riduci la finestra per mostrare mobile view

**Tempo stimato:** 3-5 minuti

---

## SLIDE 14 - Sfide e Soluzioni
**Titolo:** Problemi Affrontati e Risolti

### Contenuto:
**Sfida 1: Conflitto Jinja2/React**
- **Problema:** Entrambi usano `{{ }}`
- **Soluzione:** Tag `{% raw %}` per isolare codice React

**Sfida 2: Gestione State CSV**
- **Problema:** Lettura/scrittura concorrente
- **Soluzione:** File CSV separati, operazioni atomiche

**Sfida 3: Responsive Design**
- **Problema:** Layout complesso su mobile
- **Soluzione:** CSS Grid, media queries, mobile-first

**Sfida 4: CRUD senza DB**
- **Problema:** Persistenza dati senza database
- **Soluzione:** File CSV come storage semplice ma efficace

---

## SLIDE 15 - Possibili Estensioni Future
**Titolo:** Roadmap e Miglioramenti

### Contenuto:
**Funzionalità Future:**
- 🔍 **Ricerca e Filtri** avanzati per task
- 📅 **Date di scadenza** con notifiche
- ✏️ **Modifica inline** di progetti e task
- 🎨 **Temi** personalizzabili (dark mode)
- 📊 **Grafici** con Chart.js
- 🔄 **Drag & Drop** per riordinare task
- 👥 **Multi-utente** con autenticazione
- 📤 **Export** PDF/Excel dei progetti
- 📱 **Progressive Web App** per uso offline
- 🔔 **Notifiche** push per scadenze

---

## SLIDE 16 - Codice Significativo (1/2)
**Titolo:** Snippet di Codice - Backend Flask

### Contenuto:
**Esempio: Route per creare un progetto**
```python
@app.route('/create-project', methods=['POST'])
def create_project():
    name = request.form.get('name')
    description = request.form.get('description', '')
    color = request.form.get('color', '#3b82f6')

    # Genera nuovo ID
    projects = get_projects()
    new_id = str(max([int(p['id']) for p in projects]) + 1)

    # Salva nel CSV
    csv_path = os.path.join('static', 'data', 'projects.csv')
    with open(csv_path, 'a', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow([new_id, name, description, color,
                        datetime.now().isoformat()])

    return redirect(url_for('index'))
```

---

## SLIDE 17 - Codice Significativo (2/2)
**Titolo:** Snippet di Codice - Frontend React

### Contenuto:
**Esempio: Componente Kanban con React**
```javascript
function KanbanBoard() {
    const [tasks, setTasks] = useState([]);

    useEffect(() => {
        fetch('/api/tasks')
            .then(res => res.json())
            .then(data => setTasks(data));
    }, []);

    const todoTasks = tasks.filter(t => t.status === 'todo');
    const inProgressTasks = tasks.filter(t => t.status === 'in_progress');
    const doneTasks = tasks.filter(t => t.status === 'done');

    return (
        <div className="kanban-board">
            <KanbanColumn title="Da Fare" tasks={todoTasks} />
            <KanbanColumn title="In Corso" tasks={inProgressTasks} />
            <KanbanColumn title="Completati" tasks={doneTasks} />
        </div>
    );
}
```

---

## SLIDE 18 - Conclusioni
**Titolo:** Cosa Ho Imparato

### Contenuto:
**Competenze Acquisite:**
- ✅ Sviluppo web full-stack con Flask e React
- ✅ Design di API REST
- ✅ Template engine Jinja2
- ✅ CSS avanzato e responsive design
- ✅ Gestione stato con React Hooks
- ✅ Architettura MVC
- ✅ Storage dati con CSV

**Risultato:**
Un'applicazione web completa, funzionante e pronta all'uso che dimostra padronanza delle tecnologie web moderne.

**Tempo di sviluppo:** ~20 ore di lavoro

---

## SLIDE 19 - Ringraziamenti
**Titolo:** Grazie per l'Attenzione

### Contenuto:
```
TaskFlow - Task & Project Manager

Tesina Tecnologie Web
UNIMORE - 2026

Colince Tcheussieu Mendji

---

Repository: [Link se pubblicato su GitHub]
Demo Live: http://127.0.0.1:5000

Grazie per l'attenzione!
Domande?
```

**Suggerimenti grafici:**
- QR code per repository GitHub (se disponibile)
- Logo TaskFlow
- Info contatto

---

## SLIDE BONUS - Screenshot Raccolta
**Suggerimenti per screenshot da includere:**

1. **Homepage** - Vista desktop con 3 progetti
2. **Dettaglio Progetto** - Lista task con badge colorati
3. **Form Nuovo Progetto** - Color picker visibile
4. **Dashboard React** - Statistiche + Kanban completo
5. **Mobile View** - Versione responsive su smartphone
6. **API Response** - Browser con JSON visualizzato
7. **Kanban Close-up** - Dettaglio delle card task
8. **Progress Bars** - Progetti con diverse percentuali

---

## NOTE PER LA PRESENTAZIONE ORALE

**Durata suggerita:** 10-15 minuti

**Scaletta:**
1. Introduzione (1 min) - Cos'è TaskFlow
2. Tecnologie (2 min) - Stack utilizzato
3. Demo Live (5 min) - Mostra funzionalità principali
4. Codice (2 min) - Spiega snippet interessanti
5. Conclusioni (1 min) - Cosa hai imparato

**Consigli:**
- Prepara l'app già aperta nel browser
- Testa tutto prima della presentazione
- Prepara alcuni progetti/task di esempio interessanti
- Mostra sia versione desktop che mobile
- Evidenzia le parti più innovative (React, API)

**Possibili Domande:**
- Perché hai scelto CSV invece di un database?
- Come gestisci la concorrenza nelle scritture?
- Perché Flask invece di Django?
- Come funziona l'integrazione React?
- Hai testato su browser diversi?

---

## CHECKLIST PRESENTAZIONE

Prima della presentazione, verifica:
- [ ] Server Flask funzionante
- [ ] Browser aperto su homepage
- [ ] Dati di esempio carini e significativi
- [ ] Screenshot pronti e di qualità
- [ ] Connessione internet (per CDN React)
- [ ] PowerPoint salvato e testato
- [ ] Backup del progetto
- [ ] Note per la presentazione orale

Buona fortuna! 🚀
