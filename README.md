# 🛒 Sales API – FastAPI & PostgreSQL

---

## 🎯 À propos

API REST pour la gestion d’un système de ventes (**produits, catégories**) construite avec **FastAPI**, **PostgreSQL**, et **Docker**.  
La logique métier est en grande partie gérée côté base de données via des **fonctions PL/pgSQL**.

---

## ✨ Fonctionnalités

- ✅ Gestion complète des **produits** (CRUD)
- ✅ Gestion des **catégories** de produits
- ✅ Authentification et autorisation **admin via JWT**
- ✅ Logique métier centralisée dans **PostgreSQL** (fonctions PL/pgSQL)
- ✅ Documentation interactive auto-générée (Swagger/ReDoc)
- ✅ Déploiement simplifié avec **Docker Compose**
- ✅ Architecture scalable et performante


---

## 🧱 Stack technique

| Couche             | Technologie        |
|--------------------|-------------------|
| **Framework**      | FastAPI           |
| **Base de données**| PostgreSQL 16     |
| **Authentification**| JWT              |
| **Logique DB**     | PL/pgSQL          |
| **Conteneurisation**| Docker & Docker Compose |

---

## 📋 Prérequis

Avant de commencer, assurez-vous d'avoir installé :

- **Docker** ≥ 20.x
- **Docker Compose** ≥ v2
- **Git**

---

## 🚀 Installation

### 1️⃣ Cloner le dépôt

```bash
git clone https://github.com/HamzaMF7/Api_python.git
cd python_app
```

### 2️⃣ Lancer l'environnement

```bash
docker compose up --build -d
```

Cette commande va :
- 🐘 Créer et démarrer le conteneur **PostgreSQL** (`sales_db`)
- ⚡ Créer et démarrer le conteneur **FastAPI**
- 🔧 Exécuter les migrations et initialiser la base de données

### 3️⃣ Vérifier le statut

```bash
docker compose ps
```

---

## 💻 Utilisation

### 🌐 Accès aux services

| Service            | URL                                                        |
|--------------------|------------------------------------------------------------|
| **API**            | http://localhost:8000                                      |
| **Swagger UI**     | http://localhost:8000/docs                                 |
| **ReDoc**          | http://localhost:8000/redoc                                |

### 🔐 Authentification

Pour accéder aux routes protégées, vous devez :

1. **Créer un compte admin** :
   ```bash
   POST /admin/register
   ```

2. **Se connecter** :
   ```bash
   POST /admin/login
   ```

3. **Utiliser le token** dans les requêtes suivantes :
   ```
   Authorization: Bearer <votre_token_jwt>
   ```

---

## 📚 Documentation API

### 🧑‍💼 Administration

| Méthode | Endpoint           | Description              | Auth |
|---------|--------------------|--------------------------|------|
| `POST`  | `/admin/register`  | Créer un compte admin    | ❌   |
| `POST`  | `/admin/login`     | Connexion admin          | ❌   |

### 📦 Produits

| Méthode  | Endpoint             | Description                   | Auth |
|----------|----------------------|-------------------------------|------|
| `GET`    | `/products/{id}`     | Obtenir un produit par ID     | ❌   |
| `GET`    | `/products?name=`    | Rechercher des produits       | ❌   |
| `POST`   | `/products`          | Ajouter un nouveau produit    | ✅   |
| `PUT`    | `/products/{id}`     | Modifier un produit existant  | ✅   |
| `DELETE` | `/products/{id}`     | Supprimer un produit          | ✅   |

### 🗂️ Catégories

| Méthode  | Endpoint              | Description                      | Auth |
|----------|-----------------------|----------------------------------|------|
| `GET`    | `/categories`         | Lister toutes les catégories     | ❌   |
| `GET`    | `/categories/{id}`    | Obtenir une catégorie par ID     | ❌   |
| `POST`   | `/categories`         | Ajouter une nouvelle catégorie   | ✅   |
| `PUT`    | `/categories/{id}`    | Modifier une catégorie existante | ✅   |
| `DELETE` | `/categories/{id}`    | Supprimer une catégorie          | ✅   |

> 🔒 **Auth ✅** = Nécessite un token JWT admin



## 🛠️ Commandes utiles

### Arrêter les services
```bash
docker compose down
```

### Voir les logs
```bash
docker compose logs -f
```

### Reconstruire après modification
```bash
docker compose up --build
```

### Accéder à la base de données
```bash
docker exec -it sales_db psql -U postgres -d sales_db
```

---


## 👨‍💻 Auteur

- [Hamza MAEROF]
- [David CIRAKAZA]
- [Anass HOUDZI]


Lien du projet : [https://github.com/HamzaMF7/Api_python.git]

---

<div align="center">
  <sub>Construit avec ❤️ en utilisant FastAPI et PostgreSQL</sub>
</div>