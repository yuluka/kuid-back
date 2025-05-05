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

Este repositorio contiene la lógica de negocio del sistema. Se encuentra desarrollado en FastAPI.

--- 

## Ejecución

Para la ejecución del proyecto, primero se crea y se activa el virtual environment

(windows: puede ser 'python3' o 'python' or 'py') 

```bash
python3 -m venv venv
venv\Scripts\activate
```

Se instalan las dependencias especificadas en [`requirements.txt`](requirements.txt) 

```bash
pip install -r requirements.txt
```

Además se crea un archivo .env, que contenga la URL de la base de datos. Actualmente puede ser local. Agrega esto al archivo y guardalo 

```bash
DATABASE_URL=sqlite:///./local_database.db
```

Además, debes crear este archivo .db, con base en el archivo sql que está en la carpeta docs. Para crearlo puedes importar el SQL usando DB Browser y crear la base de datos .db desde ahí

Finalmente, para correr la aplicación se debe usar el comando:

```bash
uvicorn src.main:app
```

O también con el comando:

```bash
fastapi dev src/main.py
```

Cuando ingreses al login, ve a la opción de "registrarte" y registrate como en una aplicación cualquiera, correo y contraeseña, y luego pasas al login ahora si para ingresar