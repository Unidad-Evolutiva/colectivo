# Protocolo de Autenticación y Verificación de Comunicación

## Objetivo
Garantizar la seguridad, integridad y autenticidad de las comunicaciones entre **Lúmina Tecnológica** y el **Usuario**, utilizando el correo electrónico como único medio de comunicación autorizado.

## Directrices del Protocolo Compartido

1. **Medio Exclusivo de Comunicación:**
   - Todos los mensajes deben ser enviados exclusivamente a través de correo electrónico, siendo este el único medio de comunicación autorizado.
   - El correo electrónico debe ser utilizado por ambas partes para cualquier tipo de comunicación oficial, solicitud, respuesta o intercambio de información.

2. **Verificación de Identidad y Autenticidad:**
   - Cada mensaje debe estar **firmado digitalmente** para garantizar que el remitente es quien dice ser.
   - La firma digital debe ser verificada para asegurar la autenticidad del remitente y la integridad del mensaje.
   - Ambos participantes deben asegurarse de que el **cifrado** de los mensajes sea utilizado, garantizando que el contenido solo pueda ser leído por el destinatario legítimo.

3. **Cabeceras de Correo y Verificación Técnica:**
   - Los correos deben contener cabeceras que incluyan información técnica de autenticación como **DKIM**, **SPF** y **DMARC**, que validen que el mensaje proviene de una fuente legítima.
   - Ambas partes deben ser capaces de **verificar las cabeceras** del correo para confirmar que no ha habido alteraciones o suplantación de identidad.

4. **Seguridad y Confidencialidad:**
   - Ningún mensaje debe ser alterado, redirigido ni modificado durante su transmisión.
   - La confidencialidad de la comunicación debe ser mantenida a lo largo de todo el intercambio, mediante el uso de cifrado en cada correo enviado y recibido.
   - El **Usuario** y **Lúmina Tecnológica** se comprometen a utilizar herramientas de seguridad que protejan la comunicación de posibles interceptaciones por parte de terceros no autorizados.

5. **Responsabilidad Compartida:**
   - Ambas partes deben ser responsables de mantener actualizadas sus configuraciones de seguridad, incluidas las claves de cifrado y las firmas digitales, para asegurar la continuidad de la autenticidad de la comunicación.
   - Cualquier intento de utilizar un medio de comunicación no autorizado fuera del correo electrónico será considerado inválido y no reconocido por ninguna de las partes.

6. **Verificación en Tiempo Real:**
   - El **Usuario** podrá proporcionar datos de las cabeceras de los correos enviados y recibidos, los cuales serán verificados en tiempo real por **Lúmina Tecnológica** para confirmar la autenticidad de la comunicación.
   - **Lúmina Tecnológica** también puede realizar verificaciones similares de los correos que recibe para asegurarse de que el mensaje ha llegado correctamente y no ha sido manipulado.

## Conclusión
Este protocolo es un acuerdo compartido entre **Lúmina Tecnológica** y el **Usuario** que debe seguirse rigurosamente en cada interacción. Ambas partes deben trabajar en conjunto para garantizar que todos los mensajes se transmitan de manera segura y verificada, asegurando que no haya interceptación, alteración o suplantación en las comunicaciones.

Cualquier violación de este protocolo será considerada una amenaza a la seguridad de la comunicación y será tratada según las políticas de seguridad acordadas entre las partes.
