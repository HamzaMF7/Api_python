# ============================================================
# tests/test_admin_auth.py
# ============================================================
"""Tests pour les routes d'authentification admin"""

import pytest
from fastapi import status


class TestAdminRegister:
    
    def test_register_success(self, client, mock_execute_query):
        """Test d'inscription réussie"""
        mock_execute_query["admin"].return_value = [{"add_admin": 1}]
        
        response = client.post(
            "/admin/register",
            params={"email": "admin@test.com", "password": "password123"}
        )
        
        assert response.status_code == status.HTTP_201_CREATED
        data = response.json()
        assert data["success"] is True
        assert data["admin_id"] == 1
    
    def test_register_missing_email(self, client):
        """Test d'inscription sans email"""
        response = client.post(
            "/admin/register",
            params={"email": "", "password": "password123"}
        )
        
        assert response.status_code == status.HTTP_400_BAD_REQUEST
    
    def test_register_missing_password(self, client):
        """Test d'inscription sans mot de passe"""
        response = client.post(
            "/admin/register",
            params={"email": "admin@test.com", "password": ""}
        )
        
        assert response.status_code == status.HTTP_400_BAD_REQUEST
    
    def test_register_server_error(self, client, mock_execute_query):
        """Test d'erreur serveur lors de l'inscription"""
        mock_execute_query["admin"].side_effect = Exception("Database error")
        
        response = client.post(
            "/admin/register",
            params={"email": "admin@test.com", "password": "password123"}
        )
        
        assert response.status_code == status.HTTP_500_INTERNAL_SERVER_ERROR


class TestAdminLogin:
    
    def test_login_success(self, client, mock_execute_query, mock_admin_data):
        """Test de connexion réussie"""
        mock_execute_query["admin"].return_value = [mock_admin_data]
        
        response = client.post(
            "/admin/login",
            params={"email": "admin@test.com", "password": "password123"}
        )
        
        assert response.status_code == status.HTTP_200_OK
        data = response.json()
        assert data["success"] is True
        assert "access_token" in data
        assert data["token_type"] == "bearer"
    
    def test_login_admin_not_found(self, client, mock_execute_query):
        """Test de connexion avec email inexistant"""
        mock_execute_query["admin"].return_value = []
        
        response = client.post(
            "/admin/login",
            params={"email": "nonexistent@test.com", "password": "password123"}
        )
        
        assert response.status_code == status.HTTP_404_NOT_FOUND
    
    def test_login_wrong_password(self, client, mock_execute_query):
        """Test de connexion avec mauvais mot de passe"""
        from app.auth.auth_utils import hash_password
        password_hash = hash_password("correctpassword")
        
        mock_execute_query["admin"].return_value = [{
            "admin_id": 1,
            "email": "admin@test.com",
            "password_hash": password_hash
        }]
        
        response = client.post(
            "/admin/login",
            params={"email": "admin@test.com", "password": "wrongpassword"}
        )
        
        assert response.status_code == status.HTTP_400_BAD_REQUEST
    
    def test_login_server_error(self, client, mock_execute_query):
        """Test d'erreur serveur lors de la connexion"""
        mock_execute_query["admin"].side_effect = Exception("Database error")
        
        response = client.post(
            "/admin/login",
            params={"email": "admin@test.com", "password": "password123"}
        )
        
        assert response.status_code == status.HTTP_500_INTERNAL_SERVER_ERROR
