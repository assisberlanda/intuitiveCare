-- Criação das tabelas contábeis para 2023 e 2024

-- Estrutura para contabeis_2023
CREATE TABLE contabeis_2023_1_trimestre (
    DATA DATE,
    REG_ANS VARCHAR(20),
    CD_CONTA_CONTABIL VARCHAR(50),
    DESCRICAO TEXT,
    VL_SALDO_INICIAL DECIMAL(15,2),
    VL_SALDO_FINAL DECIMAL(15,2)
);

CREATE TABLE contabeis_2023_2_trimestre LIKE contabeis_2023_1_trimestre;
CREATE TABLE contabeis_2023_3_trimestre LIKE contabeis_2023_1_trimestre;
CREATE TABLE contabeis_2023_4_trimestre LIKE contabeis_2023_1_trimestre;

-- Estrutura para contabeis_2024
CREATE TABLE contabeis_2024_1_trimestre LIKE contabeis_2023_1_trimestre;
CREATE TABLE contabeis_2024_2_trimestre LIKE contabeis_2023_1_trimestre;
CREATE TABLE contabeis_2024_3_trimestre LIKE contabeis_2023_1_trimestre;
CREATE TABLE contabeis_2024_4_trimestre LIKE contabeis_2023_1_trimestre;

-- Importação dos arquivos CSV para as tabelas contábeis
LOAD DATA INFILE '/Users/berlanda/Downloads/intuitiveCare/data_base/demonstracoes_contabeis:2023/1T2023.csv'
INTO TABLE contabeis_2023_1_trimestre
FIELDS TERMINATED BY ','
IGNORE 1 ROWS;

LOAD DATA INFILE '/Users/berlanda/Downloads/intuitiveCare/data_base/demonstracoes_contabeis:2023/2T2023.csv'
INTO TABLE contabeis_2023_2_trimestre
FIELDS TERMINATED BY ','
IGNORE 1 ROWS;

LOAD DATA INFILE '/Users/berlanda/Downloads/intuitiveCare/data_base/demonstracoes_contabeis:2023/3T2023.csv'
INTO TABLE contabeis_2023_3_trimestre
FIELDS TERMINATED BY ','
IGNORE 1 ROWS;

LOAD DATA INFILE '/Users/berlanda/Downloads/intuitiveCare/data_base/demonstracoes_contabeis:2023/4T2023.csv'
INTO TABLE contabeis_2023_4_trimestre
FIELDS TERMINATED BY ','
IGNORE 1 ROWS;

LOAD DATA INFILE '/Users/berlanda/Downloads/intuitiveCare/data_base/demonstracoes_contabeis:2024/1T2024.csv'
INTO TABLE contabeis_2024_1_trimestre
FIELDS TERMINATED BY ','
IGNORE 1 ROWS;

LOAD DATA INFILE '/Users/berlanda/Downloads/intuitiveCare/data_base/demonstracoes_contabeis:2024/2T2024.csv'
INTO TABLE contabeis_2024_2_trimestre
FIELDS TERMINATED BY ','
IGNORE 1 ROWS;

LOAD DATA INFILE '/Users/berlanda/Downloads/intuitiveCare/data_base/demonstracoes_contabeis:2024/3T2024.csv'
INTO TABLE contabeis_2024_3_trimestre
FIELDS TERMINATED BY ','
IGNORE 1 ROWS;

LOAD DATA INFILE '/Users/berlanda/Downloads/intuitiveCare/data_base/demonstracoes_contabeis:2024/4T2024.csv'
INTO TABLE contabeis_2024_4_trimestre
FIELDS TERMINATED BY ','
IGNORE 1 ROWS;

-- Query para as 10 operadoras com maiores despesas no 4º trimestre de 2024
SELECT REG_ANS, SUM(VL_SALDO_FINAL - VL_SALDO_INICIAL) AS Total_Despesas
FROM contabeis_2024_4_trimestre
WHERE DESCRICAO = 'EVENTOS/ SINISTROS CONHECIDOS OU AVISADOS DE ASSISTÊNCIA A SAÚDE MEDICO HOSPITALAR'
GROUP BY REG_ANS
ORDER BY Total_Despesas DESC
LIMIT 10;

-- Query para as 10 operadoras com maiores despesas ao longo de 2024
SELECT REG_ANS, SUM(VL_SALDO_FINAL - VL_SALDO_INICIAL) AS Total_Despesas
FROM (
    SELECT * FROM contabeis_2024_1_trimestre
    UNION ALL
    SELECT * FROM contabeis_2024_2_trimestre
    UNION ALL
    SELECT * FROM contabeis_2024_3_trimestre
    UNION ALL
    SELECT * FROM contabeis_2024_4_trimestre
) AS contabeis_2024
WHERE DESCRICAO = 'EVENTOS/ SINISTROS CONHECIDOS OU AVISADOS DE ASSISTÊNCIA A SAÚDE MEDICO HOSPITALAR'
GROUP BY REG_ANS
ORDER BY Total_Despesas DESC
LIMIT 10;
