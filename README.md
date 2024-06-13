# Famous Paintings Database Case Study

This repository contains SQL scripts, data files, and a case study involving a database of famous paintings. The database was created using datasets obtained from Kaggle and stored in PostgreSQL. The case study involves solving several queries to extract meaningful insights from the data.

![Famous Painting](https://m.media-amazon.com/images/I/91zXgqbLCML._AC_UF1000,1000_QL80_.jpg)

## Table Descriptions

### 1. `artists.csv`
This table contains information about the artists.

| Column Name  | Data Type | Description                           |
|--------------|------------|---------------------------------------|
| artist_id    | INT        | Unique identifier for the artist      |
| full_name    | VARCHAR    | Full name of the artist               |
| first_name   | VARCHAR    | First name of the artist              |
| middle_name  | VARCHAR    | Middle name of the artist             |
| last_name    | VARCHAR    | Last name of the artist               |
| nationality  | VARCHAR    | Nationality of the artist             |
| style        | VARCHAR    | Style of painting                     |

### 2. `canvas_size.csv`
This table contains details about the size of the canvas used for the paintings.

| Column Name  | Data Type | Description                           |
|--------------|------------|---------------------------------------|
| size_id      | INT        | Unique identifier for the canvas size |
| width        | FLOAT      | Width of the canvas (in inches)       |
| height       | FLOAT      | Height of the canvas (in inches)      |
| label        | VARCHAR    | Label or description of the size      |

### 3. `image_link.csv`
This table contains URLs linking to images of the paintings.

| Column Name       | Data Type | Description                           |
|-------------------|------------|---------------------------------------|
| work_id           | INT        | Unique identifier for the artwork     |
| url               | VARCHAR    | URL of the main image                 |
| small_thumbnail   | VARCHAR    | URL of the small thumbnail image      |
| large_thumbnail   | VARCHAR    | URL of the large thumbnail image      |

### 4. `museums.csv`
This table contains information about the museums where the paintings are displayed.

| Column Name  | Data Type | Description                           |
|--------------|------------|---------------------------------------|
| museum_id    | INT        | Unique identifier for the museum      |
| name         | VARCHAR    | Name of the museum                    |
| address      | VARCHAR    | Address of the museum                 |
| city         | VARCHAR    | City where the museum is located      |
| state        | VARCHAR    | State where the museum is located     |
| postal       | VARCHAR    | Postal code of the museum             |
| country      | VARCHAR    | Country where the museum is located   |

### 5. `museum_hours.csv`
This table contains details about the operating hours of the museums.

| Column Name  | Data Type | Description                           |
|--------------|------------|---------------------------------------|
| museum_id    | INT        | Unique identifier for the museum      |
| day          | VARCHAR    | Day of the week                       |
| open_time    | TIME       | Opening time of the museum            |
| close_time   | TIME       | Closing time of the museum            |

### 6. `product_size.csv`
This table contains information about the sale and regular prices of paintings in different sizes.

| Column Name   | Data Type | Description                           |
|---------------|------------|---------------------------------------|
| work_id       | INT        | Unique identifier for the artwork     |
| size_id       | INT        | Unique identifier for the canvas size |
| sale_price    | DECIMAL    | Sale price of the painting            |
| regular_price | DECIMAL    | Regular price of the painting         |

### 7. `subject.csv`
This table contains information about the subjects of the paintings.

| Column Name  | Data Type | Description                           |
|--------------|------------|---------------------------------------|
| work_id      | INT        | Unique identifier for the artwork     |
| subject      | VARCHAR    | Subject of the painting               |

### 8. `work.csv`
This table contains details about the artworks.

| Column Name  | Data Type | Description                           |
|--------------|------------|---------------------------------------|
| work_id      | INT        | Unique identifier for the artwork     |
| name         | VARCHAR    | Name of the artwork                   |
| artist_id    | INT        | Unique identifier for the artist      |
| style        | VARCHAR    | Style of the artwork                  |
| museum_id    | INT        | Unique identifier for the museum      |

## Case Study Queries
Below are some of the key queries solved in this case study:

1. Fetch all the paintings which are not displayed in any museums.
2. Identify museums without any paintings.
3. How many paintings have an asking price greater than their regular price?
4. Identify the paintings whose asking price is less than 50% of its regular price.
5. Which canvas size costs the most?
6. Delete duplicate records from `work`, `product_size`, `subject`, and `image_link` tables.
7. Identify the museums with invalid city information in the dataset.
8. Identify the museums which are open on both Sunday and Monday. Display museum name and city.
9. Which are the top 5 most popular museums?
10. Who are the top 5 most popular artists?
11. Which museum is open for the longest duration during a day? Display museum name, state, hours open, and the specific day.

## Data Upload to PostgreSQL
The datasets were downloaded from Kaggle and uploaded into a PostgreSQL database using a simple Python script. Below is the script used and please make sure than the datset is downladed in the local device and the location of the files are mentioned in the python code.

### Python Script for Uploading Data
```python
import pandas as pd
from sqlalchemy import create_engine

conn_string = 'postgresql://postgres:'Password'@localhost/Project_1'
db = create_engine(conn_string)
conn = db.connect()

files = ['artist', 'canvas_size','image_link', 'museum_hours','museum','product_size', 'subject', 'work']

for file in files:

    df = pd.read_csv('LOCATION OF FILE IN THE SYSTEM')
    df.to_sql(file, con=conn, if_exists = 'replace', index=False)


