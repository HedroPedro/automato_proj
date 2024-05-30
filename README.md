# Simulador de automatos finitos

## Sobre

Script feito em python 3 para simular um automato finito inserido por meio da linha de comando

## Requisitos

- Interpretador python 3.x

## Estrutura dos arquivos

### Arquivo do automato

- O arquivo de entrada deve estar em formato json com a seguinte estrutura:

```
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
- Deve primeiro vir a palavra desejada e depois o resultado esparado
- Um exemplo de arquivo seria:

```text
aaab;1
bba;0
...
aaaabaab;1
```

### Arquio de saída

- O arquivo de saída é um csv que utiliza o ';' como separador
- Primeiro virá a palavra, resultado esperado, resultado atual e tempo de computação
- Um exemplo de saida seria:

```text
aaab;1;1;0.0205
bba;0;0
...
aaaabaab;1;0;0.1789
```

## Como usar

- Adicione o automato e os testes na pasta onde está o script
- O programa nescessita de três argumentos extras, o arquivo do automato (.aut), a entrada (.in) e a saida (.out), nesta ordem
- Abra o terminar e execute o seguinte comando: ```python main.py arquivo.aut entrada.in saida.out```, substituindo arquivo.aut, entrada.in e saida.out pelo nome dos seus arquivos
- O resultado sera sobrescrito no ultimo argumento, se existir, caso não exista, o arquivo então é criado
