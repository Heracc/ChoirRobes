PRAGMA foreign_keys = ON;

CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY,
    name TEXT,
    grade INTEGER
);

CREATE TABLE IF NOT EXISTS robes (
    id INTEGER PRIMARY KEY,
    student_id INTEGER UNIQUE,

    FOREIGN KEY (student_id) REFERENCES students (id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS pieces (
    id INTEGER PRIMARY KEY,
    title TEXT
);

CREATE TABLE IF NOT EXISTS sheets (
    id INTEGER PRIMARY KEY,
    piece_id INTEGER NOT NULL,
    student_id INTEGER,

    FOREIGN KEY (piece_id) REFERENCES pieces (id) ON DELETE CASCADE,
    FOREIGN KEY (student_id) REFERENCES students (id) ON DELETE CASCADE
);