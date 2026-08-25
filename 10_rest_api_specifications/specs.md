# Employee Management REST API Cheat Sheet

---

# Common Headers

## Mandatory Headers

| Header | Required | Description |
|---------|----------|-------------|
| Authorization | Yes | Bearer JWT Token |
| Accept | Yes | application/json |
| Content-Type | POST/PATCH Only | application/json |
| Idempotency-Key | POST Only | UUID to prevent duplicate resource creation |
| If-Match | PATCH (Recommended) | ETag/version for optimistic locking |

---

# Standard Success Response

```json
{
  "data": {
    ...
  },
  "metadata": {
    "requestId": "REQ12345",
    "processedTimestamp": "2026-08-25T10:30:45Z"
  }
}
```

---

# Standard Error Response

```json
{
  "error": {
    "errorCode": "EMPLOYEE_NOT_FOUND",
    "errorMessage": "Employee not found.",
    "details": []
  },
  "metadata": {
    "requestId": "REQ12345",
    "processedTimestamp": "2026-08-25T10:30:45Z"
  }
}
```

---

# 1. Create Employee

## Endpoint

```http
POST /api/v1/employees
```

## Headers

```
Authorization: Bearer <JWT>
Content-Type: application/json
Accept: application/json
Idempotency-Key: <UUID>
```

## Request

```json
{
  "data": [
    {
      "employeeName": "John Doe",
      "employeeDob": "1995-05-20",
      "department": "Engineering",
      "designation": "Software Engineer",
      "email": "john@example.com"
    }
  ]
}
```

## Success Response

**HTTP 201 Created**

```json
{
  "data": [
    {
      "employeeId": 101,
      "status": "CREATED"
    }
  ],
  "metadata": {
    "requestId": "REQ123",
    "processedTimestamp": "2026-08-25T10:15:00Z"
  }
}
```

## HTTP Status Codes

| Code | Meaning |
|------|---------|
|201|Created|
|400|Bad Request|
|401|Unauthorized|
|403|Forbidden|
|409|Conflict (Duplicate)|
|422|Validation Failure (Optional)|
|429|Too Many Requests|
|500|Internal Server Error|
|503|Service Unavailable|

---

# 2. Get Employee

## Endpoint

```http
GET /api/v1/employees/{employeeId}
```

## Headers

```
Authorization: Bearer <JWT>
Accept: application/json
```

## Success Response

**HTTP 200 OK**

```json
{
  "data": {
    "employeeId": 101,
    "employeeName": "John Doe",
    "employeeDob": "1995-05-20",
    "department": "Engineering",
    "designation": "Software Engineer",
    "email": "john@example.com"
  },
  "metadata": {
    "requestId": "REQ123",
    "processedTimestamp": "2026-08-25T10:20:00Z"
  }
}
```

## HTTP Status Codes

| Code | Meaning |
|------|---------|
|200|Success|
|400|Bad Request|
|401|Unauthorized|
|403|Forbidden|
|404|Employee Not Found|
|500|Internal Server Error|
|503|Service Unavailable|

---

# 3. Update Employee

## Endpoint

```http
PATCH /api/v1/employees/{employeeId}
```

## Headers

```
Authorization: Bearer <JWT>
Accept: application/json
Content-Type: application/json
If-Match: "v5"      (Recommended)
```

## Request

```json
{
  "data": {
    "employeeName": "John Smith",
    "department": "Platform Engineering"
  }
}
```

## Success Response

**HTTP 200 OK**

```json
{
  "data": {
    "employeeId": 101,
    "employeeName": "John Smith",
    "department": "Platform Engineering"
  },
  "metadata": {
    "requestId": "REQ123",
    "processedTimestamp": "2026-08-25T10:30:00Z"
  }
}
```

## HTTP Status Codes

| Code | Meaning |
|------|---------|
|200|Updated|
|204|Updated (No Content)|
|400|Bad Request|
|401|Unauthorized|
|403|Forbidden|
|404|Not Found|
|409|Version Conflict|
|422|Validation Failure (Optional)|
|500|Internal Server Error|
|503|Service Unavailable|

---

# 4. Delete Employee

## Endpoint

```http
DELETE /api/v1/employees/{employeeId}
```

## Headers

```
Authorization: Bearer <JWT>
Accept: application/json
```

## Success Response

### Option 1 (Preferred)

**HTTP 204 No Content**

No response body.

### Option 2

**HTTP 200 OK**

```json
{
  "data": {
    "employeeId": 101,
    "status": "DELETED"
  },
  "metadata": {
    "requestId": "REQ123",
    "processedTimestamp": "2026-08-25T10:40:00Z"
  }
}
```

## HTTP Status Codes

| Code | Meaning |
|------|---------|
|200|Deleted|
|204|Deleted (No Content)|
|400|Bad Request|
|401|Unauthorized|
|403|Forbidden|
|404|Not Found|
|409|Conflict (Dependent Records)|
|500|Internal Server Error|
|503|Service Unavailable|

---

# 5. List Employees

## Endpoint

```http
GET /api/v1/employees?page=1&size=10&sort=employeeName,asc
```

### Optional Filters

```
department=Engineering
designation=Manager
status=ACTIVE
```

## Headers

```
Authorization: Bearer <JWT>
Accept: application/json
```

## Success Response

**HTTP 200 OK**

```json
{
  "data": [
    {
      "employeeId": 101,
      "employeeName": "John Doe",
      "employeeDob": "1995-05-20"
    },
    {
      "employeeId": 102,
      "employeeName": "Jane Smith",
      "employeeDob": "1993-08-15"
    }
  ],
  "metadata": {
    "requestId": "REQ123",
    "processedTimestamp": "2026-08-25T10:50:00Z",
    "page": 1,
    "size": 10,
    "totalRecords": 200,
    "totalPages": 20,
    "sort": "employeeName,asc",
    "hasNext": true,
    "hasPrevious": false
  }
}
```

## HTTP Status Codes

| Code | Meaning |
|------|---------|
|200|Success (including empty result set)|
|400|Bad Request|
|401|Unauthorized|
|403|Forbidden|
|429|Too Many Requests|
|500|Internal Server Error|
|503|Service Unavailable|

---

# HTTP Status Code Cheat Sheet

| Status | When to Use |
|---------|-------------|
|200 OK|Successful GET, PATCH, DELETE (with response body)|
|201 Created|Resource successfully created|
|202 Accepted|Asynchronous processing started|
|204 No Content|Successful DELETE or UPDATE without response body|
|400 Bad Request|Malformed request, missing fields, invalid data types|
|401 Unauthorized|Missing/invalid authentication|
|403 Forbidden|Authenticated but not authorized|
|404 Not Found|Requested employee does not exist|
|409 Conflict|Duplicate resource, optimistic locking failure, business conflict|
|422 Unprocessable Entity|Business/validation rule violation (if adopted)|
|429 Too Many Requests|Rate limit exceeded|
|500 Internal Server Error|Unexpected server error|
|502 Bad Gateway|Downstream dependency failure|
|503 Service Unavailable|Service unavailable or under maintenance|

---

# REST API Best Practices

- Use nouns in URIs (`/employees`), not verbs.
- Use HTTP methods to express the action (`GET`, `POST`, `PATCH`, `DELETE`).
- Keep JSON naming consistent (prefer camelCase or snake_case throughout).
- Use a consistent response envelope (`data`, `metadata`, `error`).
- Use `Idempotency-Key` only for create/retry-sensitive operations.
- Use `If-Match` (ETag/version) for optimistic concurrency on updates.
- Return `200 OK` with an empty array for empty collection queries rather than `404`.
- Support filtering, sorting, and pagination through query parameters.
- Include machine-readable `errorCode` values in error responses.