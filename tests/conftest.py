# tests/conftest.py
# Version améliorée avec diagnostic automatique

import pytest
from fastapi.testclient import TestClient
from unittest.mock import patch, MagicMock
import sys


@pytest.fixture
def client():
    """Client de test FastAPI"""
    from app.main import app
    return TestClient(app)


@pytest.fixture
def admin_token():
    """Token JWT admin valide pour les tests"""
    from app.auth.auth_utils import create_access_token
    return create_access_token({"sub": "admin@test.com", "role": "admin"})


@pytest.fixture
def invalid_token():
    """Token JWT invalide pour les tests"""
    return "invalid.token.here"


@pytest.fixture
def mock_admin_data():
    """Données d'admin pour les tests"""
    from app.auth.auth_utils import hash_password
    return {
        "admin_id": 1,
        "email": "admin@test.com",
        "password_hash": hash_password("password123")
    }


@pytest.fixture
def mock_category_data():
    """Données de catégorie pour les tests"""
    return {
        "category_id": 1,
        "name": "Électronique",
        "description": "Produits électroniques",
        "slug": "electronique"
    }


@pytest.fixture
def mock_product_data():
    """Données de produit pour les tests"""
    return {
        "product_id": 1,
        "name": "Laptop",
        "description": "Un ordinateur portable",
        "price": 999.99,
        "stock": 10,
        "sku": "LAP-001"
    }


# ============================================================
# ALTERNATIVE MANUELLE SI L'AUTO-DÉTECTION NE FONCTIONNE PAS
# ============================================================

# Si les tests ne fonctionnent toujours pas, décommentez et utilisez
# cette version manuelle en commentant la version auto ci-dessus


@pytest.fixture(autouse=True)
def mock_execute_query():
    # REMPLACEZ CES CHEMINS PAR VOS CHEMINS RÉELS !
    # Pour les trouver, faites: grep -r "from.*import execute_query" app/
    
    with patch("app.crud.product_routes.execute_query") as mock_prod, \
         patch("app.crud.category_routes.execute_query") as mock_cat, \
         patch("app.crud.admin_routes.execute_query") as mock_admin:
        
        mock_prod.return_value = []
        mock_cat.return_value = []
        mock_admin.return_value = []
        
        yield {
            "products": mock_prod,
            "categories": mock_cat,
            "admin": mock_admin
        }