from jwt_generator import generate_jwt_token
import jwt


def test_jwt_generation():
    """Test the JWT token generation"""
    
    # Your secret key (keep this secure in real applications!)
    secret_key = ""
    
    print("=== JWT Token Generator Test ===")
    print(f"Using secret key: {secret_key}")
    print()
    
    # Generate a token
    token = generate_jwt_token(secret_key)
    print(f"Generated token: {token}")
    print()
    
    # Decode and verify the token
    try:
        decoded = jwt.decode(token, secret_key, algorithms=['HS256'])
        print("Token decoded successfully!")
        print(f"Payload: {decoded}")
        print()
        
        # Show human-readable timestamps
        import datetime
        issued_at = datetime.datetime.fromtimestamp(decoded['iat'])
        expires_at = datetime.datetime.fromtimestamp(decoded['exp'])
        
        print(f"Issued at: {issued_at}")
        print(f"Expires at: {expires_at}")
        
    except jwt.ExpiredSignatureError:
        print("❌ Token has expired")
    except jwt.InvalidTokenError as e:
        print(f"❌ Invalid token: {e}")


if __name__ == "__main__":
    test_jwt_generation()