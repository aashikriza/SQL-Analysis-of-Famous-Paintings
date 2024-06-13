# SQL Analysis of Famous Paintings
# Famous Paintings Database

This repository contains SQL scripts and data files for a case study involving a database of famous paintings. The database is designed to store detailed information about artists, their artworks, museums where these artworks are displayed, and various related attributes. Below is a comprehensive description of the tables included in the database.

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

## Usage
The provided SQL scripts can be used to create and populate these tables in your database. Ensure to download the CSV files and place them in the appropriate directory for loading into your database.

## Contributing
Feel free to contribute to this project by submitting pull requests. For major changes, please open an issue first to discuss what you would like to change.



## Contact
If you have any questions or suggestions, please feel free to open an issue or contact the repository owner.

---
This README file provides an overview of the database structure and its contents, making it easier for users to understand the schema and how to work with the data.
