#!/bin/bash

# Script para push completo a GitHub
# Ejecutar después de crear el repositorio en GitHub

echo "🚀 Iniciando push a GitHub..."

# Verificar que estemos en la branch main
current_branch=$(git branch --show-current)
if [ "$current_branch" != "main" ]; then
    echo "❌ Debes estar en la branch main. Ejecuta: git checkout main"
    exit 1
fi

# Agregar remote si no existe
if ! git remote get-url origin >/dev/null 2>&1; then
    echo "📡 Agregando remote origin..."
    git remote add origin https://github.com/christianfuentesradar/strands-agents-workshop.git
fi

# Push de main
echo "⬆️  Push de main..."
git push -u origin main

# Push de develop
echo "⬆️  Push de develop..."
git push origin develop

# Push de todas las feature branches
echo "⬆️  Push de feature branches..."
git push origin feature/level-1-simple-agent
git push origin feature/level-2-basic-tools
git push origin feature/level-3-multi-tools
git push origin feature/level-4-planner-executor
git push origin feature/docs-and-testing

echo "✅ ¡Push completo exitoso!"
echo ""
echo "🎯 Próximos pasos:"
echo "1. Ve a https://github.com/christianfuentesradar/strands-agents-workshop"
echo "2. Revisa que todas las branches aparezcan"
echo "3. Configura branch protection (Settings > Branches)"
echo "4. Configura labels para issues"
echo "5. ¡Comparte tu taller con la comunidad! 🌟"
