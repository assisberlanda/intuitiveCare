-- Criação da tabela operadoras_ativas
CREATE TABLE operadoras_ativas (
    Registro_ANS VARCHAR(20) PRIMARY KEY,
    CNPJ VARCHAR(20),
    Razao_Social VARCHAR(255),
    Nome_Fantasia VARCHAR(255),
    Modalidade VARCHAR(100),
    Logradouro VARCHAR(255),
    Numero VARCHAR(10),
    Complemento VARCHAR(255),
    Bairro VARCHAR(100),
    Cidade VARCHAR(100),
    UF CHAR(2),
    CEP VARCHAR(10),
    DDD VARCHAR(5),
    Telefone VARCHAR(20),
    Fax VARCHAR(20),
    Endereco_eletronico VARCHAR(255),
    Representante VARCHAR(255),
    Cargo_Representante VARCHAR(100),
    Regiao_de_Comercializacao TEXT,
    Data_Registro_ANS DATE
);

-- Importação dos dados para operadoras_ativas
LOAD DATA INFILE '/Users/berlanda/Downloads/intuitiveCare/data_base/Relatorio_cadop.csv'
INTO TABLE operadoras_ativas
FIELDS TERMINATED BY ','
IGNORE 1 ROWS;

