# ============================================================
# tests/test_products.py
# ============================================================
"""Tests pour les routes de produits"""

import pytest
from fastapi import status


class TestGetProductById:
    
    def test_get_product_success(self, client, mock_execute_query, mock_product_data):
        """Test de récupération réussie d'un produit"""
        mock_execute_query["products"].return_value = [mock_product_data]
        
        response = client.get("/products/1")
        
        assert response.status_code == status.HTTP_200_OK
        data = response.json()
        assert data["success"] is True
        assert data["data"][0]["product_id"] == 1
    
    def test_get_product_not_found(self, client, mock_execute_query):
        """Test de produit introuvable"""
        mock_execute_query["products"].return_value = [{"product_id": None}]
        
        response = client.get("/products/999")
        
        assert response.status_code == status.HTTP_404_NOT_FOUND


class TestSearchProducts:
    
    def test_search_products_success(self, client, mock_execute_query, mock_product_data):
        """Test de recherche réussie"""
        mock_execute_query["products"].return_value = [mock_product_data]
        
        response = client.get("/products/", params={"name": "Laptop"})
        
        assert response.status_code == status.HTTP_200_OK
        data = response.json()
        assert data["success"] is True
        assert data["count"] == 1


class TestAddProduct:
    
    def test_add_product_success(self, client, mock_execute_query, admin_token):
        """Test d'ajout réussi avec authentification"""
        mock_execute_query["products"].return_value = [{"add_product": 1}]
        
        response = client.post(
            "/products/",
            params={
                "name": "Nouveau Produit",
                "description": "Description",
                "price": 99.99,
                "stock": 10,
                "sku": "PROD-001"
            },
            headers={"Authorization": f"Bearer {admin_token}"}
        )
        
        assert response.status_code == status.HTTP_201_CREATED
    
    def test_add_product_no_auth(self, client):
        """Test d'ajout sans authentification - renvoie 401 car pas de token"""
        response = client.post(
            "/products/",
            params={
                "name": "Test",
                "price": 99.99,
                "sku": "TEST-001"
            }
        )
        
        # HTTPBearer renvoie 401 quand il n'y a pas de token
        assert response.status_code == status.HTTP_401_UNAUTHORIZED
    
    def test_add_product_invalid_price(self, client, admin_token):
        """Test d'ajout avec prix invalide"""
        response = client.post(
            "/products/",
            params={
                "name": "Test",
                "price": -10,
                "sku": "TEST-001"
            },
            headers={"Authorization": f"Bearer {admin_token}"}
        )
        
        assert response.status_code == status.HTTP_400_BAD_REQUEST


class TestUpdateProduct:
    
    def test_update_product_success(self, client, mock_execute_query, admin_token):
        """Test de mise à jour réussie"""
        mock_execute_query["products"].return_value = [{"update_product": True}]
        
        response = client.put(
            "/products/1",
            params={
                "name": "Produit Modifié",
                "description": "Nouvelle description",
                "price": 149.99,
                "stock": 5,
                "sku": "PROD-MOD"
            },
            headers={"Authorization": f"Bearer {admin_token}"}
        )
        
        assert response.status_code == status.HTTP_200_OK
    
    def test_update_product_no_auth(self, client):
        """Test de mise à jour sans authentification - renvoie 401"""
        response = client.put(
            "/products/1",
            params={
                "name": "Test",
                "description": None,
                "price": 99.99,
                "stock": 10,
                "sku": "TEST"
            }
        )
        
        assert response.status_code == status.HTTP_401_UNAUTHORIZED


class TestDeleteProduct:
    
    def test_delete_product_success(self, client, mock_execute_query, admin_token):
        """Test de suppression réussie"""
        mock_execute_query["products"].return_value = [{"delete_product": True}]
        
        response = client.delete(
            "/products/1",
            headers={"Authorization": f"Bearer {admin_token}"}
        )
        
        assert response.status_code == status.HTTP_200_OK
    
    def test_delete_product_no_auth(self, client):
        """Test de suppression sans authentification - renvoie 401"""
        response = client.delete("/products/1")
        
        assert response.status_code == status.HTTP_401_UNAUTHORIZED