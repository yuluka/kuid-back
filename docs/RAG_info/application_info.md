# KÜID Aplicación RAG - Base de Conocimiento

**Propósito del Documento:** Este documento proporciona información estructurada sobre las funcionalidades, pantallas y conceptos de la aplicación de seguros KÜID. Su objetivo es servir como base de conocimiento para un sistema de Generación Aumentada por Recuperación (RAG) para asistir a los usuarios explicando funcionalidades y la ubicación de elementos dentro de la aplicación.

---

## Pantalla Principal

**1. Propósito de la pantalla:**

Mostrar un resumen general del estado actual del seguro flexible del usuario, incluyendo cobertura, pagos, eventos próximos y gamificación.

**2. Componentes principales de la interfaz:**

| Sección                                  | Descripción                                                                                                                                                                                                                                         |
| ---------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Encabezado**                           | Mensaje de bienvenida personalizado con el nombre del usuario.                                                                                                                                                                                      |
| **Estado de tu cobertura**               | Muestra si la cobertura está activa, la fecha del próximo pago, el valor del pago mensual, y los módulos contratados.                                                                                                                               |
| **Próximos eventos**                     | Lista de eventos importantes, como vencimientos de pago y revisiones médicas anuales, con enlaces para ver todos.                                                                                                                                   |
| **Actividad reciente**                   | Registro de eventos importantes recientes como pagos procesados, conexión con dispositivos, y recompensas aplicadas.                                                                                                                                |
| **Objetivos y recompensas**              | Seguimiento de metas gamificadas como pasos diarios y verificaciones médicas, con barras de progreso visuales.                                                                                                                                      |
| **Botón de acción:** `Ajustar cobertura` | Permite al usuario modificar los módulos de su seguro contratado.                                                                                                                                                                                   |
| **Sidebar (menú lateral)**               | Navegación principal con las siguientes secciones: Inicio, Perfil, Dispositivos y Apps, Configuración de Seguro, Recompensas, Historias reales, Alertas, y Cerrar sesión. Incluye notificaciones activas (ej. "2" en Recompensas y "3" en Alertas). |

**3. Interacciones del usuario esperadas:**

* Navegar entre secciones desde el menú lateral.
* Ajustar su cobertura usando el botón correspondiente.
* Consultar detalles de su actividad reciente.
* Seguir su progreso hacia metas y desbloqueo de recompensas.
* Revisar próximos eventos importantes y agendar acciones.

**4. Relación con el flujo general de la app:**

Esta es la pantalla principal a la que el usuario accede tras iniciar sesión. Centraliza el acceso a las demás secciones del sistema de protección KÜID y sirve como punto de entrada para todas las acciones clave.

Perfecto, aquí tienes la ficha técnica estructurada para la segunda pantalla:

---

## Pantalla: Perfil de Usuario

**1. Propósito de la pantalla:**

Permitir al usuario visualizar, editar y gestionar su información personal, preferencias de comunicación y configuraciones de seguridad.

**2. Componentes principales de la interfaz:**

| Sección                  | Descripción                                                                                                                                                              |
| ------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Información Personal** | Campos con datos del usuario: nombre completo, correo electrónico, teléfono, dirección y fecha de nacimiento. Incluye un botón `Editar` para modificar esta información. |
| **Seguridad**            | Contiene opciones clave para proteger la cuenta: <ul><li>`Cambiar contraseña`</li><li>`Configurar autenticación de dos factores`</li></ul>                               |
| **Preferencias**         | Permite activar o desactivar: <ul><li>Notificaciones por email</li><li>Comunicaciones de marketing mediante checkboxes</li></ul>.                                        |

**3. Interacciones del usuario esperadas:**

* Revisar y actualizar su información personal.
* Cambiar la contraseña para reforzar la seguridad.
* Activar la autenticación de dos factores como medida adicional.
* Ajustar sus preferencias de comunicación según sus intereses.

**4. Relación con el flujo general de la app:**

Es una pantalla de configuración que permite al usuario mantener sus datos actualizados y seguros, y controlar cómo desea ser contactado por KÜID.

Perfecto, aquí tienes la ficha técnica estructurada para la tercera pantalla:

---

### Pantalla: Dispositivos y Aplicaciones

**1. Propósito de la pantalla:**

Gestionar la conexión de dispositivos wearables y aplicaciones externas para mejorar el monitoreo, la protección y personalización del servicio.

**2. Componentes principales de la interfaz:**

| Sección                    | Descripción                                                                                                                                                                                                                                               |
| -------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Dispositivos wearables** | Muestra el estado de conexión de dispositivos como Smartwatch o Smartphone. Se puede conectar, desconectar y ver la fecha de última sincronización. Incluye botón `Sincronizar todo ahora`. También se puede `+ Agregar dispositivo`.                     |
| **Aplicaciones**           | Permite vincular otras apps útiles para mejorar la protección: <ul><li>**Calendario** (sincroniza viajes para alertas)</li><li>**Agregador Financiero** (verifica ingresos)</li><li>**Portal de Salud** (comparte diagnósticos de forma segura)</li></ul> |

**3. Interacciones del usuario esperadas:**

* Conectar o desconectar dispositivos wearables.
* Agregar nuevos dispositivos compatibles.
* Sincronizar la información manualmente.
* Integrar aplicaciones externas útiles para la protección personalizada.
* Ver fechas de última sincronización.

**4. Relación con el flujo general de la app:**

Es una pantalla clave para la personalización de la protección que ofrece KÜID, ya que permite ampliar el monitoreo del estado del usuario a través de múltiples fuentes de datos.

Perfecto, gracias por la aclaración.

Te armaré la **estructura descriptiva de las pantallas** de la aplicación de seguros que aparece en tus capturas, con el enfoque ideal para usar en un sistema RAG (Retrieval-Augmented Generation), es decir: descripciones claras, separadas por pantalla, modulares y fácilmente indexables.

---

### 🟥 Pantalla: **Configuración de Seguro**

**Objetivo**:

Permitir al usuario personalizar su cobertura mensual seleccionando módulos de protección.

**Secciones principales**:

1. **Título y descripción principal**

   * Título: `Configuración de Seguro`
   * Descripción: `Personaliza tu cobertura según tus necesidades actuales.`

2. **Módulos de protección**

   * Disposición en formato de tarjetas (cards) seleccionables.
   * Cada tarjeta incluye:

     * Ícono representativo.
     * Nombre del módulo.
     * Descripción breve.
     * Precio por mes.
   * Módulos disponibles:

     * **Salud**: Cobertura para tu bienestar físico y mental. `$50/mes`
     * **Protección de Ingresos**: Protege tus ganancias en caso de imposibilidad para trabajar. `$40/mes`
     * **Familia**: Asegura el futuro de tus hijos. `$30/mes`
     * **Mascotas**: Cuidado para tus amigos peludos. `$20/mes`
     * **Viajes**: Cobertura para imprevistos durante tus viajes. `$15/mes`

3. **Costo mensual total**

   * Barra de progreso que representa el total acumulado.
   * Muestra el valor actual en texto, por ejemplo: `Costo mensual total: $125` o `$155`

4. **Botón de acción**

   * Botón `Guardar cambios`, ubicado en la parte inferior.
   * Permite confirmar las selecciones hechas.

---

**Sección: Preguntas sobre tu cobertura**

**Objetivo**:

Permitir al usuario hacer preguntas específicas sobre la cobertura que ha configurado.

**Elementos de la sección**:

* Título: `Preguntas sobre tu cobertura`
* Subtítulo: `¿Tienes dudas sobre tu cobertura actual? Pregunta aquí y te responderemos.`
* Campo de texto:

  * Placeholder de ejemplo:
    `Ejemplo: ¿Esta configuración me cubriría en caso de un choque con mi carro?`
* Botón: `Preguntar` (ícono de avión de papel)

Gracias por compartir la nueva pantalla. Aquí te dejo la descripción estructurada de esta nueva vista siguiendo el mismo formato para integrarla fácilmente en un sistema RAG.

---

## Pantalla: Recompensas y Logros

**Objetivo**:
Visualizar los beneficios, incentivos y metas alcanzadas por el usuario dentro del ecosistema KÜID.

**Secciones principales**:

1. **Título y descripción principal**

   * Título: `Recompensas y Logros`
   * Descripción: `Aquí hay un resumen de los beneficios y recompensas que has desbloqueado con KÜID.`

2. **Listado de recompensas (tarjetas horizontales)**
   Cada tarjeta incluye:

   * **Ícono representativo del logro.**
   * **Nombre del logro.**
   * **Descripción del beneficio.**
   * **Objetivo necesario para desbloquearlo.**
   * **Barra de progreso** (de 0% a 100%) indicando avance.
   * **Estado del logro**:

     * `Conseguido`: fondo verde claro y check.
     * `En progreso`: fondo neutro y botón con texto `En progreso`.
   * En algunos casos, incluye el botón `Ver detalles`.

Perfecto. Aquí tienes la descripción estructurada de la pantalla **Historias Reales**, siguiendo el mismo formato que las anteriores.

---

## Pantalla: Historias Reales

**Objetivo**:

Mostrar testimonios de usuarios reales sobre cómo la protección adaptativa de KÜID les ha ayudado en situaciones concretas de la vida diaria.

**Elementos principales**:

1. **Encabezado principal**

   * Título: `Historias Reales`
   * Descripción: `Descubre cómo la protección adaptativa de KÜID ha ayudado a los miembros en situaciones de la vida real.`

2. **Ícono decorativo**:

   * Ícono de libro abierto en el centro, justo debajo del encabezado.

3. **Testimonios individuales (tarjetas)**

   Cada tarjeta contiene:

   * **Título de la historia (en inglés)**
   * **Texto del testimonio** (en español, entre comillas, con estilo de cita)
   * **Nombre del testigo** (formato: `- Nombre Inicial`)
   * **Etiquetas** que clasifican el tipo de protección involucrada (estilo pill, fondo lavanda claro)

---

## Pantalla: Notificaciones

**Objetivo**:

Permitir al usuario mantenerse informado sobre alertas relevantes, recordatorios y actualizaciones del servicio KÜID.

**Elementos principales**:

1. **Encabezado principal**

   * Título: `Notificaciones`
   * Descripción: `Mantente informado sobre alertas y actualizaciones importantes.`

2. **Controles superiores**

   * Icono de campana con contador: `🔔 X sin leer`
   * Botón: `Marcar todas como leídas`

3. **Sección principal**

   * Título de la sección: `Alertas y Notificaciones`

4. **Listado de notificaciones**

   Cada notificación contiene:

   * **Ícono representativo** del tipo de alerta (color e ícono varían según el tipo)
   * **Título** en color destacado y con un punto indicando si está sin leer
   * **Descripción** o mensaje explicativo
   * **Fecha** (alineada a la derecha)
   * **Acción secundaria**: Enlace `Marcar como leída` (color púrpura)