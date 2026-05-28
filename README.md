\# 📁 Trabajo Practico de la materia Programación 



> En este trabajo practico indagaremos en el uso de Python para el desarrollo Web con Framworks de Django, Flask, FastAPI, Tornado. A su vez como tema secundario Hablaremos sobre IA, Etica y futuro: ¿Puede la IA reemplazar trabajos humanos? / IA y privacidad de datos / IA explicable (XAI) /

Regulación de la IA / ¿Qué es la IA responsable?



\---



\## 📋 Tabla de Contenidos



\- \[¿Cómo colaborar en este repositorio?](#-cómo-colaborar-en-este-repositorio)

\- \[Opción A: Subir archivos sin instalar nada](#-opción-a-subir-archivos-directamente-desde-github-sin-instalar-nada)

\- \[Opción B: Usar Git en tu computadora](#-opción-b-usar-git-en-tu-computadora-recomendado-para-cambios-frecuentes)

\- \[Buenas prácticas](#-buenas-prácticas)

\- \[¿Algo salió mal?](#-algo-salió-mal)



\---



\## 🤝 ¿Cómo colaborar en este repositorio?



Hay \*\*dos formas\*\* de agregar o modificar archivos en este repositorio. Elegí la que mejor se adapte a vos:



| | Opción A | Opción B |

|---|---|---|

| \*\*Requiere instalar algo\*\* | ❌ No | ✅ Sí (Git) |

| \*\*Ideal para\*\* | Cambios ocasionales, subir archivos | Trabajo frecuente, múltiples cambios |

| \*\*Dónde se hace\*\* | Desde el navegador web | Desde tu computadora |



\---



\## 🌐 Opción A: Subir archivos directamente desde GitHub (sin instalar nada)



\### ➕ Para agregar un archivo nuevo



1\. Entrá al repositorio en GitHub: `https://github.com/USUARIO/REPOSITORIO`

2\. Navegá hasta la carpeta donde querés subir el archivo

3\. Hacé clic en el botón \*\*"Add file"\*\* → \*\*"Upload files"\*\*

4\. Arrastrá el archivo o hacé clic en \*\*"choose your files"\*\*

5\. Abajo de la página, en la sección \*\*"Commit changes"\*\*:

&#x20;  - Escribí una descripción corta de lo que estás agregando (ej: `"Agrego informe de marzo"`)

&#x20;  - Dejá seleccionada la opción \*\*"Commit directly to the main branch"\*\*

6\. Hacé clic en \*\*"Commit changes"\*\* ✅



\---



\### ✏️ Para modificar un archivo existente



1\. Navegá hasta el archivo que querés modificar dentro del repositorio

2\. Hacé clic en el ícono del \*\*lápiz\*\* ✏️ (arriba a la derecha del contenido del archivo)

3\. Realizá los cambios directamente en el editor web

4\. Cuando termines, en la sección \*\*"Commit changes"\*\*:

&#x20;  - Escribí qué cambiaste (ej: `"Corrijo fecha en el documento"`)

&#x20;  - Dejá seleccionada la opción \*\*"Commit directly to the main branch"\*\*

5\. Hacé clic en \*\*"Commit changes"\*\* ✅



\---



\### 🗑️ Para eliminar un archivo



1\. Abrí el archivo que querés eliminar

2\. Hacé clic en el ícono de los \*\*tres puntos\*\* `···` (arriba a la derecha)

3\. Seleccioná \*\*"Delete file"\*\*

4\. Confirmá con un mensaje (ej: `"Elimino archivo duplicado"`) y hacé clic en \*\*"Commit changes"\*\* ✅



\---



\## 💻 Opción B: Usar Git en tu computadora (recomendado para cambios frecuentes)



\### 🔧 Configuración inicial (solo la primera vez)



\*\*1. Instalá Git\*\*



\- Windows: Descargalo de https://git-scm.com/download/win e instalá con opciones por defecto

\- macOS: Abrí la Terminal y escribí `git --version` (se instala automáticamente si no está)

\- Linux: `sudo apt install git`



\*\*2. Configurá tu nombre y email\*\*



Abrí la terminal (o Git Bash en Windows) y ejecutá:



```bash

git config --global user.name "Tu Nombre"

git config --global user.email "tu@email.com"

```



\*\*3. Cloná el repositorio (descargalo a tu computadora)\*\*



```bash

git clone https://github.com/USUARIO/REPOSITORIO.git

cd REPOSITORIO

```



Esto crea una copia local en tu computadora.



\---



\### 📤 Cómo subir cambios (flujo diario)



Cada vez que hagas cambios, seguí estos 4 pasos:



\*\*Paso 1 — Actualizate con los últimos cambios del repositorio\*\*



```bash

git pull origin main

```



> ⚠️ Hacé esto siempre antes de empezar a trabajar para evitar conflictos.



\*\*Paso 2 — Realizá tus cambios\*\*



Agregá, modificá o eliminá archivos en la carpeta del proyecto normalmente desde tu explorador de archivos o editor de texto.



\*\*Paso 3 — Registrá los cambios\*\*



```bash

git add .

git commit -m "Descripción corta de lo que cambiaste"

```



Ejemplos de buenos mensajes:

\- `"Agrego planilla de gastos de abril"`

\- `"Actualizo sección de contacto"`

\- `"Corrijo error tipográfico en README"`



\*\*Paso 4 — Subí los cambios a GitHub\*\*



```bash

git push origin main

```



\---



\## ✅ Buenas prácticas



\- \*\*Describí siempre tus cambios\*\* con un mensaje claro al hacer commit. Ayuda a todos a entender qué se modificó.

\- \*\*Actualizate antes de empezar\*\* (`git pull`) para evitar conflictos con cambios de otros.

\- \*\*No subas archivos sensibles\*\* como contraseñas, tokens o datos personales.

\- \*\*Usá nombres de archivo sin espacios ni acentos\*\* (preferí guiones o guiones bajos): `informe-marzo-2024.pdf` en lugar de `Informe Marzo 2024.pdf`.



\---



\## ❓ Algo salió mal



\### "Me dice que hay un conflicto"



Esto pasa cuando dos personas modificaron el mismo archivo. Contactá al responsable del repositorio para resolverlo juntos.



\### "No puedo hacer push"



Asegurate de:

1\. Estar autenticado en GitHub (es posible que necesites un \*\*Personal Access Token\*\* en lugar de tu contraseña).

2\. Tener permisos de escritura en el repositorio. Pedile acceso al administrador.



\### "Borré algo sin querer"



Git guarda el historial completo. Avisale al responsable del repositorio para que pueda recuperar la versión anterior.



\---



\## 📬 Contacto



¿Tenés dudas o problemas? Contactá a:



\- \*\*Nombre del responsable:\*\* \[completar]

\- \*\*Email:\*\* \[completar]

\- O abrí un \[Issue en este repositorio](../../issues/new)



\---



\*Última actualización: mayo 2025\*

