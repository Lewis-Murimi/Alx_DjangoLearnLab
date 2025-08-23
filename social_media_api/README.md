# Social Media API

A basic Social Media API built with Django and Django REST Framework (DRF) that supports user registration, authentication, and profile management.

## Project Setup

This project uses Django with Django REST Framework and token-based authentication. It includes a custom user model with additional fields like `bio`, `profile_picture`, and `followers`.

---

## Installation

1. **Clone the repository:**
```bash
git clone <repository_url>
cd social_media_api
````
2. **Create a virtual environment(optional):**
```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```
3. **Install the required packages:**
```bash
pip install -r requirements.txt
pip install django djangorestframework djangorestframework-authtoken Pillow
```
## Database Migrations
4. **Apply database migrations:**
```bash
python manage.py makemigrations
python manage.py migrate
```
## Running the Server
5. **Run the development server:**
```bash
python manage.py runserver
```


## Social Media API Documentation

## Base URL
http://127.0.0.1:8000/api/

## 1. Accounts Endpoints

### 1.1 Register User
- **URL:** `/accounts/register/`
- **Method:** `POST`
- **Description:** Registers a new user and returns a token for authentication.
- **Headers:** `Content-Type: application/json`
- **Request Body Example:**
```json
{
  "username": "john_doe",
  "email": "john@example.com",
  "password": "securepassword123",
  "bio": "Hello, I am John!",
  "profile_picture": null
}
```
- **Response Example:**

```json
{
  "user": {
    "id": 1,
    "username": "john_doe",
    "email": "john@example.com",
    "bio": "Hello, I am John!",
    "profile_picture": null,
    "followers": []
  },
  "token": "abc123..."
}
```
### 1.2 Login User
- URL: /accounts/login/
- Method: POST
- Description: Logs in a user and returns a token.
- Headers: Content-Type: application/json
- **Request Body Example:**
```json
{
  "username": "john_doe",
  "password": "securepassword123"
}
```
- **Response Example:**
```json
{
  "user": {
    "id": 1,
    "username": "john_doe",
    "email": "john@example.com",
    "bio": "Hello, I am John!",
    "profile_picture": null,
    "followers": []
  },
  "token": "abc123..."
}
```
### 1.3 Get Profile
- URL: /accounts/profile/
- Method: GET
- Description: Returns the authenticated user's profile.
- Headers: Authorization: Token <token>
- **Response Example:**
```json
{
  "id": 1,
  "username": "john_doe",
  "email": "john@example.com",
  "bio": "Hello, I am John!",
  "profile_picture": null,
  "followers": []
}
```
## 2. Posts Endpoints
### 2.1 List Posts
- URL: /posts/
- Method: GET
- Description: Retrieves a paginated list of all posts. Supports search by title or content.
- Headers: Authorization: Token <token>
- Query Parameters:
  * `search`: Filter posts by keyword in title or content
  * `page`: Page number
  * `page_size`: Number of posts per page

- **Response Example:**
```json
[
  {
    "id": 1,
    "author": 1,
    "author_username": "john_doe",
    "title": "My First Post",
    "content": "This is the content of my first post.",
    "created_at": "2025-08-23T08:00:00Z",
    "updated_at": "2025-08-23T08:00:00Z",
    "comments": []
  }
]
```
### 2.2 Create Post
- URL: `/posts/`
- Method: `POST`
- Description: Creates a new post. Only authenticated users can create posts.
- Headers:
  * `Content-Type`: application/json
  * `Authorization`: Token <token>

- **Request Body Example:**
```json
{
  "title": "My First Post",
  "content": "This is the content of my first post."
}
```
- **Response Example:**
```json
{
  "id": 1,
  "author": 1,
  "author_username": "john_doe",
  "title": "My First Post",
  "content": "This is the content of my first post.",
  "created_at": "2025-08-23T08:00:00Z",
  "updated_at": "2025-08-23T08:00:00Z",
  "comments": []
}
```

### 2.3 Retrieve, Update, Delete Post
- URL: `/posts/<id>/`
- Methods:
  * `GET` → Retrieve a post
  * `PUT` → Update a post (author only)
  * `DELETE` → Delete a post (author only)

- Headers: `Authorization`: Token <token>

- **Update Request Body Example:**
```json
{
  "title": "Updated Post Title",
  "content": "Updated content of the post."
}
```
- **Response Example (`GET`):**
```json
{
  "id": 1,
  "author": 1,
  "author_username": "john_doe",
  "title": "Updated Post Title",
  "content": "Updated content of the post.",
  "created_at": "2025-08-23T08:00:00Z",
  "updated_at": "2025-08-23T08:10:00Z",
  "comments": []
}
```
## 3. Comments Endpoints
### 3.1 List Comments
- URL: `/comments/`
- Method: `GET`
- Description: Retrieves a paginated list of all comments.
- Headers: `Authorization`: Token <token>

- **Response Example:**
```json
[
  {
    "id": 1,
    "post": 1,
    "author": 1,
    "author_username": "john_doe",
    "content": "This is a comment on post 1.",
    "created_at": "2025-08-23T08:05:00Z",
    "updated_at": "2025-08-23T08:05:00Z"
  }
]
```

### 3.2 Create Comment
- URL: `/comments/`
- Method: `POST`
- Description: Adds a comment to a post. Only authenticated users can comment.
- Headers:
  * `Content-Type`: application/json
  * `Authorization`: Token <token>

- **Request Body Example:**
```json
{
  "post": 1,
  "content": "This is a comment on post 1."
}
```
- **Response Example:**
```json
{
  "id": 1,
  "post": 1,
  "author": 1,
  "author_username": "john_doe",
  "content": "This is a comment on post 1.",
  "created_at": "2025-08-23T08:05:00Z",
  "updated_at": "2025-08-23T08:05:00Z"
}
```
### 3.3 Retrieve, Update, Delete Comment
- URL: `/comments/<id>/`
- Methods:
  * `GET` → Retrieve a comment
  * `PUT` → Update a comment (author only)
  * `DELETE` → Delete a comment (author only)
- Headers: `Authorization`: Token <token>

- **Update Request Body Example:**
```json
{
  "content": "Updated comment content."
}
```

## 4. User Follows and Feed Endpoints

### 4.1 Follow a User
- **URL:** `/accounts/follow/<user_id>/`
- **Method:** `POST`
- **Description:** Follow a user by their ID.
- **Headers:** `Authorization: Token <token>`
- **Response Example:**
```json
{
  "detail": "You are now following jane_doe."
}
```
### 4.2 Unfollow a User
- URL: `/accounts/unfollow/<user_id>/`
- Method: `POST`
- Description: Unfollow a user by their ID.
- Headers: `Authorization`: Token <token>
- **Response Example:**
```json
{
  "detail": "You have unfollowed jane_doe."
}
```
### 4.3 User Feed
- URL: `/posts/feed/`
- Method: `GET`
- Description: Retrieves posts from users the authenticated user follows, ordered by newest first.
- Headers: `Authorization`: Token <token>
- **Response Example:**

```json
[
  {
    "id": 5,
    "author": 2,
    "author_username": "jane_doe",
    "title": "Travel Tips",
    "content": "Some useful tips for your next adventure...",
    "created_at": "2025-08-23T12:00:00Z",
    "updated_at": "2025-08-23T12:00:00Z",
    "comments": []
  },
  {
    "id": 3,
    "author": 3,
    "author_username": "mark_smith",
    "title": "Cooking Recipes",
    "content": "My favorite recipe for a quick meal...",
    "created_at": "2025-08-23T11:00:00Z",
    "updated_at": "2025-08-23T11:00:00Z",
    "comments": []
  }
]
```

## Notes
- All endpoints requiring authentication must include the header:
  - `Authorization`: Token <your_token_here>
- Pagination defaults to 10 items per page. Use ?page=<number>&page_size=<number> for custom pagination.
- Posts can be searched by title or content using: ?search=keyword.