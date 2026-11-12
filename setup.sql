PRAGMA foreign_keys = ON;

CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY,
    name TEXT,
    grade INTEGER CHECK (grade >= 9 AND grade <= 12)
);

CREATE TABLE IF NOT EXISTS robes (
    id INTEGER PRIMARY KEY,
    student_id INTEGER UNIQUE,

    FOREIGN KEY (student_id) REFERENCES students (id) ON DELETE SET NULL
);

CREATE TABLE IF NOT EXISTS pieces (
    id INTEGER PRIMARY KEY,
    title TEXT
);

CREATE TABLE IF NOT EXISTS sheets (
    id INTEGER PRIMARY KEY,
    piece_id INTEGER NOT NULL,
    student_id INTEGER,

    -- ai told me to use restrict instead of set null for the piece_id so you cant delete a piece that still has sheets
    FOREIGN KEY (piece_id) REFERENCES pieces (id) ON DELETE RESTRICT,
    FOREIGN KEY (student_id) REFERENCES students (id) ON DELETE SET NULL
);