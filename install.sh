#!/bin/bash

echo "🤖 Instalando RemindMe Bot..."

# Verificar se o Python 3 está instalado
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 não encontrado. Por favor, instale o Python 3 primeiro."
    exit 1
fi

# Criar ambiente virtual se não existir
if [ ! -d "remindme-env" ]; then
    echo "📦 Criando ambiente virtual..."
    python3 -m venv remindme-env
fi

# Ativar ambiente virtual
echo "🔧 Ativando ambiente virtual..."
source remindme-env/bin/activate

# Instalar dependências
echo "📚 Instalando dependências..."
pip install -r requirements.txt

# Copiar arquivo de exemplo se .env não existir
if [ ! -f ".env" ]; then
    echo "📋 Criando arquivo .env..."
    cp env.example .env
    echo "⚠️  IMPORTANTE: Edite o arquivo .env com suas configurações do Telegram!"
    echo "   - TELEGRAM_BOT_TOKEN: Token do seu bot (obtenha com @BotFather)"
    echo "   - TELEGRAM_ALLOWED_USER_ID: Seu User ID (obtenha com @userinfobot)"
fi

echo "✅ Instalação concluída!"
echo ""
echo "📝 Próximos passos:"
echo "1. Edite o arquivo .env com suas configurações"
echo "2. Execute: source remindme-env/bin/activate"
echo "3. Execute: cd src && python Main.py"
