# Simulador de automatos finitos

## Sobre

Script feito em python 3 para simular um automato finito inserido por meio da linha de comando

## Requisitos

- Interpretador python 3.x

## Estrutura dos arquivos

### Arquivo do automato

- O arquivo de entrada deve estar em formato json com a seguinte estrutura:

```json
{
    "initial": int,
    "final": int[],
    "transitions": [
        {
            "from": int | str,
            "to": str | int,
            "read": str | null
        }, 
        .
        .
        ., 
        {
            "from": int | str,
            "to": str | int,
            "read": str | null
        }
    ]
}
```

### Arquivo de entrada

- O arquivo deve estar no formato csv, utilizando o ';' como separador
- Deve primeiro vir a palavra desejada

```csv
word;1
```

### Arquio de saída

## Como usar

- Adicione o o automato e os testes na pasta onde está o script
- Abra o terminar e execute o seguinte comando: ```python main.py automato.aut testes.in saida.out```
- O resultado sera sobrescrito no ultimo argumento, se existir, caso não exista, o arquivo é criado
