# Akademize Hero Enroll Python Flask App

This application provides APIs to make CRUD operations for
Hero Enroll Service.

This implementation writes the data to src/data/heros.json

## Prerequisites

- Python >= 3.7

## Env Setup

```bash
./setup.sh
```

## Start the application

```bash
$ ./start.sh
 * Serving Flask app "app"
 * Forcing debug mode on
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 914-428-710
```

## APIs

### Get All Heros

```bash
curl -X GET "http://127.0.0.1:5000/heros" -H "accept: application/json"
```

```json
{
    "success": true,
    "data": [
        {
            "id": "1",
            "name": "Super Man",
            "alter_ego": "Clark"
        },
        {
            "id": "2",
            "name": "Bat Man",
            "alter_ego": "Bruce Wayne"
        }
    ]
}
```

### Get Hero with Id

```bash
curl -X GET "http://127.0.0.1:5000/hero/2" -H "accept: application/json"
```

```json
{
  "success": true,
  "data": {
    "id": "2",
    "name": "Bat Man",
    "alter_ego": "Bruce Wayne"
  }
}
```

### Create a Hero

```bash
curl -X POST "http://127.0.0.1:5000/create-hero" -H "accept: application/json" -H "Content-Type: application/json" -d "{ \"name\": \"Ravan\", \"alter_ego\": \"Sravan\"}"
```

```json
{
  "success": true,
  "data": {
    "id": "45cd4c21-2a2f-4cfa-aecf-7e356f43418d",
    "name": "Ravan",
    "alter_ego": "Sravan"
  }
}
```

### Delete a Hero

```bash
curl -X POST "http://127.0.0.1:5000/delete-hero/1" -H "accept: application/json"
```

```json
{
  "success": true,
  "message": "The requested here is removed successfully."
}
```

### Update a hero

```bash
curl -X POST "http://127.0.0.1:5000/update-hero" -H "accept: application/json" -H "Content-Type: application/json" -d "{ \"id\": \"a543071f-0997-4b61-b54a-bbde555c5c86\", \"name\": \"Wonder Girl\", \"alter_ego\": \"Vikrama Vihari\" }"
```

```json
{
  "success": true,
  "data": {
    "id": "a543071f-0997-4b61-b54a-bbde555c5c86",
    "name": "Wonder Girl",
    "alter_ego": "Vikrama Vihari"
  }
}
```

### Search a Hero

```bash
curl -X GET "http://127.0.0.1:5000/search-hero/vihari" -H "accept: application/json"
```

```json
{
  "success": true,
  "data": {
    "message": "Heros matching the search criteria vihari",
    "heros": [
      {
        "id": "a543071f-0997-4b61-b54a-bbde555c5c86",
        "name": "Wonder Girl",
        "alter_ego": "Vikrama Vihari"
      }
    ]
  }
}
```
