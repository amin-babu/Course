-- Active: 1734759755498@@127.0.0.1@3306@bus ticket booking
CREATE TABLE buses (
  bus_id INT PRIMARY KEY AUTO_INCREMENT,
  bus_name VARCHAR(255) NOT NULL,
  bus_type VARCHAR(255) NOT NULL,
  total_seat INT NOT NULL
)

CREATE TABLE passengers (
  passenger_id INT PRIMARY KEY AUTO_INCREMENT,
  name VARCHAR(100) NOT NULL,
  email VARCHAR(100) UNIQUE NOT NULL,
  phone VARCHAR(15) UNIQUE NOT NULL
)

CREATE TABLE routes (
  route_id INT PRIMARY KEY AUTO_INCREMENT,
  source VARCHAR(100) NOT NULL,
  destination VARCHAR(100) NOT NULL,
  fare INT NOT NULL
)


CREATE TABLE booking (
  booking_id INT PRIMARY KEY AUTO_INCREMENT,
  booking_date DATETIME NOT NULL,
  seat_number INT NOT NULL,
  passenger_id INT,
  route_id INT,
  FOREIGN KEY (passenger_id) REFERENCES passengers(passenger_id) ON DELETE CASCADE,
  FOREIGN KEY (route_id) REFERENCES routes(route_id) ON DELETE CASCADE
)

CREATE TABLE bus_route (
  bus_id INT,
  route_id INT,
  FOREIGN KEY (bus_id) REFERENCES buses(bus_id) ON DELETE CASCADE,
  FOREIGN KEY (route_id) REFERENCES routes(route_id) ON DELETE CASCADE
)