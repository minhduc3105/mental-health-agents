"""
Test script to verify database connections
Run: python test_connection.py
"""

import sys

def test_qdrant():
    """Test Qdrant connection"""
    try:
        from qdrant_client import QdrantClient
        client = QdrantClient(host="localhost", port=6333)
        info = client.get_collections()
        print("✓ Qdrant connected successfully!")
        print(f"  Collections: {len(info.collections)}")
        return True
    except Exception as e:
        print(f"✗ Qdrant connection failed: {e}")
        return False

def test_postgres():
    """Test PostgreSQL connection"""
    try:
        import psycopg2
        conn = psycopg2.connect(
            host="localhost",
            port=5432,
            user="mental_health",
            password="mental_health_pass",
            dbname="mental_health_db"
        )
        conn.close()
        print("✓ PostgreSQL connected successfully!")
        return True
    except Exception as e:
        print(f"✗ PostgreSQL connection failed: {e}")
        return False

def test_env():
    """Check if .env exists"""
    import os
    from pathlib import Path

    env_file = Path(".env")
    if env_file.exists():
        print("✓ .env file exists")
        return True
    else:
        print("⚠ .env file not found (copy .env.example to .env)")
        return False

if __name__ == "__main__":
    print("=" * 50)
    print("Testing Database Connections")
    print("=" * 50)

    results = []
    results.append(test_env())
    results.append(test_qdrant())
    results.append(test_postgres())

    print("=" * 50)
    if all(results):
        print("All tests passed! ✓")
    else:
        print("Some tests failed. Check errors above.")
        sys.exit(1)
