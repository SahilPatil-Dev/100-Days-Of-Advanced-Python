-- BEFORE INDEX

EXPLAIN ANALYZE
SELECT * FROM users WHERE email = 'user500@example.com';

EXPLAIN ANALYZE
SELECT * FROM orders WHERE user_id = 100;

EXPLAIN ANALYZE
SELECT * FROM users WHERE age = 30;


-- ADD INDEXES

CREATE INDEX idx_users_email ON users(email);
CREATE INDEX idx_orders_user_id ON orders(user_id);
CREATE INDEX idx_users_age ON users(age);


-- AFTER INDEX

EXPLAIN ANALYZE
SELECT * FROM users WHERE email = 'user500@example.com';

EXPLAIN ANALYZE
SELECT * FROM orders WHERE user_id = 100;

