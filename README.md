# fastapi-jwt-auth-server

`fastapi-jwt-auth-server` is a FastAPI-based JWT authentication server that provides user authentication and token issuance functionality. It supports injecting custom user storage logic, making it easy to integrate into different applications.

---

## Features

- **User Authentication**: Validate username and password.
- **JWT Token Generation**: Generate secure JWT tokens based on user information.
- **Custom User Storage**: Support injecting custom user access logic by implementing `AbstractUserStore`.
- **Modular Design**: Clear layered architecture for easy extension and maintenance.

---

## Installation

1. Clone the project to your local machine:
   ```bash
   git clone https://github.com/TY-678/fastapi-jwt-auth-server.git
   cd fastapi-jwt-auth-server
   ```

2. Install dependencies using `poetry`:
   ```bash
   poetry install
   ```

3. Configure environment variables:
   Create a `config.env` file and set the following variables:
   #### Example
   ```env
    secret_key=your-secret-key
    algorithm=HS256
    access_token_expire_minutes=30
    server_host=0.0.0.0
    server_port=7777
    debug=False
   ```
   ### Configuration Variable Descriptions

- **`secret_key`**:
  - The key used to sign and verify JWTs. It must be a secure random string.

- **`algorithm`**:
  - The algorithm used to encrypt JWTs. Default is `HS256`.

- **`access_token_expire_minutes`**:
  - Sets the expiration time for JWTs (in minutes).

- **`server_host`**:
  - The server's host address. Default is `0.0.0.0`.

- **`server_port`**:
  - The server's port number. Default is `7777`.

- **`debug`**:
  - Whether to enable debug mode. Default is `False`.

---

### Why is `secret_key` important?

The `secret_key` is the core of JWT security and is used for:
1. **Signing JWTs**: When generating JWTs, the `secret_key` is used to sign the token, ensuring its integrity.
2. **Verifying JWTs**: When verifying JWTs, the same `secret_key` is used to check if the token has been tampered with.

If the `secret_key` is lost or leaked, attackers can generate valid JWTs, bypassing authentication. Therefore, it is crucial to keep the `secret_key` secure and rotate it regularly.

---

## Quick Start

### Start the Server

1. Ensure the environment variables are correctly set or use the default values.
2. Start the server using `poetry`:
   ```bash
   poetry run python -m fastapi_jwt_auth_server.main
   ```
3. By default, the server will run at `http://127.0.0.1:7777`.

---

### API Routes

#### 1. **Login**
- **Path**: `POST /auth/login`
- **Request Body**:
  ```json
  {
    "username": "your_username",
    "password": "your_password"
  }
  ```
- **Response**:
  - Success:
    ```json
    {
      "access_token": "your_jwt_token"
    }
    ```
  - Failure:
    ```json
    {
      "detail": "Invalid username or password"
    }
    ```

---

## Custom User Data Access

You can define custom user access logic by implementing `AbstractUserStore`. For example:

```python
from fastapi_jwt_auth_server.bo.auth_bo import AbstractUserStore
from typing import Optional

class CustomUserStore(AbstractUserStore):
    FAKE_USER_DB = {
        "alice": {"username": "alice", "password": "secret", "role": "admin"},
        "bob": {"username": "bob", "password": "password", "role": "user"},
    }

    async def get_user(self, username: str) -> Optional[dict]:
        return self.FAKE_USER_DB.get(username)
```

Then inject the custom `UserStore` during initialization:

```python
from fastapi_jwt_auth_server.client.auth_client import AuthServerClient
from example_user_store import CustomUserStore

user_store = CustomUserStore()
auth_client = AuthServerClient(user_store)
```

---

## Project Structure

```plaintext
fastapi-jwt-auth-server/
├── fastapi_jwt_auth_server/
│   ├── bo/
│   │   ├── auth_bo.py
│   ├── config/
│   │   ├── config.py
│   ├── core/
│   │   ├── security.py
│   ├── endpoint/
│   │   ├── auth_router.py
│   ├── schemas/
│   │   ├── auth_schema.py
│   │   ├── env_models.py
│   ├── main.py
├── config.env
├── pyproject.toml
├── README.md
├── CHANGELOG.md

```

---

## Contribution

Feel free to submit Issues or Pull Requests to improve this project!

---

## License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).