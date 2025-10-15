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


Faca um bot para o telegram no Main.py que a cada minuto validara se tem eventos e mandara mensagens para o user
o formato dos dados estao em remindeList/Reminder.json La vc tem a lsita dos dias e o que faz em cada horario
