import os
import json
import asyncio
from datetime import datetime, timedelta
from telegram import Bot
from telegram.error import TelegramError
import logging
from dotenv import load_dotenv

# Carregar variáveis de ambiente do arquivo .env
load_dotenv()

# Configuração de logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

class RemindMeBot:
    def __init__(self):
        # Carregar configurações do ambiente
        self.bot_token = os.getenv('TELEGRAM_BOT_TOKEN')
        self.allowed_user_id = os.getenv('TELEGRAM_ALLOWED_USER_ID')
        
        if not self.bot_token or not self.allowed_user_id:
            raise ValueError("TELEGRAM_BOT_TOKEN e TELEGRAM_ALLOWED_USER_ID devem estar definidos no arquivo .env")
        
        self.bot = Bot(token=self.bot_token)
        self.reminder_data = self.load_reminder_data()
        self.last_daily_summary = None
        
    def load_reminder_data(self):
        """Carrega os dados do arquivo Reminder.json"""
        try:
            with open('../remindList/Reminder.json', 'r', encoding='utf-8') as file:
                return json.load(file)
        except FileNotFoundError:
            logger.error("Arquivo Reminder.json não encontrado")
            return {}
        except json.JSONDecodeError:
            logger.error("Erro ao decodificar o arquivo JSON")
            return {}
    
    def get_current_day(self):
        """Retorna o dia da semana atual em português"""
        days = {
            0: 'SEGUNDA',
            1: 'TERCA', 
            2: 'QUARTA',
            3: 'QUINTA',
            4: 'SEXTA',
            5: 'SABADO',
            6: 'DOMINGO'
        }
        return days[datetime.now().weekday()]
    
    def get_current_time(self):
        """Retorna o horário atual no formato HH:MM"""
        return datetime.now().strftime("%H:%M")
    
    async def send_message(self, message):
        """Envia mensagem para o usuário autorizado"""
        try:
            await self.bot.send_message(chat_id=self.allowed_user_id, text=message)
            logger.info(f"Mensagem enviada: {message}")
        except TelegramError as e:
            logger.error(f"Erro ao enviar mensagem: {e}")
    
    async def check_current_event(self):
        """Verifica se há evento no horário atual"""
        current_day = self.get_current_day()
        current_time = self.get_current_time()
        
        if current_day not in self.reminder_data:
            return
        
        day_events = self.reminder_data[current_day]
        
        if current_time in day_events:
            event = day_events[current_time]
            if event.get('title', '').strip():
                message = f"🔔 Lembrete {current_time}: {event['title']}"
                if event.get('detalhes', '').strip():
                    message += f"\n📝 Detalhes: {event['detalhes']}"
                await self.send_message(message)
    
    async def check_upcoming_events(self):
        """Verifica eventos que acontecerão em 30 minutos"""
        current_day = self.get_current_day()
        current_time = datetime.now()
        future_time = current_time + timedelta(minutes=30)
        future_time_str = future_time.strftime("%H:%M")
        
        if current_day not in self.reminder_data:
            return
        
        day_events = self.reminder_data[current_day]
        
        if future_time_str in day_events:
            event = day_events[future_time_str]
            if event.get('title', '').strip():
                message = f"⏰ Em 30 minutos ({future_time_str}): {event['title']}"
                if event.get('detalhes', '').strip():
                    message += f"\n📝 Detalhes: {event['detalhes']}"
                await self.send_message(message)
    
    async def send_daily_summary(self):
        """Envia resumo de todas as tarefas do dia às 00:00"""
        current_day = self.get_current_day()
        
        if current_day not in self.reminder_data:
            return
        
        day_events = self.reminder_data[current_day]
        events_with_tasks = []
        
        for time_str, event in day_events.items():
            if event.get('title', '').strip():
                events_with_tasks.append(f"🕐 {time_str} - {event['title']}")
        
        if events_with_tasks:
            message = f"📅 Resumo do dia - {current_day}\n\n" + "\n".join(events_with_tasks)
            await self.send_message(message)
            self.last_daily_summary = datetime.now().date()
    
    async def check_daily_summary(self):
        """Verifica se deve enviar o resumo diário"""
        current_date = datetime.now().date()
        current_time = datetime.now().time()
        
        # Enviar resumo às 00:00 se ainda não foi enviado hoje
        if (current_time.hour == 0 and current_time.minute == 0 and 
            self.last_daily_summary != current_date):
            await self.send_daily_summary()
    
    async def run_checks(self):
        """Executa todas as verificações"""
        try:
            await self.check_daily_summary()
            await self.check_current_event()
            await self.check_upcoming_events()
        except Exception as e:
            logger.error(f"Erro durante as verificações: {e}")
    
    async def start(self):
        """Inicia o bot"""
        logger.info("Iniciando RemindMe Bot...")
        
        # Enviar mensagem de inicialização
        await self.send_message("🤖 RemindMe Bot iniciado! Verificando eventos...")
        
        # Loop principal
        while True:
            try:
                await self.run_checks()
                await asyncio.sleep(60)  # Aguarda 1 minuto
            except KeyboardInterrupt:
                logger.info("Bot interrompido pelo usuário")
                await self.send_message("👋 RemindMe Bot encerrado.")
                break
            except Exception as e:
                logger.error(f"Erro no loop principal: {e}")
                await asyncio.sleep(60)  # Aguarda 1 minuto antes de tentar novamente

if __name__ == "__main__":
    try:
        bot = RemindMeBot()
        asyncio.run(bot.start())
    except Exception as e:
        logger.error(f"Erro ao iniciar o bot: {e}")
