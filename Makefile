# Makefile - Trabalho M1 Grafos

PYTHON = python3

.PHONY: demo all help clean slides slides_mod espacoaereo parte1 parte2 data_all

demo:
	@echo "Demonstracao principal..."
	@$(PYTHON) demo_parte2.py

parte1:
	@echo "Demonstracao Parte 1..."
	@$(PYTHON) demo_parte1.py

parte2:
	@echo "Demonstracao Parte 2..."
	@$(PYTHON) demo_parte2.py

slides:
	@echo "Demonstracao com slides.txt..."
	@$(PYTHON) demo_parte2.py

slides_mod:
	@echo "Demonstracao com slides_modificado.txt..."
	@$(PYTHON) demo_parte2.py

espacoaereo:
	@echo "Demonstracao com espacoaereo.txt..."
	@$(PYTHON) demo_parte2.py

data_all: slides slides_mod espacoaereo

all: parte1 parte2 data_all

clean:
	@echo "Limpando..."
	@find . -name "*.pyc" -delete 2>/dev/null || true
	@find . -name "__pycache__" -type d -exec rm -rf {} + 2>/dev/null || true

help:
	@echo "TRABALHO M1 - GRAFOS"
	@echo "Comandos disponiveis:"
	@echo "  make demo        - Demonstracao principal"
	@echo "  make parte1      - Demonstracao da Parte 1"
	@echo "  make parte2      - Demonstracao da Parte 2"
	@echo "  make slides      - Demo com slides.txt"
	@echo "  make slides_mod  - Demo com slides_modificado.txt"
	@echo "  make espacoaereo - Demo com espacoaereo.txt"
	@echo "  make data_all    - Demo com todos os arquivos de dados"
	@echo "  make all         - Executar todas as demonstracoes"
	@echo "  make clean       - Limpar arquivos temporarios"
	@echo "  make help        - Mostrar esta ajuda"
