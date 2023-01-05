# Computação Gráfica

## Construções

1. **(P5)** Bézier de grau 3 usando a forma paramétrica da reta
2. **(P5)** Polígono estrelado
3. **(OpenGL)** Prisma e pirâmide
4. **(OpenGL)** Esfera
5. **(OpenGL)** Malha definida por uma função `f(x,y) -> z` (p. exemplo parabolóide circular e parabolóide hiperbólico)

**Importante:** Construções 1 e 2 estão em Javascript, enquanto as 3, 4 e 5 estão em Python.

## Instalação

### Para questões em Javascript

Recomendo o uso de qualquer servidor web simples. Nesse caso, usaremos o servidor web embutido do PHP, disponível em qualquer versão do **PHP 5.4** ou superior.

Para iniciar o servidor, basta executar o comando `php -S localhost:8000` na pasta raiz do projeto. Em seguida, basta acessar o endereço `http://localhost:8000` no seu navegador. Tem uma página de guia que te direcionará para as duas construções disponíveis.

### Para questões em Python

Será necessário apenas o **Python 3.8** com o venv instalado. Inicie um novo venv e instale as dependências com o arquivo `requirements.txt`:

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Caso você esteja executando via WSL, pode se deparar com vários erros. Isso ocorre pela falta de uma interface gráfica. Para contornar esse problema, vamos instalar algumas libs e forçar o uso de uma delas para a construção das interfaces:

```bash
sudo apt install ubuntu-desktop mesa-utils freeglut3-dev
export PYOPENGL_PLATFORM=glx
export LIBGL_ALWAYS_INDIRECT=0
```

Do lado do Windows, ainda será necessário instalar o [VcXsrv](https://sourceforge.net/projects/vcxsrv/) e escolher as opções `Multiple Windows`, `display 0`, `start no client` e `disable native opengl`. Se quiser mais informações, pode dar uma olhada na [issue #2855](https://github.com/microsoft/WSL/issues/2855) do WSL.

Agora para rodar as soluções, basta executar os arquivos `app.py` dentro de cada pasta. Por exemplo:

```bash
python c3/app.py
python c4/app.py
python c5/app.py
```

> **Nota:** Caso tenha passado pelos problemas no WSL e os tenha corrigido como descrito acima, não se esqueça de executar `export PYOPENGL_PLATFORM=glx` e `export LIBGL_ALWAYS_INDIRECT=0` sempre que for rodar o projeto, antes ou depois de executar `source venv/bin/activate`.