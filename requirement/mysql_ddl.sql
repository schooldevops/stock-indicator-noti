-- 데이터베이스 생성
CREATE DATABASE stock_indicator_db;

-- 데이터베이스 사용
USE stock_indicator_db;

-- 사용자 생성 (사용자 이름과 비밀번호를 적절히 변경하세요)
CREATE USER 'stock_user'@'%' IDENTIFIED BY 'your_password';

-- CRUD 권한 부여
GRANT ALL PRIVILEGES ON stock_indicator_db.* TO 'stock_user'@'%';

-- 권한 적용
FLUSH PRIVILEGES;

-- 테이블 생성 예시 (티커 테이블)
CREATE TABLE tickers (
    id INT AUTO_INCREMENT PRIMARY KEY,
    ticker VARCHAR(10) NOT NULL UNIQUE,
    name VARCHAR(255) NOT NULL,
    description TEXT,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    modified_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- 테이블 생성 예시 (인디케이터 테이블)
CREATE TABLE indicators (
    id INT AUTO_INCREMENT PRIMARY KEY,
    indicator_code VARCHAR(10) NOT NULL UNIQUE,
    indicator_name VARCHAR(255) NOT NULL,
    description TEXT,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    modified_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);