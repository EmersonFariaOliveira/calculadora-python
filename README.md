# Calculadora Simples em Python

Este projeto é uma **calculadora de linha de comando** escrita em Python, que permite realizar operações matemáticas básicas de forma simples e interativa.

## Funcionalidades

- Soma (`+`)
- Subtração (`-`)
- Multiplicação (`*`)
- Divisão (`/`) com tratamento de divisão por zero
- Potência (`^`)
- Resto da divisão (`%`)
- Repetição de cálculos sem precisar reiniciar o programa
- Confirmação antes de sair
- Aceita números com **vírgula ou ponto** (ex.: `10,5` ou `10.5`)

## Requisitos

- **Python 3.8+** instalado na máquina  
  Para verificar, execute no terminal/prompt:

```bash
python --version
```

Se o comando acima não funcionar, tente:

```bash
python3 --version
```

## Como executar

1. Clone o repositório:

```bash
git clone https://github.com/EmersonFariaOliveira/calculadora-python.git
cd calculadora-python
```

2. Execute o arquivo da calculadora:

```bash
python calculadora.py
```

Ou, dependendo da sua instalação:

```bash
python3 calculadora.py
```

## Como usar

1. Ao iniciar, será exibido o menu com as operações disponíveis.
2. Escolha uma opção digitando o número correspondente (de `0` a `6`).
3. Informe o primeiro número.
4. Informe o segundo número.
5. O resultado da operação será exibido na tela.
6. Você poderá escolher se deseja fazer outro cálculo ou encerrar o programa.

## Estrutura do projeto

- `calculadora.py` — código fonte principal da calculadora.
- `README.md` — este arquivo, com explicações sobre o projeto.

## Próximas melhorias (ideias)

- Adicionar histórico de operações.
- Suporte a operações com mais de dois números.
- Interface gráfica (ex.: usando Tkinter).
- Testes automatizados.
