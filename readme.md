# MyInfo Integration

This project demonstrates the integration of the Singpass MyInfo API using Django REST Framework. It allows users to retrieve and verify personal information from MyInfo through the Singpass service.

## Features
- OAuth2 authentication with MyInfo.
- Secure retrieval of user data.

## Requirements
- Python 3.7+
- Django 3.2+
- Django REST Framework
- Redis
- Requests

## Installation

1. **Create a virtual environment and activate it**
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

2. **Install dependencies**
   ```sh
   pip install -r requirements.txt
   ```

3. **Set up environment variables**
   Create a `.env` file in the project root and add the following variables:
   ```
   MYINFO_CLIENT_ID=your_client_id
   MYINFO_PURPOSE_ID=your_purpose_id
   MYINFO_PRIVATE_KEY_SIG=your_private_key_sig
   MYINFO_PRIVATE_KEY_ENC=your_private_key_enc
   ```

4. **Run migrations**
   ```sh
   python manage.py migrate
   ```

5. **Run the server**
   ```sh
   python manage.py runserver
   ```

## Usage

### Endpoints
- **GET `/api/myinfo/login/`**: Returns the Singpass login URL for user authentication.
- **POST `/api/myinfo/data/`**: Retrieves user data from MyInfo after successful authentication. This endpoint requires a request body containing `{"auth_code": "your_auth_code"}`. The `auth_code` is provided by MyInfo after user authentication and is used to retrieve user details.

### Testing

1. **Run tests using pytest**
   ```sh
   pytest
   ```

## Running the Tests
The tests are written using `pytest` and mock the MyInfo API calls.
