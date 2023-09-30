-- Crie o banco de dados
CREATE DATABASE MeuBancoDeDados;

-- Use o banco de dados criado
USE MeuBancoDeDados;

-- Crie as tabelas
CREATE TABLE Produto (
    identificador INT PRIMARY KEY,
    nome_produto VARCHAR(255),
    preco_produto DECIMAL(10, 2),
    custo_produto DECIMAL(10, 2),
    novo BOOLEAN,
    imposto DECIMAL(10, 2)
);

CREATE TABLE Venda (
	identificador INT PRIMARY KEY,
    entregue BOOLEAN
);

CREATE TABLE Produto_x_Venda (
	identificador INT AUTO_INCREMENT PRIMARY KEY,
    id_produto INT,
    FOREIGN KEY (id_produto) REFERENCES Produto(identificador),
    id_venda INT,
    FOREIGN KEY (id_venda) REFERENCES Venda(identificador),
    quantidade INT
);

-- Insere 5 produtos de vendas na tabela de produtos
DELIMITER //
CREATE PROCEDURE GenerateProductsData()
BEGIN
	INSERT INTO Produto (nome_produto, identificador, preco_produto, custo_produto, novo, imposto)
	VALUES ('Monitor', 1, 109.99, 49.9, 1, 19.9);
    INSERT INTO Produto (nome_produto, identificador, preco_produto, custo_produto, novo, imposto)
	VALUES ('Teclado', 5, 159.99, 79.49, 0, 17.9);
	INSERT INTO Produto (nome_produto, identificador, preco_produto, custo_produto, novo, imposto)
	VALUES ('Desktop', 3, 259.99, 39.49, 0, 21.9);
	INSERT INTO Produto (nome_produto, identificador, preco_produto, custo_produto, novo, imposto)
	VALUES ('Mouse', 2, 69.99, 29.49, 1, 24.9);
	INSERT INTO Produto (nome_produto, identificador, preco_produto, custo_produto, novo, imposto)
	VALUES ('Processador', 4, 569.99, 229.49, 1, 19.9);
END //
DELIMITER ;

CALL GenerateProductsData();

-- Insire 100 vendas aleatórias
DELIMITER //
CREATE PROCEDURE GenerateRandonSales()
BEGIN
    SET @counter = 0;
    WHILE @counter < 100 DO
        SET @EntregueStatus =  FLOOR(RAND() * 2);
        INSERT INTO Venda (identificador, entregue)
		VALUES (@counter, @EntregueStatus);
        SET @IdProduct = 1;
		WHILE @IdProduct < 6 DO
			SET @IsBought = FLOOR(RAND() * 2);
            IF @IsBought > 0 THEN
				SET @NumberOfProducts =  FLOOR(RAND() * 5) + 1;
				INSERT INTO Produto_x_Venda (id_produto, id_venda, quantidade)
				VALUES (@IdProduct, @counter, @NumberOfProducts);
			END IF;
			SET @IdProduct = @IdProduct + 1;
		END WHILE;
		SET @counter = @counter + 1;
    END WHILE;
END //
DELIMITER ;

CALL GenerateRandonSales;

-- Visualize os dados
SELECT * FROM Venda
INNER JOIN Produto_x_Venda
ON Venda.identificador = Produto_x_Venda.id_venda
INNER JOIN Produto ON Produto_x_Venda.id_produto = Produto.identificador;

SELECT id_venda, entregue, nome_produto, quantidade, preco_produto, custo_produto
FROM Venda INNER JOIN Produto_x_Venda ON Venda.identificador = Produto_x_Venda.id_venda 
INNER JOIN Produto ON Produto_x_Venda.id_produto = Produto.identificador
ORDER BY id_venda asc;

DROP DATABASE MEUBANCODEDADOS