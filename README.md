# Utilizando TDD com o auxílio da biblioteca de testes Pytest

Nesse exemplo vou verificar a existência da função is_even no arquivo testes.py.

Após a aplicação do Pytest será possível verificar 3 erros, 1 NameError na função test_in_even_true, 1 NameError na test_in_even_false e 1 NameError 
na test_in_even_except, pois a função is_even não existe.

Obs: Um NameError é gerado quando uma variável ou função não é válida. Nesse Caso estou chamando uma função, is_even, que não foi declarada. 
