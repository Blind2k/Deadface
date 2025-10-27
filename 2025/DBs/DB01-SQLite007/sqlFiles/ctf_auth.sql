DROP TABLE IF EXISTS users;

-- *) Login DB
CREATE TABLE IF NOT EXISTS users (username TEXT, password TEXT);

INSERT INTO users (username, password) VALUES ('admin', '231fsda7dsabg56ds9a6fd9qm7f9m17f4791b56fb1456817fb5871n9');
INSERT INTO users (username, password) VALUES ('alpha','a1a2a3a4a5a6978899aabbccddeeff');
INSERT INTO users (username, password) VALUES ('bravo','b1b2b3b4b5b6c7d8e9f0a1b2c3d4e5f');
INSERT INTO users (username, password) VALUES ('charlie2','c2c3c4c5c6c7d8e9f0a1b2c3d4e5f60');
INSERT INTO users (username, password) VALUES ('delta','d3d4d5d6d7d8e9f0a1b2c3d4e5f6071');
INSERT INTO users (username, password) VALUES ('legacy1','lgcy-001-aaaa1111bbbb2222cccc3333');
INSERT INTO users (username, password) VALUES ('legacy2','lgcy-002-dddd4444eeee5555ffff6666');
INSERT INTO users (username, password) VALUES ('sys','sys-9e9d8c7b6a5f4e3d2c1b');
INSERT INTO users (username, password) VALUES ('integration','intg-000-123abc456def789ghi');
INSERT INTO users (username, password) VALUES ('u101','p101-1111222233334444555566667777');
INSERT INTO users (username, password) VALUES ('u102','p102-88889999aaaabbbbccccdddd0000');
INSERT INTO users (username, password) VALUES ('u103','p103-123123123abcabcabc456456456def');
INSERT INTO users (username, password) VALUES ('u104','p104-9876543210fedcba0123456789abcd');
INSERT INTO users (username, password) VALUES ('u105','p105-0f0e0d0c0b0a09080706050403020100');
INSERT INTO users (username, password) VALUES ('qa01','qa-01-aaaaaaaa1111111122222222333333');
INSERT INTO users (username, password) VALUES ('qa02','qa-02-bbbbbbbb2222222233333333444444');
INSERT INTO users (username, password) VALUES ('ci_bot','ci-bot-commit-9a8b7c6d5e4f3a2b1c');
INSERT INTO users (username, password) VALUES ('deploy','deploy-2025-0a0b0c0d0e0f');
