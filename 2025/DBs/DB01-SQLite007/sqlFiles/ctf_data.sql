DROP TABLE IF EXISTS secrets;
DROP TABLE IF EXISTS profiles;
DROP TABLE IF EXISTS sessions;
DROP TABLE IF EXISTS api_keys;
DROP TABLE IF EXISTS activity_logs;

-- **) Flag table
CREATE TABLE IF NOT EXISTS general (flag TEXT);
INSERT INTO very_not_common_name (flag) VALUES ('DEADFACE{you_found_the_sqli_01_flag!}');

-- Extra info
-- 1) profiles: user metadata
CREATE TABLE IF NOT EXISTS profiles (
    user_id TEXT PRIMARY KEY,
    username TEXT,
    full_name TEXT,
    email TEXT,
    bio TEXT,
    created_at TEXT
);

INSERT OR IGNORE INTO profiles (user_id, username, full_name, email, bio, created_at) VALUES ('u001','user001','Alice Mercer','alice.mercer@example.test','Enthusiastic tester and coffee lover. Writes silly scripts on weekends.', '2024-01-12 09:15:00');
INSERT OR IGNORE INTO profiles (user_id, username, full_name, email, bio, created_at) VALUES ('u002','user002','Bob Carter','bob.carter@example.test','DevOps tinkerer. Collector of weird logs.', '2024-02-05 14:03:00');
INSERT OR IGNORE INTO profiles (user_id, username, full_name, email, bio, created_at) VALUES ('u003','user003','Charlie Vega','charlie.vega@example.test','Likes long walks through console output.', '2024-03-21 20:30:00');
INSERT OR IGNORE INTO profiles (user_id, username, full_name, email, bio, created_at) VALUES ('u004','alice','Alice Liddell','alice.liddell@example.test','Faux admin account for integration tests.', '2023-11-11 11:11:11');
INSERT OR IGNORE INTO profiles (user_id, username, full_name, email, bio, created_at) VALUES ('u005','bob','Robert "Bob" Stone','robert.stone@example.test','Temporary account. Do not panic.', '2022-07-01 08:00:00');
INSERT OR IGNORE INTO profiles (user_id, username, full_name, email, bio, created_at) VALUES ('u006','guest','Guest User','guest@example.test','Guest profile for demonstrations.', '2025-01-01 00:00:00');
INSERT OR IGNORE INTO profiles (user_id, username, full_name, email, bio, created_at) VALUES ('svc_db','service_db','Database Service','dbsvc@example.test','Service account used by DB jobs (fake).', '2024-06-30 12:00:00');
INSERT OR IGNORE INTO profiles (user_id, username, full_name, email, bio, created_at) VALUES ('qa01','qa01','QA Team Member','qa01@example.test','QA automation bot.', '2024-05-15 09:00:00');
INSERT OR IGNORE INTO profiles (user_id, username, full_name, email, bio, created_at) VALUES ('u101','u101','Member 101','member101@example.test','Patterned user for load testing.', '2023-03-10 07:45:00');
INSERT OR IGNORE INTO profiles (user_id, username, full_name, email, bio, created_at) VALUES ('root','root','Root User','root@example.test','Simulated superuser (do not use in production).', '2021-12-31 23:59:59');

-- 2) sessions: active session tokens / tracking (fake session ids)
CREATE TABLE IF NOT EXISTS sessions (
    session_id TEXT PRIMARY KEY,
    user_id TEXT,
    created_at TEXT,
    expires_at TEXT,
    client_ip TEXT,
    user_agent TEXT
);

INSERT OR IGNORE INTO sessions (session_id, user_id, created_at, expires_at, client_ip, user_agent) VALUES ('sess-1a2b3c4d','u001','2025-09-18 12:00:00','2025-09-18 18:00:00','192.0.2.10','Mozilla/5.0 (TestAgent)');
INSERT OR IGNORE INTO sessions (session_id, user_id, created_at, expires_at, client_ip, user_agent) VALUES ('sess-7f8e9d0c','u002','2025-09-17 08:20:00','2025-09-17 20:20:00','198.51.100.22','ci-bot/1.0');
INSERT OR IGNORE INTO sessions (session_id, user_id, created_at, expires_at, client_ip, user_agent) VALUES ('sess-aa11bb22','u003','2025-09-15 22:45:00','2025-09-16 22:45:00','203.0.113.5','curl/7.82.0');
INSERT OR IGNORE INTO sessions (session_id, user_id, created_at, expires_at, client_ip, user_agent) VALUES ('sess-ffff0000','guest','2025-09-19 06:00:00','2025-09-19 18:00:00','10.0.0.5','GuestClient/0.1');
INSERT OR IGNORE INTO sessions (session_id, user_id, created_at, expires_at, client_ip, user_agent) VALUES ('sess-dbsvc-01','svc_db','2025-09-10 00:00:00','2026-09-10 00:00:00','127.0.0.1','Service/DBJob');
INSERT OR IGNORE INTO sessions (session_id, user_id, created_at, expires_at, client_ip, user_agent) VALUES ('sess-ci-9a8b','qa01','2025-08-01 09:00:00','2025-08-01 17:00:00','172.16.0.8','CI-Pipeline/runner');

-- 3) api_keys: fake API keys and scopes
CREATE TABLE IF NOT EXISTS api_keys (
    key_id TEXT PRIMARY KEY,
    user_id TEXT,
    api_key TEXT,
    scopes TEXT,
    created_at TEXT,
    revoked INTEGER DEFAULT 0
);

INSERT OR IGNORE INTO api_keys (key_id, user_id, api_key, scopes, created_at, revoked) VALUES ('key-0001','u001','ak_test_0123456789abcdef','read,write', '2024-09-01 10:00:00', 0);
INSERT OR IGNORE INTO api_keys (key_id, user_id, api_key, scopes, created_at, revoked) VALUES ('key-0002','u002','ak_test_fedcba9876543210','read', '2024-09-02 11:00:00', 0);
INSERT OR IGNORE INTO api_keys (key_id, user_id, api_key, scopes, created_at, revoked) VALUES ('key-0003','svc_db','ak_srv_db_aaaaaaaa1111','db:read,db:write', '2024-06-30 12:05:00', 0);
INSERT OR IGNORE INTO api_keys (key_id, user_id, api_key, scopes, created_at, revoked) VALUES ('key-0004','qa01','ak_qa_9999bbbb0000','test:run', '2025-02-14 09:09:09', 0);
INSERT OR IGNORE INTO api_keys (key_id, user_id, api_key, scopes, created_at, revoked) VALUES ('key-revoked-1','u003','ak_revoked_1234deadbeef','read', '2023-12-01 00:00:00', 1);
INSERT OR IGNORE INTO api_keys (key_id, user_id, api_key, scopes, created_at, revoked) VALUES ('key-admin-alpha','root','ak_root_admin_zz99yy88','admin', '2021-01-01 01:01:01', 0);
INSERT OR IGNORE INTO api_keys (key_id, user_id, api_key, scopes, created_at, revoked) VALUES ('key-guest-temp','guest','ak_guest_temp_0000','read', '2025-09-19 05:55:00', 0);

-- 4) activity_logs: user actions (fake, verbose for testing)
CREATE TABLE IF NOT EXISTS activity_logs (
    log_id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id TEXT,
    action TEXT,
    timestamp TEXT,
    details TEXT
);

INSERT OR IGNORE INTO activity_logs (user_id, action, timestamp, details) VALUES ('u001','login','2025-09-18 12:00:10','Successful password auth from 192.0.2.10');
INSERT OR IGNORE INTO activity_logs (user_id, action, timestamp, details) VALUES ('u002','failed_login','2025-09-17 08:21:03','Invalid password attempt, user_agent=ci-bot/1.0');
INSERT OR IGNORE INTO activity_logs (user_id, action, timestamp, details) VALUES ('u003','password_reset','2025-05-02 15:33:00','Password reset requested via email');
INSERT OR IGNORE INTO activity_logs (user_id, action, timestamp, details) VALUES ('guest','view_page','2025-09-19 06:05:22','Visited /landing');
INSERT OR IGNORE INTO activity_logs (user_id, action, timestamp, details) VALUES ('svc_db','job_run','2025-09-10 00:02:11','Nightly DB job completed, rows_processed=10234');
INSERT OR IGNORE INTO activity_logs (user_id, action, timestamp, details) VALUES ('qa01','test_run','2025-08-01 09:10:00','Integration test suite executed, failures=0');
INSERT OR IGNORE INTO activity_logs (user_id, action, timestamp, details) VALUES ('root','schema_migration','2024-12-31 23:50:00','Applied migration v20241231_01');
INSERT OR IGNORE INTO activity_logs (user_id, action, timestamp, details) VALUES ('u101','bulk_import','2023-03-10 07:46:11','Imported 1000 fake users from CSV');
INSERT OR IGNORE INTO activity_logs (user_id, action, timestamp, details) VALUES ('u002','api_call','2024-09-02 11:02:45','Called /api/v1/report?start=2024-08-01');
INSERT OR IGNORE INTO activity_logs (user_id, action, timestamp, details) VALUES ('u001','logout','2025-09-18 17:59:59','User logged out manually');
