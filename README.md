# Plan Consolidé : Application Playbook Flag Football

## 1. Objectif et Vision du Projet

**Titre** : Flag Playbook Designer (Concepteur de Jeux Flag)

**Objectif Principal** : Développer une application desktop intuitive et visuellement riche permettant aux entraîneurs et joueurs de flag football de créer, visualiser, sauvegarder et gérer des stratégies de jeu (playbooks). L'application incluera une gestion complète des équipes et des joueurs, avec une attention particulière portée à la clarté visuelle et à la facilité d'utilisation.

**Public Cible** : Entraîneurs et joueurs de flag football souhaitant créer, organiser et partager des stratégies de jeu.

## 2. Architecture Technique

**Technologies Principales** :
- **Langage** : Python
- **Interface Graphique** : CustomTkinter (interface moderne et personnalisable)
- **Base de Données** : SQLite (légère, intégrée, parfaite pour une application desktop)
- **Gestion des Données** : JSON pour l'export/import des playbooks

**Structure de la Base de Données** :
- `teams` : Informations sur les équipes
- `players` : Informations détaillées sur les joueurs
- `formations` : Formations prédéfinies
- `plays` : Jeux complets avec positions et tracés
- `playbooks` : Collections de jeux organisés par thème

## 3. Fonctionnalités Principales

### 3.1 Gestion des Équipes et Joueurs

**Gestion des Équipes** :
- Création, modification et suppression d'équipes
- Nom de l'équipe et informations de base
- Visualisation de l'effectif complet

**Gestion des Joueurs** :
- Ajout/modification/suppression de joueurs avec :
  - Nom complet
  - Postes possibles (Center, Quarterback, Running Back, Receiver 1-3)
  - État de forme (En forme, Blessé, Fatigué, Absent)
  - Numéro de maillot (optionnel)
- Filtrage par poste ou état
- Indicateurs visuels colorés pour l'état des joueurs :
  - Vert : "En forme"
  - Orange : "Fatigué" 
  - Rouge : "Blessé"
  - Gris : "Absent"
- Les joueurs peuvent avoir les compétences "Coach" et/ou "referee".

### 3.2 Éditeur de Terrain Interactif (Cœur de l'Application)

**Terrain de Jeu** :
- Représentation visuelle d'un terrain de flag football
- Orientation du bas vers le haut (sens du jeu)
- Lignes de scrimmage, zones d'en-but, marqueurs de distance
- Grille magnétique optionnelle pour l'alignement précis
- Zoom et panoramique pour une meilleure précision

**Position du Ballon** :
- Icône distinctive pour le ballon
- Déplaçable par glisser-déposer
- Magnétisme sur la ligne de scrimmage

**Placement des Joueurs** :
- Icônes distinctes par poste (C, QB, R, W1, W2, etc.)
- Placement via clic ou glisser-déposer
- Assignation des joueurs de l'équipe aux positions
- Couleurs distinctes par joueur et rôle
- Affichage du nom/numéro du joueur assigné

**Création des Tracés** :
- **Tracés manuels** : Dessin libre avec points de contrôle modifiables
- **Patterns prédéfinis** : Bibliothèque de tracés communs
  - Go/Fly, Post, Slant, Out, In, Curl, Corner, Flat, Block
- **Styles de tracés** :
  - Ligne continue (course)
  - Ligne pointillée (option de passe)
  - Flèches directionnelles
  - Épaisseur et couleur personnalisables
- **Couleurs uniques** : Chaque joueur et tracé avec une couleur distinctive
- **Édition avancée** : Modification des points, suppression, duplication

**Outils d'Édition** :
- Sélection/déplacement d'éléments
- Gomme pour suppression
- Annuler/Rétablir (Undo/Redo)
- Détection des collisions de trajets (optionnel)

### 3.3 Gestion des Formations et Jeux

**Formations** :
- Création de formations prédéfinies (Shotgun, Pistol, I-Formation, etc.)
- Positions de base sauvegardables
- Application rapide d'une formation à un nouveau jeu

**Propriétés des Jeux** :
- Nom du jeu (ex: "Spread Right - Double Slants")
- Formation offensive de base
- Description et notes tactiques
- Côté (attaque/défense)
- Catégorisation par situation (Zone Rouge, 3ème down, etc.)

### 3.4 Organisation et Gestion des Playbooks

**Structure Hiérarchique** :
- Organisation des jeux en "Playbooks" thématiques
- Catégories : "Match Dimanche", "Jeux Zone Rouge", "Situations Spéciales"
- Vue d'ensemble avec aperçus compacts

**Sauvegarde et Chargement** :
- Sauvegarde automatique en base SQLite
- Chargement rapide des jeux existants
- Duplication de jeux pour modifications rapides
- Système de versions (optionnel)

### 3.5 Visualisation et Export

**Modes de Visualisation** :
- Vue détaillée pour l'édition
- Vue compacte "Wristband" pour impression
- Prévisualisation claire avec couleurs et tracés

**Fonctions d'Export** :
- **Images** : PNG/JPG haute résolution
- **PDF** : Documents imprimables avec nom et notes
- **Mode Wristband** : Format compact (4-6 jeux par page)
- **JSON** : Export/import pour partage entre utilisateurs
- **Impression** : Optimisée pour formats A4 et Letter

## 4. Interface Utilisateur (CustomTkinter)

### 4.1 Fenêtre Principale
- **Barre de menu** : Fichier, Édition, Affichage, Outils, Aide
- **Toolbar** : Outils de dessin et d'édition rapides
- **Zone centrale** : Canvas du terrain de jeu
- **Panneaux latéraux** :
  - Gestion des joueurs et équipes
  - Propriétés du jeu en cours
  - Bibliothèque de tracés prédéfinis
  - Liste des jeux sauvegardés

### 4.2 Fenêtres Secondaires
- **Gestionnaire d'équipes** : CRUD complet des équipes et joueurs
- **Bibliothèque de formations** : Création et gestion des formations
- **Paramètres** : Configuration de l'application et préférences utilisateur
- **Export/Import** : Assistants pour les différents formats

### 4.3 Principes UX/UI
- **Intuitivité** : Actions naturelles et découvrables
- **Clarté visuelle** : Contraste optimal, icônes claires
- **Feedback immédiat** : Réaction instantanée aux actions
- **Consistance** : Comportements prévisibles
- **Performance** : Fluidité même avec des jeux complexes

## 5. Modèle de Données

### Structure des Entités Principales

```python
# Joueur
{
    "id": "uuid_joueur_1",
    "nom": "Alex Dupont",
    "postesPossibles": ["Quarterback", "Receiver"],
    "etat": "En forme",
    "numeroMaillot": "12",
    "equipeId": "uuid_equipe_1"
}

# Jeu
{
    "id": "uuid_jeu_1",
    "nom": "Shotgun Twins - Slant & Out",
    "formation": "Shotgun",
    "description": "Lecture rapide du safety",
    "positionBallon": {"x": 50, "y": 75},
    "joueursSurTerrain": [
        {
            "idElement": "canvas_qb_1",
            "joueurAssigneId": "uuid_joueur_1",
            "posteSymbol": "QB",
            "positionInitiale": {"x": 50, "y": 70},
            "trace": {
                "type": "manuel",
                "points": [{"x": 50, "y": 70}, {"x": 55, "y": 65}],
                "couleur": "#FF0000",
                "style": "continu"
            }
        }
    ],
    "playbookIds": ["uuid_playbook_1"]
}
```

## 6. Phases de Développement

### Phase 1 : MVP (4 semaines)
- Configuration de l'environnement CustomTkinter
- Base de données SQLite avec tables principales
- Interface de base avec terrain statique
- Placement manuel des joueurs
- Tracés simples manuels
- Sauvegarde/chargement basique

### Phase 2 : Fonctionnalités Avancées (3 semaines)
- Gestion complète des équipes et joueurs
- Patterns de tracés prédéfinis
- Palette de couleurs et styles
- Outils d'édition avancés (undo/redo)
- Formations prédéfinies

### Phase 3 : Visualisation et Export (2 semaines)
- Modes de visualisation multiples
- Export en images et PDF
- Mode Wristband pour impression
- Import/export JSON

### Phase 4 : Perfectionnement et Tests (2 semaines)
- Tests utilisateur et corrections
- Optimisation des performances
- Documentation utilisateur
- Préparation du déploiement

### Phase 5 : Fonctionnalités Avancées (optionnel)
- Animation des jeux
- Statistiques d'utilisation
- Mode défense avec défenseurs
- Synchronisation cloud

## 7. Ressources et Outils

**Équipe de Développement** :
- Développeur Python/CustomTkinter
- Designer UX/UI
- Testeur fonctionnel

**Outils de Développement** :
- Python 3.8+
- CustomTkinter pour l'interface
- SQLite3 pour la base de données
- Pillow pour la manipulation d'images
- ReportLab pour la génération PDF
- Git pour le contrôle de version

## 8. Calendrier Prévisionnel

**Total : 11-13 semaines**
- Conception détaillée : 1 semaine
- Phase 1 (MVP) : 4 semaines
- Phase 2 (Fonctionnalités) : 3 semaines
- Phase 3 (Export/Visualisation) : 2 semaines
- Phase 4 (Tests/Finition) : 2 semaines
- Phase 5 (Optionnel) : 2-3 semaines

## 9. Évolutions Futures Envisagées

- **Mode collaboratif** : Édition partagée en temps réel
- **Analyse statistique** : Suivi de l'efficacité des jeux
- **Simulation animée** : Visualisation du déroulement des jeux
- **Application mobile** : Version companion pour consultation
- **Intelligence artificielle** : Suggestions de jeux basées sur l'historique
- **Intégration vidéo** : Liens vers des vidéos explicatives

## 10. Conclusion

Ce projet représente une solution complète pour la création et gestion de playbooks de flag football. L'architecture modulaire en Python avec CustomTkinter permettra une évolution progressive et une maintenance aisée. L'accent mis sur l'expérience utilisateur et la clarté visuelle garantira une adoption facile par les entraîneurs et joueurs.
