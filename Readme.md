# RemindMe

RemindMe é um bot que le uma lista pre censtralizada e informa ao user o que tem para a quele momento



O que o reminder me Fara?

Ele verificara sua llista de dias e em cada horaio comunicara ao user selecionado TELEGRAM_ALLOWED_USER_ID seu evento em questao sempre avisara 30min antes do evento, e toda virara de dia 00:00 informara todas as tarefas do dia



Usamos Python 3.12.3
```
python3 -m venv remindme-env
```

```
source remindme-env/bin/activate
```


Copie o .eve.exemple e coloque seus dados
Copie a pasta remindList e faca sua lista


## Bot do Telegram Implementado! 🤖

O bot foi criado no arquivo `src/Main.py` e possui as seguintes funcionalidades:

### Funcionalidades:
- ✅ Verifica eventos a cada minuto
- ✅ Avisa 30 minutos antes de cada evento
- ✅ Envia resumo diário às 00:00 com todas as tarefas do dia
- ✅ Formato de dados compatível com `remindList/Reminder.json`

### Como usar:

1. **Instalação automática:**
   ```bash
   ./install.sh
   ```

2. **Configuração manual:**
   ```bash
   # Criar ambiente virtual
   python3 -m venv remindme-env
   
   # Ativar ambiente virtual
   source remindme-env/bin/activate
   
   # Instalar dependências
   pip install -r requirements.txt
   ```

3. **Configurar o bot:**
   - Copie `env.example` para `.env`
   - Edite o arquivo `.env` com suas configurações:
     - `TELEGRAM_BOT_TOKEN`: Token do seu bot (obtenha com @BotFather)
     - `TELEGRAM_ALLOWED_USER_ID`: Seu User ID (obtenha com @userinfobot)

4. **Executar o bot:**
   ```bash
   cd src
   python Main.py
   ```

### Como obter as configurações:

**Bot Token:**
1. Fale com @BotFather no Telegram
2. Use o comando `/newbot`
3. Siga as instruções para criar seu bot
4. Copie o token fornecido

**User ID:**
1. Fale com @userinfobot no Telegram
2. Ele retornará seu User ID
3. Copie o ID numérico fornecido

### Estrutura dos dados:
O formato dos dados está em `remindList/Reminder.json` com a lista dos dias e o que fazer em cada horário no formato:
```json
{
  "DOMINGO": {
    "6:00": {"title": "PASSEAR COM DOG", "detalhes": ""},
    "7:00": {"title": "Leitura pessoal", "detalhes": "Ler Livro Codigo limpo"}
  }
}
```
