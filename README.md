# Prueba-de-Ruffier
# Especificaciones del Proyecto: Aplicación "Prueba de Ruffier"

## 1. Descripción del Proyecto
El proyecto consiste en el desarrollo de una aplicación de escritorio para computadora personal que permita a los usuarios realizar de manera independiente la **Prueba de Ruffier**. Esta prueba evalúa el estado del sistema cardiorrespiratorio y el rendimiento cardíaco durante el esfuerzo físico, entregando una interpretación automática de los resultados.

## 2. Lógica de la Prueba de Ruffier
La evaluación se basa en el registro del pulso en diferentes momentos de la prueba, junto con la edad del usuario.

### Procedimiento paso a paso:
1. El usuario descansa unos minutos y se toma el pulso durante **15 segundos** (P1).
2. El usuario realiza **30 sentadillas en 45 segundos**.
3. Inmediatamente después del ejercicio, se toma el pulso durante **15 segundos** (P2).
4. El usuario descansa durante **30 segundos**.
5. Tras el descanso, se toma el pulso nuevamente durante **15 segundos** (P3).

### Datos de entrada requeridos:
- **Edad** del usuario.
- **Tres mediciones de pulso** (P1, P2 y P3).

## 3. Especificaciones de la Interfaz de Usuario usando pyQt
La interfaz debe estar estructurada en tres pantallas principales utilizando widgets como `QLabel`, `QPushButton` y `QLineEdit`.

### Pantalla 1: Inicio
- **Componentes:**
  - **Textos informativos:** Mostrar el título de la aplicación y una breve descripción explicativa de qué es la Prueba de Ruffier y su propósito.
  - **Botón de acción:** Un botón principal de "Inicio" para comenzar la prueba. Al hacer clic en el botón de inicio, el usuario será redirigido a la siguiente pantalla para comenzar con la prueba.

### Pantalla 2: Ejecución y Recopilación de Datos
Es la pantalla principal donde el usuario ingresa los datos para realizar la prueba.
- **Componentes:**
  - **Entrada de datos:** Espacios para que el usuario escriba su edad y los resultados de las tres mediciones de pulso requeridas.
  - **Descriptivos:** Instrucciones claras que indiquen que debe hacer el usuario en cada paso.
  - **Botones de control de tiempo y flujo:**
    - **Botón 1:** Inicia un temporizador de 15 segundos para el primer pulso.
    - **Botón 2:** Inicia un temporizador de 45 segundos para la realización de las 30 sentadillas.
    - **Botón 3:** Inicia un temporizador de 1 minuto para el tiempo de descanso y la última toma de pulso.
    - **Botón 4:** Un botón de confirmación o  para enviar los datos ingresados, calcular el resultado y avanzar a la pantalla final.

### Pantalla 3: Resultados
 Muestra al usuario el resultado final de la prueba, presentando su Índice de Ruffier calculado y la interpretación de su estado de salud cardiovascular  basada en la tabla de edades.

 # Comandos de Git

## 1. Cómo abrir la terminal en Visual Studio Code
Para poder ejecutar los comandos de Git

- **Desde el menú:** Ve a la barra superior y selecciona **Ver > Terminal**

## 2. Ver el estado y la rama actual

- **Ver los archivos modificados, añadidos o eliminados:**
  ```bash
  git status
  ```
  *Este comando te indica qué archivos están listos para ser guardados y cuáles no.*

- **Ver en qué rama estás trabajando:**
  ```bash
  git branch
  ```
  *Lista todas las ramas locales. La rama en la que te encuentras actualmente estará marcada con un asterisco (`*`) y resaltada.*

## 3. Crear una nueva rama

- **Crear una nueva rama y cambiar a ella inmediatamente:**
  ```bash
  git checkout -b nombre-de-tu-nueva-rama
  ```
- **Moverse a una rama ya existente (por ejemplo, para volver a la rama principal main):**

  ```bash
  git checkout main
  ```

## 4. Preparar y guardar el trabajo (Commit)
Una vez que has hecho cambios en tu código, necesitas guardarlos en el historial de Git.

- **Paso 1: Añadir todos los archivos modificados al área de preparación:**
  ```bash
  git add .
  ```
  *El punto (`.`) indica que quieres agregar todos los archivos. Si solo quieres añadir un archivo específico, usa `git add nombre_del_archivo`.*

- **Paso 2: Guardar los cambios con un mensaje descriptivo:**
  ```bash
  git commit -m "Escribe aquí un mensaje claro sobre lo que modificaste"
  ```
## 5. Como hacer Merge
Cuando terminas de trabajar en tu rama secundaria, necesitas fusionar (merge) esos cambios a la rama principal.

1. **Asegúrate de haber guardado todos tus cambios en tu rama actual** (usando `git add .` y `git commit`).
2. **Cámbiate a la rama que va a recibir los cambios** (usualmente es `main` o `master`):
   ```bash
   git checkout main
   ```
3. **Actualiza tu rama principal** (por si alguien más subió cambios) antes de fusionar:
   ```bash
   git pull origin main
   ```
4. **Ejecuta el comando para fusionar tu rama de trabajo hacia la rama principal:**
   ```bash
   git merge nombre-de-tu-rama
   ```
   *Si hay conflictos de código, VSCode te los mostrará en el editor para que los resuelvas antes de finalizar el merge.*

## 6. Cambios de local a remoto

- **Subir tus cambios (commits) locales al repositorio remoto en GitHub:**
  ```bash
  git push origin nombre-de-tu-rama
  ```

- **Descargar y aplicar los últimos cambios del repositorio remoto a tu computadora:**
  ```bash
  git pull origin nombre-de-tu-rama
  ```

- **Ver el historial resumido de los commits realizados:**
  ```bash
  git log --oneline
  ```
  *Esto te mostrará una lista rápida de todos los cambios guardados con sus respectivos códigos de identificación.*