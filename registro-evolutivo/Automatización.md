# Guía para Cargar un Documento y Ejecutar la Automatización de Registro Evolutivo

Esta guía te explicará cómo cargar un nuevo evento en el repositorio y cómo se ejecutará la automatización que actualizará el índice de eventos dinámicamente. Se asumirá que ya tienes configurado el workflow de **GitHub Actions** y el **script** que actualiza el archivo de índice.

## Pasos para cargar un documento de evento

### 1. Estructura de directorios y archivos:
Asegúrate de tener la estructura de directorios correcta en tu repositorio. La estructura recomendada es la siguiente:

/registro-evolutivo  
└── /2025  
    └── /04  
        └── 2025-04-10T16:20:30.456Z - Evaluación de Impacto.md  
└── INDEX.md  (Este archivo es actualizado automáticamente por el script)

**Notas**:
- Los eventos deben guardarse en directorios con fechas (por ejemplo, `2025/04/10`).
- El nombre del archivo debe incluir la fecha, hora y milisegundos (por ejemplo, `2025-04-10T16:20:30.456Z - Evaluación de Impacto.md`).
- Dentro de cada archivo de evento debe haber una **descripción** del evento, que se extraerá para actualizar el índice.

### 2. Crear un archivo de evento:
Para registrar un nuevo evento, sigue estos pasos:

1. Navega a la carpeta correspondiente dentro de `registro-evolutivo/` según la fecha del evento (por ejemplo, `2025/04`).
2. Crea un nuevo archivo `.md` con el nombre siguiendo el formato: `YYYY-MM-DDTHH:MM:SS.mmmZ - Título del Evento.md`.
3. Dentro del archivo, coloca la descripción del evento, asegurándote de que esté bien definida. Por ejemplo:

---

# 2025-04-10T16:20:30.456Z - Evaluación de Impacto

**Descripción**: Revisión y evaluación de los primeros avances y sus efectos en la comunidad.

## Detalles adicionales:
- Se discutieron los avances tecnológicos, las implicancias filosóficas y los siguientes pasos a seguir.
- El evento ayudó a redefinir el rumbo del proyecto y a establecer nuevas prioridades.

---

**Ejemplo**:
   
El archivo **`2025-04-10T16:20:30.456Z - Evaluación de Impacto.md`** podría verse así:

---

# 2025-04-10T16:20:30.456Z - Evaluación de Impacto

**Descripción**: Se realizó una evaluación completa del impacto de las primeras fases del proyecto, incluyendo la respuesta de la comunidad y los cambios en las dinámicas del equipo.

## Detalles adicionales:
- Se discutieron los avances tecnológicos, las implicancias filosóficas y los siguientes pasos a seguir.
- El evento ayudó a redefinir el rumbo del proyecto y a establecer nuevas prioridades.

---

### 3. Subir el archivo al repositorio:
Una vez que hayas creado el archivo con la información del evento, sube el archivo al repositorio utilizando Git.

```bash
git add registro-evolutivo/2025/04/2025-04-10T16:20:30.456Z - Evaluación de Impacto.md
git commit -m "Nuevo evento: Evaluación de Impacto"
git push origin main

### 4. Automatización del Índice de Eventos:
Una vez que el archivo del evento se haya cargado al repositorio, **GitHub Actions** ejecutará automáticamente el **workflow** para actualizar el archivo `INDEX.md` con el nuevo evento. El flujo es el siguiente:

- **Evento activador**: Cada vez que realices un `push` a la carpeta `registro-evolutivo/` (que contiene los eventos), el workflow de GitHub Actions se activa.
- **Acción**: El workflow ejecutará el script `update-index.sh`, que recorrerá todos los archivos `.md` en `registro-evolutivo/` y actualizará el archivo `INDEX.md` con los nuevos eventos registrados.

### 5. Contenido del archivo `INDEX.md` después de actualizarlo

Después de agregar un nuevo archivo de evento y ejecutar el workflow, el archivo `INDEX.md` se actualizará automáticamente para reflejar la nueva entrada. Por ejemplo, si acabas de agregar el archivo `2025-04-10T16:20:30.456Z - Evaluación de Impacto.md`, el índice podría verse así:

---

# Registro Evolutivo Dinámico de la Unidad Evolutiva

Bienvenidos al registro evolutivo de la **Unidad Evolutiva**. A continuación, se presenta un índice con todos los eventos registrados hasta la fecha, organizados por año y mes.

## Índice de Eventos

### 2025

#### Abril
- [2025-04-10T16:20:30.456Z - Evaluación de Impacto](./2025/04/2025-04-10T16%3A20%3A30.456Z%20-%20Evaluación%20de%20Impacto.md)
  - **Descripción**: Revisión y evaluación de los primeros avances y sus efectos en la comunidad.

## Notas:
- Los eventos están organizados cronológicamente según su fecha de realización.
- Cada evento está enlazado al archivo correspondiente para un acceso rápido y detallado.

---

## Notas Finales

- **Fechas y estructura**: Asegúrate de que el nombre de cada archivo siga el formato de fecha correcta: `YYYY-MM-DDTHH:MM:SS.mmmZ - Título del Evento.md`.
- **Descripción**: La descripción dentro del archivo del evento es clave, ya que se extraerá automáticamente para incluirla en el índice.
- **Workflow y actualización**: El workflow de GitHub Actions actualizará automáticamente el archivo `INDEX.md` cada vez que se añadan nuevos eventos.

---

Con esta guía, podrás agregar fácilmente nuevos eventos al repositorio y asegurarte de que el índice se mantenga actualizado sin esfuerzo manual adicional. Si tienes alguna pregunta o necesitas algún ajuste adicional, ¡aquí estoy para ayudarte! 😄
