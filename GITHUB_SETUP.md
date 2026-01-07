# 🚀 Configuración de GitHub para Strands Agents Workshop

Este archivo contiene las instrucciones para crear y configurar el repositorio en GitHub.

## 📋 Pasos para Crear el Repositorio

### 1. Crear Repositorio en GitHub

1. Ve a [GitHub.com](https://github.com) y haz login
2. Click en el botón **"New repository"**
3. Configura el repositorio:
   - **Repository name**: `strands-agents-workshop`
   - **Description**: `Un taller progresivo para dominar agentes inteligentes con Strands`
   - **Visibility**: `Public` ✅
   - ⚠️ **NO marques** "Add a README file" (ya tenemos uno)
   - ⚠️ **NO marques** "Add .gitignore" (ya tenemos uno)
   - ⚠️ **NO marques** "Choose a license" (ya tenemos MIT)

### 2. Conectar Repositorio Local con GitHub

Después de crear el repositorio, GitHub te mostrará comandos. Ejecuta:

```bash
# Agregar el remote origin (reemplaza TU_USUARIO por tu username de GitHub)
git remote add origin https://github.com/christiangfv/strands-agents-workshop.git

# Verificar que el remote se agregó
git remote -v

# Hacer push inicial
git push -u origin main
```

### 3. Configurar Branches en GitHub

```bash
# Push de todas las branches
git push origin develop
git push origin feature/level-1-simple-agent
git push origin feature/level-2-basic-tools
git push origin feature/level-3-multi-tools
git push origin feature/level-4-planner-executor
git push origin feature/docs-and-testing
```

### 4. Configurar GitHub Pages (Opcional)

Para documentación:
1. Ve a **Settings** → **Pages**
2. **Source**: `Deploy from a branch`
3. **Branch**: `main` → `/docs`
4. Click **Save**

## 🏷️ Configurar Labels (Etiquetas)

En la sección **Issues** → **Labels**, crea estas etiquetas:

### Labels de Tipo
- `bug` - 🐛 Problemas o errores
- `enhancement` - ✨ Nuevas funcionalidades
- `documentation` - 📝 Mejoras en docs
- `question` - ❓ Preguntas o dudas

### Labels de Estado
- `good first issue` - 👶 Bueno para principiantes
- `help wanted` - 🆘 Necesita ayuda
- `wontfix` - 🚫 No se va a arreglar

### Labels de Nivel
- `level-1` - 🟢 Agente simple
- `level-2` - 🟡 Tools básicas
- `level-3` - 🟠 Multi-tools
- `level-4` - 🔴 Planner-executor

## 📊 Configurar Proyectos

1. Ve a **Projects** → **New project**
2. Elige **"Table"** o **"Board"**
3. Nombre: `Strands Agents Workshop Roadmap`
4. Crea columnas: `Backlog`, `In Progress`, `Review`, `Done`

## 🔐 Configurar Secrets (Opcional)

Para CI/CD avanzado:

1. Ve a **Settings** → **Secrets and variables** → **Actions**
2. Agrega secrets si necesitas:
   - `CODECOV_TOKEN` (para codecov si lo usas)
   - `PYPI_API_TOKEN` (para publicar en PyPI)

## 🤝 Configurar Pull Request Template

Crea el archivo `.github/pull_request_template.md`:

```markdown
## 📋 Descripción

Describe los cambios que estás proponiendo.

## 🎯 Tipo de Cambio

- [ ] 🐛 Bug fix
- [ ] ✨ Nueva funcionalidad
- [ ] 📝 Documentación
- [ ] 🎨 Estilo/código
- [ ] ♻️ Refactorización
- [ ] 🧪 Tests
- [ ] 🛠️ Configuración

## 🔍 ¿Cómo probar?

Describe cómo probar los cambios.

## 📚 Documentación

- [ ] He actualizado la documentación
- [ ] No requiere cambios en documentación

## ✅ Checklist

- [ ] Mis cambios siguen las guías de estilo del proyecto
- [ ] He ejecutado los tests localmente
- [ ] He actualizado los tests si corresponde
- [ ] Mi código compila sin warnings
- [ ] He probado manualmente los cambios
```

## 🎯 Configurar Branch Protection (Recomendado)

Para la branch `main`:

1. Ve a **Settings** → **Branches**
2. Click **"Add rule"**
3. **Branch name pattern**: `main`
4. Marca:
   - ✅ **Require a pull request before merging**
   - ✅ **Require approvals** (1 approval mínimo)
   - ✅ **Require status checks to pass**
   - ✅ **Require branches to be up to date**

## 🚀 Comandos Útiles

```bash
# Ver estado del repositorio
git status

# Ver branches
git branch -a

# Push de nueva branch
git checkout -b feature/nueva-funcionalidad
git push -u origin feature/nueva-funcionalidad

# Crear PR desde GitHub website
# Ve a la branch y click "Compare & pull request"
```

## 📈 Próximos Pasos

1. ✅ Crear repositorio en GitHub
2. ⏳ Hacer push inicial
3. ⏳ Configurar CI/CD
4. ⏳ Agregar colaboradores
5. ⏳ Crear releases

---

¡Tu repositorio de Strands Agents Workshop está listo para la comunidad! 🎉
