# ETilang App
A system consists of [ETilang](https://www.etlebanten.info/id/check-data) and ETilang API to check ETilang status.

## Setting Up
1. Clone https://github.com/steffiindrayani/etilang-api.git
2. Fill out environment variable in `.env` file
    ```
    SQLALCHEMY_DATABASE_URI = "postgresql://<username>:<password>@<host>:<port>/<database>"
   ```
3. Install depenedencies
    ```
    pipenv install
    ```
4. Start the server with
    ```
    pipenv run python3 app.py
    ```
5. Server will run in `localhost:8087`

## API

#### POST /api/etilang/check
Example Request
```
{
     "plate_number": "A0000XX",
     "machine_number": "0X00XX000",
     "skeleton_number": "X0XN0000018193"
}
```
Example Response
```
{
    "data": {
        "crawl_timestamp": "2023-05-14T15:44:53.752746",
        "location": "Kota Serang",
        "machine_number": "0X00XX000",
        "offense_timestamp": "1980-01-01T01:01:00",
        "offense_type": "Tidak menggunakan sabuk pengaman",
        "plate_number": "A0000XX",
        "skeleton_number": "X0XN0000018193",
        "status": "Terbayar"
    },
    "message": "ETilang found",
    "status": 200
}
```