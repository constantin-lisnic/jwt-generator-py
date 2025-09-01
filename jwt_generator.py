import jwt
import time


def generate_jwt_token(private_key: str) -> str:
    """
    Generate a JWT token using HMAC-SHA256 signing.
    
    Args:
        private_key (str): The private key used for signing the token
        
    Returns:
        str: The generated JWT token
    """
    # Get current time as Unix timestamp
    current_time = int(time.time())
    
    # Set expiration to 1 hour from now
    expiration_time = current_time + 3600  # 3600 seconds = 1 hour
    
    # Create the payload with claims
    payload = {
        'iat': current_time,  # Issued at
        'exp': expiration_time  # Expiration time
    }
    
    # Generate the JWT token using HMAC-SHA256
    token = jwt.encode(
        payload,
        private_key,
        algorithm='HS256'
    )
    
    return token


# Example usage
if __name__ == "__main__":
    # Example private key (replace with your actual key)
    private_key = ""
    
    # Generate the token
    token = generate_jwt_token(private_key)
    print(f"Generated JWT Token: {token}")
    
    # Optionally decode to verify
    try:
        decoded = jwt.decode(token, private_key, algorithms=['HS256'])
        print(f"Decoded payload: {decoded}")
    except jwt.ExpiredSignatureError:
        print("Token has expired")
    except jwt.InvalidTokenError:
        print("Invalid token")