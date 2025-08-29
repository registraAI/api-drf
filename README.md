### Passo-a-passo para instalação deste projeto
```bash
mkdir nome-da-sua-pasta
cd nome-da-sua-pasta
git clone https://github.com/registraAI/api-drf.git .
code .
```

### Agora dentro do seu vscode
Abra um terminal novo e insira os seguintes comandos:
- Para o Windows
```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```
- Para Linux
```bash
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
```
___
## Boas práticas
### [Conventional commits](https://www.conventionalcommits.org/pt-br/v1.0.0/#resumo)
São trechos que servem para melhorar o controle sobre os fluxos de commit, os principais para nosso projeto são:
- *feat*: serve para indicar que seu commit conta com algo novo para a base de código
```bash
git commit -m "feat: criei a função x"
```
- *fix*: serve para indicar que seu commit conserta algo na base de código
```bash
git commit -m "fix: corrigi a função x"
```
### Manejando branches
Vamos trabalhar com duas branches fixas que são:
- *main*: Servirá para guardar códigos funcionais e aprovados para serem usados com o minimo de erros possiveis. Pense nela como um check-point. **NÃO DÊ COMMIT DIRETO NA MAIN**
- *dev*: É a branch de desenvolvimento, nela teremos o código em fase de testes e que quando estiver aprovado será fundido com a main para "salvarmos o progresso".
Para melhor organização também separeremos as branches por funcionalidades, por exemplo, digamos que eu esteja responsavel por implementar a funcionalidade de autenticação:
- Primeiro devo criar no projeto que está na minha máquina uma branch para isso.
```bash
git branch auth
git switch auth
```
- Agora estou na branch correta e posso continuar o desenvolvimento, quando terminar posso fazer um commit para o repositório remoto no github.
```bash
git commit -m "feat: criei a função autenticação"
git push origin auth
```
- Agora no github crie uma pull request para a branch dev e pronto, terminou pae.