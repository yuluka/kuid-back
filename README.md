# KÜID: Tu escudo flexible - Backend

## Integrantes

- Juan Diego Lora Lara
- Santiago Prado Larrarte
- Yuluka Gigante Muriel

---

## Acerca de KÜID

Incentivados por el reto planteado por **_Global Seguros_**, creamos **KÜID**, una experiencia de protección que se **adapta a tu estilo de vida**, no al revés. Desde el primer momento, una app con onboarding emocional y lenguaje simple te permite armar tu plan como un combo personalizado: solo agregas lo que realmente necesitas (salud, ingresos, hijos, mascotas, etc.) y puedes activarlo o pausarlo según tu realidad diaria. 

La plataforma se integra con tu realidad y herramientas cotidianas. Tus apps, wearables, pagos y datos financieros (si así lo decides), forman parte de la experiencia de protección. **KÜID** se basa en los datos recopilados para darte recomendaciones en tiempo real, alertarte sobre riesgos y premiarte por hábitos saludables o decisiones responsables.

Además, cuentas con asistencia humana directa, contratos transparentes y coberturas explicadas con historias reales y ejemplos simples. **Si no usas tu seguro, tranquilo**, parte de tu dinero se convierte en ahorro o cashback. Y si lo compartes en grupo (familia, comunidad laboral, colectivo), accedes a beneficios compartidos y precios más bajos.

Con nosotros, **protegerse deja de ser un trámite** y se convierte en una experiencia de cuidado activo, inteligente y cercana.

---

## Acerca del proyecto

Por el momento, **KÜID** se encuentra en su etapa de validación y evaluación, por lo que está disonible un MVP funcional que busca familiarizar a nuevos usuarios con esta propuesta tan innovadora, y enamorarlos de nuestra visión sin límites.

Este repositorio contiene la lógica de negocio del sistema que se encuentra en desarrollo y está preparada para brindar las funcionalidades básicas del sistema. Se encuentra desarrollado en FastAPI.

--- 

## Ejecución

Si deseas ejecutar el proyecto de forma local, puedes hacerlo. Sin embargo, en este momento, el sistema se encuentra desplegado sobre la plataforma [Railway](https://railway.com/), en el dominio:

`kuid-back-production.up.railway.app`

Puede encontrar un listado de los [endpoints expuestos acá](kuid-back-production.up.railway.app/docs).

Para la ejecución del proyecto en local se deben seguir los siguientes pasos:

1. Crea y activar el entorno virtual:

    ```bash
    python3 -m venv venv
    .\venv\Scripts\activate
    ```

2. Instalar las dependencias especificadas en [`requirements.txt`](requirements.txt):

    ```bash
    pip install -r requirements.txt
    ```
    > **Nota:** La instalación puede tomar un tiempo debido a la cantidad de dependencias del proyecto.

3. Crear el archivo con las variables de entorno `.env`:

    ```
    DATABASE_URL=db_url
    GROQ_API_KEY=groq_api_key
    OPENAI_API_KEY=openai_api_key
    COHERE_API_KEY=cohere_api_key
    MODEL=deepseek-r1-distill-llama-70b
    LANGUAGE=ES
    ```

4. Crear la base de datos:

    Para la creación de la base de datos se puede hacer uso del [script de creación](docs/DB/db_creation.sql).

5. Ejecutar

    ```bash
    uvicorn src.main:app --reload
    ```
