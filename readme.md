# Complete Lijst van Design Patterns

Design patterns worden onderverdeeld in drie hoofdcategorieën: Creational, Structural en Behavioral patterns.

## Creational Patterns (Creatie)
*Patterns die object creatie mechanismen behandelen*

### 1. **Singleton**
Zorgt ervoor dat een klasse slechts één instantie heeft en biedt een globaal toegangspunt.

**Gebruik:** Database connecties, configuratie managers, loggers

### 2. **Factory Method**
Definieert een interface voor het creëren van objecten, maar laat subklassen beslissen welke klasse te instantiëren.

**Gebruik:** Wanneer de exacte types en afhankelijkheden van objecten vooraf niet bekend zijn

### 3. **Abstract Factory**
Biedt een interface voor het creëren van families van gerelateerde objecten zonder hun concrete klassen te specificeren.

**Gebruik:** UI toolkits, cross-platform applicaties

### 4. **Builder**
Scheidt de constructie van een complex object van zijn representatie, zodat hetzelfde constructieproces verschillende representaties kan creëren.

**Gebruik:** Complexe objecten met veel configuratie opties (bijv. HTML builders, query builders)

### 5. **Prototype**
Specificeert de soorten objecten die gecreëerd moeten worden door een prototype instantie te gebruiken en creëert nieuwe objecten door dit prototype te kopiëren.

**Gebruik:** Wanneer object creatie duur is en objecten vergelijkbaar zijn

### 6. **Object Pool**
Hergebruikt objecten die duur zijn om te creëren in plaats van ze telkens opnieuw aan te maken.

**Gebruik:** Database connecties, thread pools

---

## Structural Patterns (Structuur)
*Patterns die betrekking hebben op klasse en object compositie*

### 7. **Adapter (Wrapper)**
Converteert de interface van een klasse naar een andere interface die clients verwachten.

**Gebruik:** Legacy code integratie, third-party libraries

### 8. **Bridge**
Scheidt een abstractie van zijn implementatie zodat beide onafhankelijk kunnen variëren.

**Gebruik:** Cross-platform UI, device drivers

### 9. **Composite**
Componeert objecten in boomstructuren om part-whole hiërarchieën te representeren.

**Gebruik:** Bestandssystemen, UI component trees, organisatiestructuren

### 10. **Decorator**
Voegt dynamisch verantwoordelijkheden toe aan een object.

**Gebruik:** Uitbreiden van functionaliteit zonder subclassing

### 11. **Facade**
Biedt een uniforme interface naar een set van interfaces in een subsysteem.

**Gebruik:** Vereenvoudigen van complexe systemen, library wrappers

### 12. **Flyweight**
Gebruikt delen om efficiënt grote aantallen fijnmazige objecten te ondersteunen.

**Gebruik:** Text editors (karakters), game development (sprites)

### 13. **Proxy**
Biedt een surrogaat of placeholder voor een ander object om toegang ertoe te controleren.

**Gebruik:** Lazy loading, access control, logging, caching

### 14. **Private Class Data**
Beperkt accessor/mutator toegang tot class data.

**Gebruik:** Data encapsulatie en bescherming

---

## Behavioral Patterns (Gedrag)
*Patterns die communicatie tussen objecten behandelen*

### 15. **Chain of Responsibility**
Laat meer dan één object een kans om een verzoek af te handelen door de ontvangende objecten te koppelen.

**Gebruik:** Event handling, middleware, logging frameworks

### 16. **Command**
Kapselt een verzoek in als een object, waardoor je clients kunt parametriseren met verschillende verzoeken.

**Gebruik:** Undo/redo functionaliteit, macro recording, queuing

### 17. **Interpreter**
Definieert een representatie voor een taalgrammatica samen met een interpreter.

**Gebruik:** SQL parsing, expression evaluators, reguliere expressies

### 18. **Iterator**
Biedt een manier om sequentieel toegang te krijgen tot elementen van een aggregaat object.

**Gebruik:** Collections traversal, custom iteration

### 19. **Mediator**
Definieert een object dat encapsuleert hoe een set objecten interageert.

**Gebruik:** GUI dialogs, chat rooms, air traffic control

### 20. **Memento**
Legt de interne toestand van een object vast en externaliseert deze zonder encapsulatie te schenden.

**Gebruik:** Undo mechanismen, save states in games

### 21. **Observer (Publisher-Subscriber)**
Definieert een één-op-veel afhankelijkheid tussen objecten waarbij alle afhankelijke objecten automatisch worden genotificeerd.

**Gebruik:** Event systems, MVC architectuur, real-time notifications

### 22. **State**
Laat een object zijn gedrag veranderen wanneer zijn interne toestand verandert.

**Gebruik:** State machines, workflow engines, game character states

### 23. **Strategy**
Definieert een familie van algoritmen, kapselt ze in en maakt ze uitwisselbaar.

**Gebruik:** Sorting algoritmen, payment methods, compression algorithms

### 24. **Template Method**
Definieert het skelet van een algoritme in een operatie, waarbij sommige stappen aan subklassen worden overgelaten.

**Gebruik:** Frameworks, game AI, data processing pipelines

### 25. **Visitor**
Representeert een operatie die moet worden uitgevoerd op elementen van een objectstructuur.

**Gebruik:** Compilers (AST traversal), reporting, export functionaliteit

### 26. **Null Object**
Biedt een object als surrogaat voor het ontbreken van een object van een bepaald type.

**Gebruik:** Vermijden van null checks, default behavior

---

## Concurrency Patterns
*Patterns specifiek voor multi-threaded programmeren*

### 27. **Active Object**
Ontkoppelt method execution van method invocation voor objecten in verschillende threads.

**Gebruik:** Asynchrone processing, concurrent servers

### 28. **Monitor Object**
Synchroniseert concurrent method execution om ervoor te zorgen dat slechts één method tegelijk actief is.

**Gebruik:** Thread-safe objects, mutual exclusion

### 29. **Half-Sync/Half-Async**
Ontkoppelt asynchrone en synchrone service processing in concurrent systems.

**Gebruik:** Network servers, I/O frameworks

### 30. **Read-Write Lock**
Staat meerdere readers of één writer toe voor een gedeelde resource.

**Gebruik:** Caching, database access

### 31. **Thread Pool**
Creëert een aantal threads bij het starten die wachten op en taken uitvoeren.

**Gebruik:** Web servers, task executors

---

## Architectural Patterns
*Patterns voor systeem architectuur*

### 32. **Model-View-Controller (MVC)**
Scheidt applicatie logica, presentatie en user input.

**Gebruik:** Web frameworks, desktop applicaties

### 33. **Model-View-ViewModel (MVVM)**
Verbetert MVC door view logic te scheiden in een ViewModel.

**Gebruik:** Modern UI frameworks (WPF, Angular)

### 34. **Model-View-Presenter (MVP)**
Variant van MVC waarbij de Presenter alle presentatie logica afhandelt.

**Gebruik:** GUI applicaties, testing-friendly architectuur

### 35. **Dependency Injection**
Injecteert afhankelijkheden in een object in plaats van dat het object ze zelf creëert.

**Gebruik:** Loose coupling, testability, frameworks

### 36. **Repository**
Medieert tussen domain en data mapping layers met een collectie-achtige interface.

**Gebruik:** Data access layer, ORM abstraction

### 37. **Service Locator**
Kapselt processen in voor het verkrijgen van een service met een sterke abstractie laag.

**Gebruik:** Service discovery, plugin architectures

---

## Enterprise Patterns
*Patterns voor enterprise applicaties*

### 38. **Data Transfer Object (DTO)**
Object dat data draagt tussen processen om het aantal method calls te verminderen.

**Gebruik:** Remote facades, API responses

### 39. **Unit of Work**
Houdt een lijst bij van objecten die zijn gewijzigd door een business transactie.

**Gebruik:** ORM frameworks, transactie management

### 40. **Identity Map**
Zorgt ervoor dat elk object slechts één keer wordt geladen door alle geladen objecten in een map te houden.

**Gebruik:** ORM, caching

### 41. **Lazy Load**
Object dat niet alle data bevat maar weet hoe het te verkrijgen wanneer nodig.

**Gebruik:** Performance optimalisatie, database queries

---

## Anti-Patterns (Wat te vermijden)

### Veelvoorkomende Anti-Patterns:

- **God Object** - Een object dat te veel weet of te veel doet
- **Spaghetti Code** - Code met complexe en verwarde structuur
- **Golden Hammer** - Één oplossing gebruiken voor alle problemen
- **Lava Flow** - Dead code die niemand durft te verwijderen
- **Copy-Paste Programming** - Code duplicatie zonder refactoring
- **Magic Numbers** - Hard-coded waarden zonder betekenis
- **Premature Optimization** - Optimaliseren voordat het nodig is

---

## Pattern Selectie Guide

### Bij object creatie problemen:
- **Singleton** - Eén instantie nodig
- **Factory Method** - Flexibele object creatie
- **Abstract Factory** - Families van objecten
- **Builder** - Complexe constructie
- **Prototype** - Klonen van objecten

### Bij structuur problemen:
- **Adapter** - Interface incompatibiliteit
- **Facade** - Vereenvoudig complex systeem
- **Decorator** - Dynamisch gedrag toevoegen
- **Composite** - Tree structuren
- **Proxy** - Gecontroleerde toegang

### Bij gedrags problemen:
- **Observer** - Event notifications
- **Strategy** - Uitwisselbare algoritmen
- **Command** - Parametriseer operaties
- **State** - Object gedrag per state
- **Template Method** - Algoritme skelet

---

## Bronnen en Verder Lezen

**Klassieke boeken:**
- "Design Patterns: Elements of Reusable Object-Oriented Software" (Gang of Four)
- "Head First Design Patterns" by Freeman & Freeman
- "Patterns of Enterprise Application Architecture" by Martin Fowler

**Online resources:**
- Refactoring.Guru
- SourceMaking.com
- Python Design Patterns Guide

---

## Conclusie

Design patterns zijn herbruikbare oplossingen voor veelvoorkomende problemen in software design. Ze zijn geen finished designs die direct kunnen worden omgezet naar code, maar templates die beschrijven hoe een probleem kan worden opgelost in verschillende situaties.

**Belangrijkste punten:**
- Gebruik patterns om code maintainable en flexibel te houden
- Ken de patterns maar pas ze alleen toe waar nodig
- Over-engineering vermijden - niet elk probleem heeft een pattern nodig
- Patterns zijn taal-agnostisch maar implementaties variëren per taal