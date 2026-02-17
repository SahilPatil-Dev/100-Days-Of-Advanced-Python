# User Management API Design

---

## Base URL

/api/v1

---

## 1. GET /users

### Description
Retrieve a list of users.

### Success Response (200 OK)

{
  "success": true,
  "data": [
    {
      "id": 1,
      "email": "user@example.com",
      "age": 25
    }
  ],
  "message": ""
}

### Error Response (500 Internal Server Error)

{
  "success": false,
  "error": "Internal server error"
}

---

## 2. GET /users/{id}

### Description
Retrieve a specific user by ID.

### Success Response (200 OK)

{
  "success": true,
  "data": {
    "id": 1,
    "email": "user@example.com",
    "age": 25
  },
  "message": ""
}

### Error Responses

404 Not Found

{
  "success": false,
  "error": "User not found"
}

400 Bad Request

{
  "success": false,
  "error": "Invalid user ID"
}

---

## 3. POST /users

### Description
Create a new user.

### Request Body

{
  "email": "new@example.com",
  "age": 22
}

### Success Response (201 Created)

{
  "success": true,
  "data": {
    "id": 10,
    "email": "new@example.com",
    "age": 22
  },
  "message": "User created successfully"
}

### Error Responses

400 Bad Request

{
  "success": false,
  "error": "Invalid input data"
}

---

## 4. PUT /users/{id}

### Description
Update an existing user.

### Request Body

{
  "email": "updated@example.com",
  "age": 30
}

### Success Response (200 OK)

{
  "success": true,
  "data": {
    "id": 1,
    "email": "updated@example.com",
    "age": 30
  },
  "message": "User updated successfully"
}

### Error Responses

404 Not Found
400 Bad Request

---

## 5. DELETE /users/{id}

### Description
Delete a user.

### Success Response (200 OK)

{
  "success": true,
  "data": null,
  "message": "User deleted successfully"
}

### Error Response

404 Not Found

{
  "success": false,
  "error": "User not found"
}
