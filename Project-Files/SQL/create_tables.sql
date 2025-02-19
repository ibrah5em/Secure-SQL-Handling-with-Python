
    CREATE TABLE users (
        id INT PRIMARY KEY IDENTITY(1,1),
        username NVARCHAR(50) NOT NULL,
        password NVARCHAR(50) NOT NULL
    );

    -- Insert sample data
    INSERT INTO users (username, password) VALUES ('admin', 'admin');
    INSERT INTO users (username, password) VALUES ('user1', 'password1');
    INSERT INTO users (username, password) VALUES ('user2', 'password2');
    INSERT INTO users (username, password) VALUES ('user3', 'password3');
    INSERT INTO users (username, password) VALUES ('johndoe', 'secret');

