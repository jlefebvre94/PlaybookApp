# Idées d'Interface pour Flag Playbook Designer (CustomTkinter)

## 1. Layout Principal de la Fenêtre

### Structure Générale
```
┌─────────────────────────────────────────────────────────────────┐
│ Menu Bar (Fichier, Édition, Affichage, Outils, Aide)          │
├─────────────────────────────────────────────────────────────────┤
│ Toolbar (Outils rapides)                                       │
├──────────────┬─────────────────────────────┬────────────────────┤
│              │                             │                    │
│  Panneau     │        Canvas Terrain       │   Panneau          │
│  Gauche      │       (Zone principale)     │   Droite           │
│  (200px)     │                             │   (250px)          │
│              │                             │                    │
├──────────────┴─────────────────────────────┴────────────────────┤
│ Barre de Statut (Coordonnées, Mode, Infos)                     │
└─────────────────────────────────────────────────────────────────┘
```

## 2. Couleurs et Thème CustomTkinter

### Palette de Couleurs Recommandée
```python
# Thème principal (mode sombre recommandé pour réduire la fatigue)
COLORS = {
    "bg_primary": "#1a1a1a",      # Fond principal
    "bg_secondary": "#2d2d2d",    # Panneaux latéraux
    "bg_tertiary": "#3d3d3d",     # Boutons/widgets
    "accent": "#4a9eff",          # Bleu accent (boutons actifs)
    "success": "#4caf50",         # Vert (joueurs en forme)
    "warning": "#ff9800",         # Orange (fatigués)
    "error": "#f44336",           # Rouge (blessés)
    "text_primary": "#ffffff",    # Texte principal
    "text_secondary": "#b0b0b0",  # Texte secondaire
    "field_green": "#2e7d32",     # Vert terrain
    "field_lines": "#ffffff"      # Lignes blanches
}
```

## 3. Panneau Gauche - Gestion des Éléments

### Section 1: Équipe Active
```
┌─────────────────────┐
│ 🏈 ÉQUIPE ACTIVE    │
├─────────────────────┤
│ ▼ Les Faucons       │ <- Dropdown équipe
│                     │
│ Joueurs (12):       │
│ ┌─ QB Alex (12) 🟢 │ <- État coloré
│ ├─ RB Marc (5)  🟠  │
│ ├─ WR John (88) 🟢  │
│ └─ [+ Nouveau]      │
│                     │
│ [Gérer Équipes]     │
└─────────────────────┘
```

### Section 2: Outils de Dessin
```
┌─────────────────────┐
│ 🔧 OUTILS           │
├─────────────────────┤
│ ○ Sélection         │ <- Radio buttons
│ ○ Placer Joueur     │
│ ○ Tracer Route      │
│ ○ Déplacer Ballon   │
│ ○ Gomme             │
│                     │
│ Grille: ☑ Activée   │ <- Checkbox
│ Magnétisme: ☑ On    │
└─────────────────────┘
```

### Section 3: Tracés Prédéfinis
```
┌─────────────────────┐
│ 📋 ROUTES           │
├─────────────────────┤
│ [Go/Fly]   [Post]   │ <- Boutons 2x2
│ [Slant]    [Out]    │
│ [In]       [Curl]   │
│ [Corner]   [Flat]   │
│                     │
│ Couleur: 🔴🔵🟢🟡   │ <- Sélecteur couleurs
└─────────────────────┘
```

## 4. Canvas Central - Terrain de Jeu

### Spécifications du Canvas
```python
# Dimensions recommandées
CANVAS_WIDTH = 600   # pixels
CANVAS_HEIGHT = 400  # pixels
FIELD_RATIO = 3:2    # Proportion terrain flag football

# Éléments visuels
- Fond vert foncé (#2e7d32)
- Lignes blanches (lignes de scrimmage, zones)
- Grille optionnelle (pointillés gris)
- Coordonnées affichées en temps réel
```

### Légende Visuelle du Terrain
```
  Zone d'en-but adverse
┌─────────────────────────┐
│ ╭─╮ ╭─╮ ╭─╮ ╭─╮ ╭─╮   │  <- Joueurs avec icônes
│ QB  R  W1 W2 W3         │     distinctes par poste
├─────────────────────────┤
│         🏈              │  <- Ballon (position variable)
│    ↗ ↘  ↑  ↗ ↘         │  <- Tracés colorés avec flèches
│                         │
│         ═══             │  <- Ligne de scrimmage
└─────────────────────────┘
  Zone d'en-but équipe
```

## 5. Panneau Droit - Propriétés et Jeux

### Section 1: Jeu Actuel
```
┌─────────────────────────┐
│ 📝 JEU ACTUEL           │
├─────────────────────────┤
│ Nom: [Spread Right]     │ <- Entry field
│ Formation: [Shotgun ▼]  │ <- Dropdown
│ Description:            │
│ ┌─────────────────────┐ │
│ │ Lecture rapide du   │ │ <- Text widget
│ │ safety...           │ │
│ └─────────────────────┘ │
│                         │
│ [💾 Sauvegarder]       │
│ [🗑️ Nouveau Jeu]       │
└─────────────────────────┘
```

### Section 2: Bibliothèque de Jeux
```
┌─────────────────────────┐
│ 📚 MES JEUX             │
├─────────────────────────┤
│ 🔍 [Recherche...]       │
│                         │
│ ▼ Playbook Offense      │ <- TreeView
│   ├─ Spread Right       │   expandable
│   ├─ Double Slant       │
│   └─ Screen Pass        │
│ ▼ Situations Spéciales  │
│   ├─ 4th Down           │
│   └─ Zone Rouge         │
│                         │
│ [📁 Nouveau Playbook]   │
└─────────────────────────┘
```

## 6. Toolbar Principal

### Outils Rapides (avec icônes)
```
[📁 Nouveau] [💾 Sauver] [📂 Ouvrir] | [↶ Undo] [↷ Redo] | [🔍+ Zoom+] [🔍- Zoom-] | [🎨 Couleurs] [⚙️ Options]
```

## 7. Fenêtres Modales Spécialisées

### Gestionnaire d'Équipes
```
┌─────────────────────────────────────────────┐
│ Gestion des Équipes et Joueurs              │
├─────────────────┬───────────────────────────┤
│ ÉQUIPES         │ JOUEURS                   │
│                 │                           │
│ ▼ Les Faucons   │ Nom: [Alex Dupont]       │
│ ▷ Eagles        │ Postes: ☑QB ☑WR □RB     │
│ ▷ Lions         │ État: ○En forme ○Blessé  │
│                 │ N°: [12]                 │
│ [+ Nouvelle]    │                          │
│ [✏️ Modifier]   │ [Ajouter Joueur]         │
│ [🗑️ Supprimer] │ [Modifier] [Supprimer]   │
└─────────────────┴───────────────────────────┤
│                [Fermer]                     │
└─────────────────────────────────────────────┘
```

### Assistant Export
```
┌─────────────────────────────────────────┐
│ Assistant d'Export                      │
├─────────────────────────────────────────┤
│ Type d'export:                          │
│ ○ Image PNG/JPG                         │
│ ○ Document PDF                          │
│ ○ Mode Wristband (4-6 jeux/page)       │
│ ○ Données JSON                          │
│                                         │
│ Jeux à exporter:                        │
│ ☑ Spread Right    ☑ Double Slant       │
│ ☑ Screen Pass     □ 4th Down Special   │
│                                         │
│ Options:                                │
│ ☑ Inclure descriptions                  │
│ ☑ Afficher couleurs                     │
│ ☑ Légende des postes                    │
│                                         │
│        [Aperçu] [Exporter] [Annuler]   │
└─────────────────────────────────────────┘
```

## 8. Interactions et Feedback Utilisateur

### Feedback Visuel
- **Survol**: Bordure colorée sur les éléments survolés
- **Sélection**: Halo lumineux autour de l'élément sélectionné
- **Drag & Drop**: Ombre portée pendant le déplacement
- **Validation**: Flash vert pour les actions réussies
- **Erreur**: Flash rouge + message dans la barre de statut

### Raccourcis Clavier Recommandés
```
Ctrl+N  : Nouveau jeu
Ctrl+S  : Sauvegarder
Ctrl+O  : Ouvrir
Ctrl+Z  : Annuler
Ctrl+Y  : Rétablir
Ctrl+E  : Export
Delete  : Supprimer élément sélectionné
Espace  : Basculer mode sélection/dessin
```

## 9. Responsive Design (Adaptabilité)

### Redimensionnement de Fenêtre
- **Minimum**: 1024x768 pixels
- **Panneaux**: Redimensionnables avec séparateurs
- **Canvas**: Garde ses proportions, zoom automatique si nécessaire
- **Éléments**: Repositionnement intelligent

### États d'Interface
```python
# Modes d'affichage
MODES = {
    "EDIT": "Mode édition complète",
    "VIEW": "Mode visualisation seule", 
    "PRESENT": "Mode présentation (plein écran terrain)"
}
```

## 10. Code d'Exemple CustomTkinter

### Structure de Base
```python
import customtkinter as ctk

class PlaybookApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        # Configuration fenêtre principale
        self.title("Flag Playbook Designer")
        self.geometry("1200x800")
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(1, weight=1)
        
        # Thème
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")
        
        self.create_widgets()
    
    def create_widgets(self):
        # Menu et toolbar
        self.create_menu()
        self.create_toolbar()
        
        # Panneaux principaux
        self.create_left_panel()
        self.create_canvas_area()
        self.create_right_panel()
        
        # Barre de statut
        self.create_status_bar()
```
